"""
Smoke test before a long campaign: every method used by the remaining blocks of config.yaml, with the
configured and tuned parameters, on large instances of the campaign itself (fresh contexts), at a short
budget. Checks that nothing crashes, that every schedule is feasible and that the charged time respects
the budget. The instances run in parallel processes (one per core); the methods of an instance run one
after the other, so that each run has its core.

    python -m tests.smoke_large [config.yaml] [--budget 5] [--instances large_omega_n2000_T96_000,...]
"""

import argparse
import json
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from cri.core.config import deep_merge, load_config  # noqa: E402
from cri.core.registry import PROBLEMS, make_method, set_defaults  # noqa: E402
from cri.core.results import ResultStore  # noqa: E402
from cri.core.resources import plan_workers, single_thread_env  # noqa: E402
from cri.core.runner import _apply_tuned, build_instances, method_specs, resolve_path  # noqa: E402
import cri.problems.ppmsp  # noqa: E402,F401


def _setup(config_path, blocks):
    """Configuration, tuned defaults and method specs of the remaining blocks (in the master and in each worker)."""
    cfg = load_config(config_path)
    out = resolve_path(cfg, cfg["run"].get("output", "results"))
    tuned = {}
    p = os.path.join(ResultStore(out).data_root, "tuned_defaults.json")
    if os.path.exists(p):
        tuned = json.load(open(p, encoding="utf-8"))
    set_defaults(deep_merge(cfg.get("defaults", {}), tuned.get("classes", {})))
    ids = []
    for b in blocks.split(","):
        for m in cfg["experiments"][b]["methods"]:
            if m not in ids:
                ids.append(m)
    specs = [_apply_tuned(s, tuned.get("ids", {})) for s in method_specs(cfg, ids)]
    return cfg, out, specs


def smoke_instance(config_path, blocks, name, budget):
    """Every method on one instance (fresh context), sequentially: returns (lines, runs to check)."""
    cfg, out, specs = _setup(config_path, blocks)
    problem = PROBLEMS["ppmsp"]
    env = problem.make_env(cfg["run"])
    problem.warmup(env)
    sets = build_instances(cfg, problem, ResultStore(out), lambda m: None)
    inst = {i.name: i for v in sets.values() for i in v}[name]
    ctx = problem.make_context(inst, env, cfg.get("context", {}))
    lines, bad = [f"\n== {name}  (n={inst.n}, T={inst.T}), budget {budget:g} s, {len(specs)} methods"], 0
    for sp in specs:
        t0 = time.time()
        try:
            r = make_method(sp).run(inst, ctx, budget, 0, None)
            wall = time.time() - t0
            st = r.get("status", "ok")
            x = r.get("solution")
            feas = inst.is_feasible(x) if x is not None else None
            over = r.get("time", 0) > 1.2 * budget + 1.0
            flag = "" if (feas in (True, None) and not over and st in ("ok", "not_available")) else "  <-- CHECK"
            bad += bool(flag)
            lines.append(f"  {sp['id']:16s} peak {r.get('objective', np.nan):9.1f}  charged {r.get('time', np.nan):6.1f} s  "
                         f"wall {wall:6.1f} s  feasible {feas}  status {st}{flag}")
        except Exception as ex:
            bad += 1
            lines.append(f"  {sp['id']:16s} EXCEPTION {ex!r}  <-- CHECK")
    lines.append("  context costs: " + ", ".join(f"{k} {v:.1f}s" for k, v in ctx._own.items()))
    return lines, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config", nargs="?", default=os.path.join(ROOT, "config.yaml"))
    ap.add_argument("--budget", type=float, default=5.0)
    ap.add_argument("--instances", default="large_omega_n2000_T96_000,large_overnight_n1000_T96_000")
    ap.add_argument("--blocks", default="E4a_equal_budgets,E4b_equal_budgets_60s,E3_long_runs,E3x_long_runs_xlarge,E5_ablation,"
                    "E6_scalability,E7_gurobi_threads,E9_managerial,E10a_state_of_the_art")
    ap.add_argument("--workers", type=int, default=0, help="instances in parallel (default: automatic, as the runner)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    names = a.instances.split(",")
    cfg, out, specs = _setup(a.config, a.blocks)
    problem = PROBLEMS["ppmsp"]
    build_instances(cfg, problem, ResultStore(out), lambda m: None)   # data/instances.pkl exists before the workers
    if a.workers:
        workers, why = a.workers, "fixed"
    else:
        workers, why = plan_workers(cfg["run"], {"mem_gb_per_worker": 2.0}, 1)
    workers = max(1, min(workers, len(names)))
    print(f"smoke test: {len(names)} instances x {len(specs)} methods at {a.budget:g} s, {workers} worker(s) ({why})",
          flush=True)
    if workers > 1:                                 # one instance per process, each on its own core
        import multiprocessing as mp
        from concurrent.futures import ProcessPoolExecutor
        single_thread_env()
        with ProcessPoolExecutor(max_workers=workers, mp_context=mp.get_context("spawn")) as ex:
            results = list(ex.map(smoke_instance, [a.config] * len(names), [a.blocks] * len(names), names,
                                  [a.budget] * len(names)))
    else:
        results = [smoke_instance(a.config, a.blocks, nm, a.budget) for nm in names]
    bad = 0
    for lines, b in results:
        print("\n".join(lines), flush=True)
        bad += b
    print(f"\n{bad} method runs to check")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
