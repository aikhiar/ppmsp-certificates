"""
Correctness tests (pytest tests/test_kernels.py, about 2-3 minutes):
  * every method returns a feasible schedule whose reported peak is its true peak
  * certified lower bounds never exceed the optimum (exact standard model on small instances)
  * a priori guarantees of CE, MT and IR hold
  * Numba kernels agree with plain numpy (loads, greedy, sums of squares)
  * statistics agree with scipy (Friedman) and textbook values (Holm, Nemenyi)
  * configuration merging and run keys
"""

import os
import sys

import numpy as np
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import cri.problems.ppmsp  # noqa: E402,F401  (registers the problem and the methods)
from cri.analysis import metrics as MT  # noqa: E402
from cri.analysis import stats as S  # noqa: E402
from cri.core.config import deep_merge  # noqa: E402
from cri.core.registry import make_method  # noqa: E402
from cri.core.runner import expand_grid, run_key  # noqa: E402
from cri.problems.ppmsp import context as CX  # noqa: E402
from cri.problems.ppmsp import exact as EX  # noqa: E402
from cri.problems.ppmsp import generators as G  # noqa: E402
from cri.problems.ppmsp import kernels as K  # noqa: E402
from cri.problems.ppmsp.instance import UNIT  # noqa: E402

SPECS = [{"class": "G"}, {"class": "G", "params": {"mode": "budget"}}, {"class": "RR", "params": {"N": 500}},
         {"class": "RR", "params": {"stop": "budget"}}, {"class": "RLP", "params": {"trials": 5}},
         {"class": "SA", "params": {"N": 2000}}, {"class": "SA", "params": {"stop": "budget"}},
         {"class": "SA", "params": {"init": "G", "N": 2000}},
         {"class": "CE", "params": {"matrix": "lp", "estimator": "excess"}},
         {"class": "CE", "params": {"matrix": "cut", "estimator": "union"}},
         {"class": "CE", "params": {"matrix": "conf", "estimator": "component"}},
         {"class": "IR"}, {"class": "MT", "params": {"matrix": "lp"}}, {"class": "MT", "params": {"matrix": "cut", "mode": "budget"}},
         {"class": "LLS"}, {"class": "WLNS"}, {"class": "CRI"}, {"class": "CRI", "params": {"complete": True}},
         {"class": "GUROBI", "params": {"model": "standard"}}, {"class": "GUROBI", "params": {"model": "aggregated"}},
         {"class": "ASAP"}, {"class": "GNP"}, {"class": "BK"}, {"class": "NFDH"}, {"class": "ZAIDI_H"},
         {"class": "ZAIDI_ILS", "params": {"max_trials": 100}}, {"class": "ZAIDI_ILS", "params": {"restart": True}},
         {"class": "HUNSAKER"}, {"class": "AFSHAR_BB"}, {"class": "AN_HYBRID", "params": {"pop": 12, "maxgen": 30}},
         {"class": "AN_HYBRID", "params": {"variant": "PAR", "ls": "LS1", "pop": 12, "maxgen": 30}}]


@pytest.fixture(scope="module")
def env():
    import gurobipy as gp
    from cri.problems.ppmsp import PPMSP
    e = gp.Env(empty=True); e.setParam("OutputFlag", 0); e.start()
    # compile every Numba kernel first, as every campaign worker does (run.warmup): on a fresh clone the
    # first calls compile, and the budget tests must not pay for it
    PPMSP.warmup(e)
    return e


@pytest.fixture(scope="module")
def instances():
    rng = np.random.default_rng(11)
    return [G.FAMILIES[f](n, T, rng) for f, n, T in (("omega", 15, 24), ("staggered", 25, 24), ("overnight", 12, 24),
                                                     ("pcmax", 10, 4), ("single", 20, 24))]


def test_kernels_against_numpy(instances):
    for inst in instances:
        K.seed_numba(3)
        x = K.random_schedule(inst.s, inst.e, inst.p, inst.T)
        assert inst.is_feasible(x)
        L = K.loads_of(x, inst.wu)
        assert np.array_equal(L, inst.loads(x))
        assert K.sum_sq(L) == int((L.astype(np.int64) ** 2).sum())
        xg, Lg = K.greedy_vf(inst.s, inst.e, inst.p, inst.wu, inst.T, 5)
        assert inst.is_feasible(xg) and np.array_equal(Lg, inst.loads(xg))


