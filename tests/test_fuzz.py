"""
Fuzz test: every method on degenerate and random tiny instances, against exact optima.

Edge cases run without a target; random instances run with the certified lower bound as stopping target
(the early-stop path). Invariants checked for every run that returns a schedule:
  feasible schedule; reported peak = true peak; peak >= OPT; guarantee >= peak; reported lower bound
  <= OPT. For every instance: certified LB <= OPT <= every upper certificate.

    pytest tests/test_fuzz.py            (about 2 minutes)
"""

import os
import sys

import numpy as np
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import cri.problems.ppmsp  # noqa: E402,F401
from cri.core.registry import make_method  # noqa: E402
from cri.problems.ppmsp import context as CX  # noqa: E402
from cri.problems.ppmsp import exact as EX  # noqa: E402
from cri.problems.ppmsp import generators as G  # noqa: E402
from cri.problems.ppmsp.context import _is_upper  # noqa: E402
from cri.problems.ppmsp.instance import Instance  # noqa: E402

TOL = 1e-6

SPECS = (
    [{"class": "G"}, {"class": "G", "params": {"mode": "budget"}}, {"class": "RR", "params": {"N": 200}},
     {"class": "RR", "params": {"stop": "budget"}}, {"class": "RLP", "params": {"trials": 5}},
     {"class": "RLP", "params": {"stop": "budget"}}, {"class": "SA", "params": {"N": 500}},
     {"class": "SA", "params": {"stop": "budget"}}, {"class": "SA", "params": {"init": "G", "N": 300}},
     {"class": "SA", "params": {"init": "RR", "init_spec": {"class": "RR", "params": {"N": 100}}, "N": 300}},
     {"class": "SA", "params": {"init": "RLP", "init_spec": {"class": "RLP", "params": {"trials": 2}}, "N": 300}},
     {"class": "SA", "params": {"stop": "budget", "init": "CRI", "init_spec": {"class": "CRI", "params": {"improve": []}}}}]
    + [{"class": "CE", "params": {"matrix": m, "estimator": e}} for m in ("lp", "cut", "conf")
       for e in ("excess", "union", "component")]
    + [{"class": "IR"}] + [{"class": "MT", "params": {"matrix": m}} for m in ("lp", "cut", "conf")]
    + [{"class": "MT", "params": {"matrix": "lp", "mode": "budget"}}, {"class": "LLS"}, {"class": "WLNS"},
       {"class": "CRI"}, {"class": "CRI", "params": {"complete": True}}, {"class": "CRI", "params": {"improve": []}},
       {"class": "CRI", "params": {"round": [{"class": "IR"}]}},
       {"class": "CRI", "params": {"certify": {"conf": False}, "improve": [{"class": "SA", "params": {"stop": "budget"}}]}},
       {"class": "GUROBI", "params": {"model": "standard"}}, {"class": "GUROBI", "params": {"model": "aggregated"}},
       {"class": "ASAP"}, {"class": "GNP"}, {"class": "BK"}, {"class": "NFDH"}, {"class": "ZAIDI_H"},
       {"class": "ZAIDI_ILS", "params": {"max_trials": 50}}, {"class": "ZAIDI_ILS", "params": {"restart": True}},
       {"class": "HUNSAKER"}, {"class": "AFSHAR_BB"}]
    + [{"class": "AN_HYBRID", "params": {"variant": v, "ls": ls, "pop": 8, "maxgen": 10}}
       for v in ("SER", "PAR", "DE", "GA", "PSO") for ls in ("LS1", "LS2")]
    + [{"class": "AN_HYBRID", "params": {"objective": "dev", "pop": 8, "maxgen": 10}}]
)


