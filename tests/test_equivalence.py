"""
The framework's faster Certify code gives the same results as the verified implementation of the theory
(theory/, checked by verify_theory.py): LB_cut and its vertex alpha_cut, LB_conf, and the knapsack
pricing. Skipped if theory/ is missing.

    pytest tests/test_equivalence.py
"""

import os
import sys

import numpy as np
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAB = os.path.join(ROOT, "theory")
sys.path.insert(0, ROOT)

from cri.problems.ppmsp import certificates as C  # noqa: E402
from cri.problems.ppmsp import context as CX  # noqa: E402
from cri.problems.ppmsp import generators as G  # noqa: E402

pytestmark = pytest.mark.skipif(not os.path.isdir(LAB), reason="theory/ not available")


@pytest.fixture(scope="module")
def lab():
    sys.path.insert(0, LAB)
    import bounds as LB_
    import certificates as LC_
    return LB_, LC_


@pytest.fixture(scope="module")
def env():
    import gurobipy as gp
    e = gp.Env(empty=True); e.setParam("OutputFlag", 0); e.start()
    return e


def _lab_instance(LB_, inst):
    n = inst.n
    return LB_.Instance((np.ones(n, int), inst.s + 1, inst.e + 1, inst.p, inst.w, n, 1, inst.T, 0.0))


def test_knapsack_same_as_reference():
    rng = np.random.default_rng(0)
    for _ in range(300):
        m = int(rng.integers(1, 25))
        v = rng.normal(size=m)
        w = rng.integers(1, 60, size=m)
        cap = int(rng.integers(1, 300))
        a = C._knapsack(v, w, cap)
        b = C._knapsack_py(v, w, cap)
        assert abs(a[0] - b[0]) < 1e-12 and sorted(a[1]) == sorted(b[1])


def test_cut_and_conf_bounds_same_as_verified(lab, env):
    LB_, LC_ = lab
    rng = np.random.default_rng(42)
    for fam, n, T in (("omega", 20, 24), ("staggered", 40, 48), ("overnight", 15, 24), ("omega", 60, 48)):
        inst = G.FAMILIES[fam](n, T, rng)
        ctx = CX.make_context(inst, env, {"conf_time_limit": 600})
        lbc, alpha_c, q = ctx.get("lb_cut")
        lbf, alpha_f, ok = ctx.get("lb_conf")
        li = _lab_instance(LB_, inst)
        p_lp, a = LB_.solve_lp(li, env)
        cert = LC_.Certificates(li, a, p_lp)
        ub = cert.round_down_ub(p_lp + li.w.max())
        lbc2, alpha_c2, q2 = LC_.cut_lower_bound(cert, ub, env, 8)
        assert abs(lbc - lbc2) < 1e-9, (fam, lbc, lbc2)
        assert np.allclose(alpha_c, alpha_c2, atol=1e-7), fam          # same final vertex
        lbf2, _ = LC_.config_lower_bound(cert, lbc2, ub, env)
        assert ok and abs(lbf - lbf2) < 1e-9, (fam, lbf, lbf2)