def test_methods_feasible_and_consistent(instances, env):
    for inst in instances:
        ctx = CX.make_context(inst, env, {"conf_time_limit": 10})
        for sp in SPECS:
            r = make_method(sp).run(inst, ctx, 1.0, 0)
            if r.get("status") == "not_available":
                continue
            x = r["solution"]
            assert inst.is_feasible(x), (inst.family, sp)
            assert abs(inst.peak(x) - r["objective"]) < 1e-6, (inst.family, sp, inst.peak(x), r["objective"])
            g = r.get("guarantee", np.nan)
            if g == g:
                assert r["objective"] <= g + 1e-6, (inst.family, sp, r["objective"], g)


def test_lower_bounds_valid(env):
    rng = np.random.default_rng(23)
    for f in ("omega", "staggered", "overnight", "single"):
        for _ in range(3):
            inst = G.FAMILIES[f](12, 16, rng)
            ctx = CX.make_context(inst, env, {"conf_time_limit": 20})
            opt = EX.solve_standard(inst, env, 60.0)
            assert opt["proven"]
            lb = ctx.get("lb")
            assert lb <= opt["peak"] + 1e-6, (f, lb, opt["peak"])
            b = ctx.get("bounds")
            assert b["U_best"] >= opt["peak"] - 1e-6, (f, b["U_best"], opt["peak"])
            agg = EX.solve_aggregated(inst, env, 60.0)
            assert abs(agg["peak"] - opt["peak"]) < 1e-6          # Theorem 3.3: same optimum


def test_statistics():
    from scipy import stats
    rng = np.random.default_rng(0)
    import pandas as pd
    M = pd.DataFrame(rng.normal(size=(20, 4)) + np.array([0, 0.3, 0.6, 1.0]), columns=list("abcd"))
    M.iloc[0, :] = 1.0                                      # a block of ties
    fr = S.friedman(M)
    ref = stats.friedmanchisquare(*[M[c] for c in M.columns])
    assert abs(fr["chi2"] - ref.statistic) < 1e-8
    assert abs(S.nemenyi_cd(4, 20) - 1.0488) < 2e-3        # Demsar (2006): q_0.05(k=4) = 2.569
    p = np.array([0.01, 0.04, 0.03, 0.005])
    assert np.allclose(S.holm(p), [0.03, 0.06, 0.06, 0.02])
    assert S.cliffs_delta([1, 2], [3, 4]) == -1.0 and S.a12([1, 2], [3, 4]) == 1.0


def test_metrics_primal_integral():
    tr = [(1.0, 12.0), (2.0, 10.0)]
    # gap 1 on [0,1], 2/12 on [1,2], 0 on [2,4]
    assert abs(MT.primal_integral(tr, 10.0, 4.0) - (1 + 2 / 12) / 4) < 1e-12
    assert MT.time_to_target(tr, 10.0) == 2.0 and MT.time_to_target(tr, 9.0) == np.inf


def test_config_and_keys():
    a = {"x": {"y": 1, "z": [1, 2]}, "g": {"SA": {"T0": [1, 2]}}}
    b = {"x": {"z": [3]}, "g": {"__replace__": True, "LLS": {"k": [1]}}}
    m = deep_merge(a, b)
    assert m == {"x": {"y": 1, "z": [3]}, "g": {"LLS": {"k": [1]}}}
    g = expand_grid({"id": "SA", "class": "SA"}, {"L": [1, 2], "T0": [5]})
    assert [s["id"] for s in g] == ["SA[L=1,T0=5]", "SA[L=2,T0=5]"]
    assert run_key("i", "SA[L=1]", 10, 0) != run_key("i", "SA[L=2]", 10, 0)


def test_units():
    rng = np.random.default_rng(1)
    inst = G.FAMILIES["omega"](10, 24, rng)
    assert np.allclose(inst.w * UNIT, inst.wu)