def edge_instances():
    rng = np.random.default_rng(2026)
    out = [
        Instance([0, 0, 0], [0, 0, 0], [1, 1, 1], [7.2, 3.3, 22.0], 1, name="single_slot"),
        Instance([1], [4], [3], [11.5], 6, name="single_vehicle"),
        Instance([0, 2, 1, 5], [1, 4, 5, 6], [2, 3, 5, 2], [7.2, 9.6, 3.3, 22.0], 7, name="no_flexibility"),
        Instance([0, 0, 0, 0, 0, 0], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [3.3, 6.2, 7.2, 9.6, 11.5, 22.0], 4,
                 name="all_forced_common"),
        Instance([0, 0, 0, 0, 0, 0], [3, 3, 3, 3, 3, 3], [1, 2, 3, 1, 2, 3], [7.2] * 6, 4, name="one_power_common"),
        Instance([0, 0, 1, 1, 2], [4, 4, 4, 3, 4], [1, 1, 2, 1, 3], [3.3, 22.0, 3.3, 22.0, 3.3], 5, name="extreme_powers"),
        Instance([0, 5], [4, 9], [2, 2], [7.2, 7.2], 10, name="disjoint_windows"),
        Instance([0, 0, 0], [2, 2, 2], [3, 1, 1], [22.0, 22.0, 22.0], 3, name="ties_everywhere"),
    ]
    for fam, n, T in (("omega", 6, 8), ("staggered", 8, 10), ("overnight", 5, 8), ("pcmax", 6, 3), ("single", 6, 8),
                      ("staggered", 10, 12), ("omega", 9, 12)):
        inst = G.FAMILIES[fam](n, T, rng)
        inst.name = f"{fam}_{n}_{T}"
        out.append(inst)
    return out


def random_instances(k=12, seed=7):
    """Arbitrary tiny instances (no family structure): n in 1..8, T in 1..10, mixed powers."""
    rng = np.random.default_rng(seed)
    out = []
    for j in range(k):
        n, T = int(rng.integers(1, 9)), int(rng.integers(1, 11))
        s = rng.integers(0, T, n)
        e = np.array([rng.integers(si, T) for si in s])
        p = np.array([rng.integers(1, ei - si + 2) for si, ei in zip(s, e)])
        w = rng.choice([3.3, 7.2, 11.5, 22.0, round(float(rng.uniform(0.1, 30.0)), 1)], n)
        out.append(Instance(s, e, p, w, T, name=f"random_{j}_n{n}_T{T}"))
    return out


@pytest.fixture(scope="module")
def env():
    import gurobipy as gp
    e = gp.Env(empty=True); e.setParam("OutputFlag", 0); e.start()
    return e


CASES = [(i, False) for i in edge_instances()] + [(i, True) for i in random_instances()]


@pytest.mark.parametrize("inst,stop_at_lb", CASES, ids=lambda c: c.name if hasattr(c, "name") else ("lb" if c else ""))
def test_all_methods_on_instance(inst, stop_at_lb, env):
    opt = EX.solve_standard(inst, env, 60.0)
    assert opt["proven"], inst.name
    P = opt["peak"]
    ctx = CX.make_context(inst, env, {"conf_time_limit": 10})
    assert ctx.get("lb") <= P + TOL, (inst.name, "certified LB above OPT")
    b = ctx.get("bounds")
    for k, v in b.items():
        if _is_upper(k) and v == v:
            assert v >= P - TOL, (inst.name, k, v, P)
    assert b["LB"] <= P + TOL and b["U_best"] >= P - TOL
    problems = []
    for sp in SPECS:
        try:
            r = make_method(sp).run(inst, ctx, 0.3, 1, ctx.get("lb") if stop_at_lb else None)
        except Exception as ex:                                    # every method must survive every instance
            problems.append((sp, f"exception {ex!r}"))
            continue
        if r.get("status") == "not_available":
            continue
        x = r.get("solution")
        if x is None:
            problems.append((sp, "no schedule")); continue
        if not inst.is_feasible(x):
            problems.append((sp, "infeasible")); continue
        pk = inst.peak(x)
        if abs(pk - r["objective"]) > TOL:
            problems.append((sp, f"reported {r['objective']} true {pk}"))
        if pk < P - TOL:
            problems.append((sp, f"peak {pk} below the proven optimum {P}"))
        g = r.get("guarantee", np.nan)
        if g == g and pk > g + TOL:
            problems.append((sp, f"guarantee {g} violated by {pk}"))
        lb = r.get("lower_bound", np.nan)
        if lb == lb and lb > P + TOL:
            problems.append((sp, f"lower bound {lb} above the optimum {P}"))
    assert not problems, (inst.name, problems)
