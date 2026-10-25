"""
Invariants of the incremental Numba kernels: after every chunk the working loads equal the loads of the
working schedule, the segment tree holds them, every schedule stays feasible and the best kept is the
best seen. Chunks are chained as the methods chain them.

    pytest tests/test_invariants.py        (under a minute)
"""

import os
import sys

import numpy as np
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import cri.problems.ppmsp  # noqa: E402,F401
from cri.problems.ppmsp import context as CX  # noqa: E402
from cri.problems.ppmsp import generators as G  # noqa: E402
from cri.problems.ppmsp import kernels as K  # noqa: E402
from cri.problems.ppmsp.instance import UNIT  # noqa: E402
from cri.problems.ppmsp.methods import _matrix, _mt_arrays, units_floor  # noqa: E402


@pytest.fixture(scope="module")
def instances():
    rng = np.random.default_rng(5)
    return [G.FAMILIES[f](n, T, rng) for f, n, T in (("omega", 30, 24), ("staggered", 40, 32), ("overnight", 25, 24),
                                                     ("pcmax", 12, 4), ("single", 30, 24), ("omega", 8, 6))]


@pytest.fixture(scope="module")
def env():
    import gurobipy as gp
    e = gp.Env(empty=True); e.setParam("OutputFlag", 0); e.start()
    return e


def _tree_ok(tree, size, L):
    return np.array_equal(tree[size:size + len(L)], L) and tree[1] == L.max()


@pytest.mark.parametrize("eps", [0.0, 0.05])
def test_sa_chunks(instances, eps):
    for inst in instances:
        K.seed_numba(1)
        x = K.random_schedule(inst.s, inst.e, inst.p, inst.T)
        L = K.loads_of(x, inst.wu)
        tree, size = K.seg_build(L)
        sq = K.sum_sq(L) / UNIT ** 2
        state = np.array([50.0, L.max() / UNIT + eps * sq, 0, 0, L.max(), sq], float)
        best_x, best_L = x.copy(), L.copy()
        rec_it = np.zeros(4096, np.int64); rec_val = np.zeros(4096, np.int64)
        seen = L.max()
        for _ in range(8):
            prm = np.array([0.01, 0.95, 50, 10 ** 9, 0.3, eps, 700], float)
            nrec = K.sa_chunk(x, L, tree, size, inst.s, inst.e, inst.p, inst.wu, float(UNIT), state, prm,
                              best_x, best_L, rec_it, rec_val, -1)
            assert inst.is_feasible(x) and inst.is_feasible(best_x), inst.name
            assert np.array_equal(L, inst.loads(x)), inst.name
            assert _tree_ok(tree, size, L), inst.name
            assert np.array_equal(best_L, inst.loads(best_x)) and state[4] == best_L.max(), inst.name
            assert abs(state[5] - K.sum_sq(best_L) / UNIT ** 2) < 1e-6 * max(1.0, state[5]), inst.name
            seen = min(seen, L.max())
            assert state[4] <= seen
            assert all(rec_val[k] >= state[4] for k in range(nrec))
            # the objective of the current schedule is the one SA believes it has
            assert abs(state[1] - (L.max() / UNIT + eps * K.sum_sq(L) / UNIT ** 2)) < 1e-6 * max(1.0, state[1])


def test_rr_chunks(instances):
    for inst in instances:
        K.seed_numba(2)
        x = K.random_schedule(inst.s, inst.e, inst.p, inst.T)
        L = K.loads_of(x, inst.wu)
        best_x = x.copy(); best = np.array([L.max()], np.int64)
        rec_it = np.zeros(4096, np.int64); rec_val = np.zeros(4096, np.int64)
        for c in range(6):
            K.rr_chunk(x, L, inst.s, inst.e, inst.p, inst.wu, 300, best_x, best, rec_it, rec_val, c * 300)
            assert inst.is_feasible(x) and inst.is_feasible(best_x), inst.name
            assert np.array_equal(L, inst.loads(x)), inst.name
            assert best[0] == inst.loads(best_x).max() and best[0] <= L.max(), inst.name


def test_lls_chunks(instances):
    for inst in instances:
        K.seed_numba(3)
        x, L = K.greedy_vf(inst.s, inst.e, inst.p, inst.wu, inst.T, 3)
        x = x.astype(np.int8)
        K.lls_local(x, L, inst.s, inst.e, inst.wu, 200000)
        assert inst.is_feasible(x) and np.array_equal(L, inst.loads(x)), inst.name
        # local optimum: no single unit move lowers a slot without reaching its load
        for i in range(inst.n):
            on = [t for t in inst.win[i] if x[i, t]]; off = [t for t in inst.win[i] if not x[i, t]]
            if on and off:
                assert min(L[off]) + inst.wu[i] >= max(L[on]), (inst.name, i)
        rec_it = np.zeros(4096, np.int64); rec_val = np.zeros(4096, np.int64)
        prev = L.max()
        for c in range(4):
            K.lls_iterate(x, L, inst.s, inst.e, inst.wu, 20, 3, 200000, -1, rec_it, rec_val, c * 20)
            assert inst.is_feasible(x) and np.array_equal(L, inst.loads(x)), inst.name
            assert L.max() <= prev, inst.name                  # lexicographic acceptance never worsens the peak
            prev = L.max()


def test_mt_and_rlp(instances, env):
    for inst in instances:
        ctx = CX.make_context(inst, env, {"conf_time_limit": 10})
        _, alpha = ctx.get("lp")
        K.seed_numba(4)
        for _ in range(20):
            x, L = K.rlp_trial(alpha, inst.s, inst.e, inst.p, inst.wu, float(UNIT))
            assert inst.is_feasible(x) and np.array_equal(L, inst.loads(x)), inst.name
        for which in ("lp", "cut"):
            cert, _ = _matrix(ctx, which)
            arrs = _mt_arrays(inst, cert)
            assert np.array_equal(arrs["L0"], inst.loads(arrs["x0"]))
            u = int(round(units_floor(cert.lll()) * UNIT))
            for r in range(5):
                K.seed_numba(100 + r)
                x, L, steps, ok = K.mt_run(arrs["x0"], arrs["L0"], inst.wu, arrs["fr_ptr"], arrs["fr_slot"],
                                           arrs["fr_cum"], arrs["fr_r"], arrs["veh_of"], arrs["slot_ptr"],
                                           arrs["slot_veh"], u, 10 ** 6)
                assert inst.is_feasible(x) and np.array_equal(L, inst.loads(x)), (inst.name, which)
                assert ok and L.max() <= u, (inst.name, which, L.max(), u)
                # vehicles with an integral row are never moved
                integ = [i for i in range(inst.n) if i not in cert.frac_slots]
                assert np.array_equal(x[integ], arrs["x0"][integ]), (inst.name, which)