def test_budgets_respected(env):
    """Anytime methods (charged time included) stay within the budget on a medium instance."""
    inst = G.FAMILIES["staggered"](300, 96, np.random.default_rng(4))
    ctx = CX.make_context(inst, env, {"conf_time_limit": 10})
    specs = [{"class": "G", "params": {"mode": "budget"}}, {"class": "RR", "params": {"stop": "budget"}},
             {"class": "RLP", "params": {"stop": "budget"}}, {"class": "SA", "params": {"stop": "budget"}},
             {"class": "MT", "params": {"matrix": "lp", "mode": "budget"}}, {"class": "LLS"}, {"class": "WLNS"},
             {"class": "CRI"}, {"class": "CRI", "params": {"complete": True}},
             {"class": "SA", "params": {"stop": "budget", "init": "CRI", "init_spec": {"class": "CRI", "params": {"improve": []}}}},
             {"class": "GUROBI", "params": {"model": "standard"}}, {"class": "GUROBI", "params": {"model": "aggregated"}}]
    for budget in (1.0, 3.0):
        for sp in specs:
            r = make_method(sp).run(inst, ctx, budget, 0)
            assert r["time"] <= 1.2 * budget + 0.5, (sp, budget, r["time"])
            assert inst.is_feasible(r["solution"])


def test_nfdh_common_window_levels():
    """On a common window NFDH is Ranjan et al.'s NFDH_Preemptive: levels are filled left to right, and the
    peak never exceeds the sum of the level heights."""
    from cri.problems.ppmsp.sota import nfdh_kernel
    from cri.problems.ppmsp.instance import Instance
    inst = Instance(np.zeros(4, int), np.full(4, 9), np.array([6, 6, 5, 3]), np.array([22.0, 11.0, 11.0, 7.2]), 10)
    order = np.lexsort((-inst.p, -inst.wu)).astype(np.int64)
    x, levels = nfdh_kernel(inst.s, inst.e, inst.p, order, inst.T)
    assert inst.is_feasible(x) and levels == 2
    # level 1: job 0 on [0,6), job 1 on [6,10) then its rest [0,2) on level 2; job 2 on [2,7); job 3 on [7,10)
    assert x[0, :6].all() and x[1, 6:].all() and x[1, :2].all() and x[2, 2:7].all() and x[3, 7:].all()


def test_hunsaker_alpha_table():
    """alpha_T of Hunsaker et al. (2003), Table 4.1."""
    from cri.problems.ppmsp.sota import hunsaker_alpha
    for T, ref in ((2, 4 / 3), (3, 1.5), (10, 1.93576), (50, 2.26470), (100, 2.35061)):
        assert abs(hunsaker_alpha(T) - ref) < 1e-4, (T, hunsaker_alpha(T))


def test_afshar_bb_exact_on_tiny(env):
    """Run to completion, the branch and bound returns a proven optimum."""
    rng = np.random.default_rng(31)
    for f in ("omega", "staggered", "overnight", "single"):
        inst = G.FAMILIES[f](6, 8, rng)
        opt = EX.solve_standard(inst, env, 60.0)
        r = make_method({"class": "AFSHAR_BB"}).run(inst, None, 60.0, 0)
        assert r["info"]["complete_search"] and abs(r["objective"] - opt["peak"]) < 1e-6, (f, r["objective"], opt["peak"])


def test_worker_rule():
    """Automatic number of workers from cores, threads per task and free memory."""
    from cri.core.resources import plan_workers
    run = {"workers": "auto", "reserve_cores": 1, "reserve_mem_gb": 1.0, "mem_gb_per_worker": 1.0}
    laptop = {"logical_cores": 8, "physical_cores": 4, "mem_total_gb": 7.9, "mem_available_gb": 5.0}
    vm = {"logical_cores": 32, "physical_cores": 32, "mem_total_gb": 128, "mem_available_gb": 120}
    assert plan_workers(run, {}, 1, laptop)[0] == 3                                   # cores bound
    assert plan_workers(run, {"mem_gb_per_worker": 2.0}, 1, laptop)[0] == 2           # memory bound
    assert plan_workers(run, {}, 4, laptop)[0] == 1                                   # 4-thread Gurobi
    assert plan_workers(run, {}, 1, vm)[0] == 31
    assert plan_workers(run, {"mem_gb_per_worker": 8.0}, 1, vm)[0] == 14              # E6 on a big VM
    assert plan_workers(run, {}, 4, vm)[0] == 7
    assert plan_workers(dict(run, max_workers=8), {}, 1, vm)[0] == 8
    assert plan_workers(dict(run, workers=5), {}, 1, vm)[0] == 5                      # fixed
    assert plan_workers(run, {"workers": 2}, 1, vm)[0] == 2                           # block override


