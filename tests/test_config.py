"""
Static consistency of the campaign configurations: every reference resolves before hours of computing.

    pytest tests/test_config.py
"""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import cri.problems.ppmsp  # noqa: E402,F401
from cri.core.config import load_config  # noqa: E402
from cri.core.registry import METHODS, make_method  # noqa: E402
from cri.core.runner import expand_grid, expand_sets, method_specs  # noqa: E402
from cri.problems.ppmsp.generators import FAMILIES  # noqa: E402


@pytest.mark.parametrize("name", ["config.yaml", "config_quick.yaml"])
def test_configuration_resolves(name):
    cfg = load_config(os.path.join(ROOT, name))
    lib = {m.get("id", m["class"]): m for m in cfg["methods"]}
    # library: classes exist, ids unique, tuned_as targets exist, every spec builds with its parameters
    ids = [m.get("id", m["class"]) for m in cfg["methods"]]
    assert len(ids) == len(set(ids)), "duplicate method ids"
    for m in cfg["methods"]:
        assert m["class"] in METHODS, m
        if "tuned_as" in m:
            assert m["tuned_as"] in lib, m
        make_method(m, defaults=cfg.get("defaults", {}))
        for k in ("init_spec",):
            if k in (m.get("params") or {}):
                assert (m["params"][k]["class"]) in METHODS
        for lst in ("round", "improve"):
            for sp in (m.get("params") or {}).get(lst, []) or []:
                assert sp["class"] in METHODS, (m["id"], sp)
    for k in cfg.get("defaults", {}):
        assert k in METHODS, f"defaults for unknown class {k}"
    # instance sets
    for s in expand_sets(cfg):
        assert s["family"] in FAMILIES, s
        assert int(s["n"]) >= 1 and int(s["T"]) >= 1 and int(s.get("count", 1)) >= 1
    set_names = {s["name"] for s in cfg["instance_sets"]}
    for s in cfg.get("references", {}).get("sets", []):
        assert s in set_names
    # blocks
    names = list(cfg["experiments"])
    for bname, ex in cfg["experiments"].items():
        for s in ex["sets"]:
            assert s in set_names, (bname, s)
        specs = method_specs(cfg, ex["methods"])                 # raises on unknown ids
        for b in ex.get("budgets", [None]):
            assert b is None or float(b) > 0, (bname, b)
        if ex.get("kind") == "tuning":
            for mid, grid in ex.get("grid", {}).items():
                assert mid in ex["methods"], (bname, mid)
                for g in expand_grid(lib[mid], grid):
                    make_method(g, defaults=cfg.get("defaults", {}))
            for mid, cls in (ex.get("apply_to_class") or {}).items():
                assert mid in ex["methods"] and cls in METHODS, (bname, mid, cls)
        for inc in ex.get("include", []):
            assert inc["experiment"] in names and names.index(inc["experiment"]) < names.index(bname), (bname, inc)
            src = cfg["experiments"][inc["experiment"]]
            for m in inc["methods"]:
                assert m in src["methods"], (bname, inc["experiment"], m)
            assert set(ex.get("budgets", [])) <= set(src.get("budgets", [])), (bname, "budgets not in the source block")
        for k in ("control",):
            if ex.get(k):
                pool = set(ex["methods"]) | {m for inc in ex.get("include", []) for m in inc["methods"]}
                assert ex[k] in pool, (bname, k, ex[k])
        for a, b_ in ex.get("pairs", []):
            assert a in ex["methods"] and b_ in ex["methods"], (bname, a, b_)
        for m in ex.get("figure_methods", []) or []:
            assert m in ex["methods"], (bname, m)
        for m in ex.get("baselines", []) or []:
            assert m in ex["methods"], (bname, m)
        assert all(s["class"] in METHODS for s in specs)
    # tuning blocks come before the blocks that use their results
    tun = [i for i, n in enumerate(names) if cfg["experiments"][n].get("kind") == "tuning"]
    uses = [i for i, n in enumerate(names) if cfg["experiments"][n].get("kind") != "tuning"
            and n not in ("E0_sanity", "E1_certificates")]
    assert not tun or max(tun) < min(uses)