def test_cri_time_limited_certify(env):
    """CRI stays within its budget on a large instance whose cover-cut bound alone costs seconds, and its
    charged time includes the Certify steps it used or abandoned."""
    inst = G.FAMILIES["overnight"](500, 96, np.random.default_rng(8))
    ctx = CX.make_context(inst, env, {"conf_time_limit": 20})
    for budget in (1.0, 10.0):
        r = make_method({"class": "CRI"}).run(inst, ctx, budget, 0)
        assert inst.is_feasible(r["solution"])
        assert r["time"] <= 1.2 * budget + 0.5, (budget, r["time"], r["info"])
        assert r["info"]["certify_time"] <= 0.5 * budget + 1e-9
        assert r["lower_bound"] <= r["objective"] + 1e-9


def test_cri_keeps_ir_after_deadline(env):
    """Proposition 5.1(d): once iterative rounding has completed in Certify, its schedule counts in the
    Round stage even if an earlier rounding used the whole budget, so P(X) <= P_LP + w_max."""
    inst = G.FAMILIES["staggered"](40, 24, np.random.default_rng(9))
    ctx = CX.make_context(inst, env, {"conf_time_limit": 10})
    p_lp, _ = ctx.get("lp")
    spec = {"class": "CRI", "params": {"round": [{"class": "SA", "params": {"stop": "budget"}}, {"class": "IR"}],
                                       "improve": []}}
    # budget 2 s: the Certify steps (about 0.2 s here) fit in their share even when the tests run in parallel,
    # and the SA rounding uses the rest of the budget, so IR's schedule is taken after the deadline
    r = make_method(spec).run(inst, ctx, 2.0, 0)
    assert r["info"]["used_ir"], r["info"]
    assert r["guarantee"] <= p_lp + inst.w_max + 1e-6 and r["objective"] <= r["guarantee"] + 1e-9


def test_exact_deadline_and_runtime(env):
    """The exact models: the runtime includes the read-out of the schedule; with a passed deadline the model is
    not built (CRI's completion stage); improve_on skips the read-out when the solver did not improve on it."""
    import time
    inst = G.FAMILIES["staggered"](400, 48, np.random.default_rng(12))
    for f in (EX.solve_standard, EX.solve_aggregated):
        r = f(inst, env, 30.0, deadline=time.time() - 1.0)
        assert r["status"] == "BUILD_TIME_LIMIT" and r["x"] is None and r["runtime"] < 5.0
        t = time.time()
        r = f(inst, env, 1.0)
        wall = time.time() - t
        assert r["x"] is not None and inst.is_feasible(r["x"])
        assert wall - 0.05 <= r["runtime"] <= wall, (f.__name__, r["runtime"], wall)
        r2 = f(inst, env, 1.0, improve_on=0.0)                 # nothing can be below 0: no read-out
        assert r2["x"] is None and r2["peak"] == r2["peak"]


def test_cri_complete_within_budget(env):
    """CRI+C at 1 s on n = 1000 (an earlier version took up to 2.5 s there, because the completion model was
    built after the deadline): it stays within its budget and keeps a feasible schedule."""
    inst = G.FAMILIES["overnight"](1000, 96, np.random.default_rng(1000))
    ctx = CX.make_context(inst, env, {"conf_time_limit": 20})
    make_method({"class": "CRI"}).run(inst, ctx, 1.0, 0)          # artifacts cached, as in the runner
    r = make_method({"class": "CRI", "params": {"complete": True}}).run(inst, ctx, 1.0, 0)
    assert inst.is_feasible(r["solution"]) and not r["objective"] > r["guarantee"] + 1e-9   # NaN: no certificate
    assert r["time"] <= 1.2 * 1.0 + 0.3, (r["time"], r["info"])
