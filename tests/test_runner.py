"""
Runner behaviour that a long campaign relies on: waiting for the solver licence (a Gurobi WLS licence
needs the network) instead of skipping the remaining blocks, and stopping cleanly when it does not come back.

    pytest tests/test_runner.py
"""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from cri.core.config import load_config  # noqa: E402
from cri.core.runner import Runner, SolverUnavailable  # noqa: E402


class _FlakyEnv:
    """make_env fails `fails` times (as during a network cut), then starts."""

    def __init__(self, fails):
        self.fails, self.calls = fails, 0

    def make_env(self, cfg):
        self.calls += 1
        if self.calls <= self.fails:
            raise RuntimeError("Could not resolve host: token.gurobi.com")
        return None


def _runner(tmp_path, wait_min):
    cfg = load_config(os.path.join(ROOT, "config_quick.yaml"),
                      {"run": {"output": str(tmp_path / "results"), "cache": str(tmp_path / "cache"),
                               "licence_wait_min": wait_min, "licence_poll_s": 0.01}})
    lines = []
    r = Runner(cfg, log=lines.append)
    return r, lines


def test_waits_for_the_licence(tmp_path):
    r, lines = _runner(tmp_path, wait_min=1.0)
    r.problem = _FlakyEnv(fails=3)
    assert r.check_solver("E4a") is True                     # waited, then the licence came back
    assert r.problem.calls == 4
    assert any("unavailable" in m for m in lines) and any("available again" in m for m in lines)
    r.problem = _FlakyEnv(fails=0)
    assert r.check_solver("E4b") is False                    # no wait when the licence is there


def test_audit_overrun_check():
    """The budget check of the audit with no overrun, expected single-shot overruns and unexpected ones
    (the case that crashed the first audit of the VM campaign)."""
    import pandas as pd
    from cri.analysis.audit import overrun_check
    base = dict(experiment="E10a_state_of_the_art", instance="i1", seed=0)
    r = pd.DataFrame([dict(base, method="CRI", info_class="CRI", budget=10.0, time=10.2),
                      dict(base, method="CE-cut-excess", info_class="CE", budget=1.0, time=3.0)])
    ok, detail = overrun_check(r)
    assert ok and "expected single-shot" in detail
    r2 = pd.concat([r, pd.DataFrame([dict(base, method="ZAIDI_ILS", info_class="ZAIDI_ILS", budget=10.0, time=13.0),
                                     dict(base, method="ZAIDI_ILS", info_class="ZAIDI_ILS", budget=10.0, time=11.6)])])
    ok, detail = overrun_check(r2)
    assert not ok and "E10a_state_of_the_art/ZAIDI_ILS: 2 runs, worst 1.30x budget" in detail, detail
    ok, detail = overrun_check(r.iloc[:1])
    assert ok and detail == ""
    # overruns documented in the configuration (report.documented_overruns) pass, and are reported as such
    ok, detail = overrun_check(r2, {"ZAIDI_ILS": "first step indivisible"})
    assert ok and "documented overruns: {'ZAIDI_ILS': 2}" in detail, detail
    ok, detail = overrun_check(r2, {"OTHER": "x"})
    assert not ok
    # with the anytime traces: an overrun whose result was reached by the budget gained nothing and passes;
    # one that improved after the budget (or had no schedule by then) does not
    r3 = pd.DataFrame([dict(base, method="CRI", info_class="CRI", budget=1.0, time=1.17, objective=10.0),
                       dict(base, method="LLS", info_class="LLS", budget=1.0, time=1.20, objective=9.0, seed=1),
                       dict(base, method="RLP-b", info_class="RLP", budget=1.0, time=2.9, objective=12.0, seed=2)])
    tr = {("E10a_state_of_the_art", "i1", "CRI", 1.0, 0): [(0.3, 11.0), (0.9, 10.0)],
          ("E10a_state_of_the_art", "i1", "LLS", 1.0, 1): [(0.2, 11.0), (1.18, 9.0)],   # after 1.1 x 1 + 0.05
          ("E10a_state_of_the_art", "i1", "RLP-b", 1, 2): [(2.9, 12.0)]}
    ok, detail = overrun_check(r3.iloc[:1], traces=tr)
    assert ok and "no gain after the budget: {'CRI': 1}" in detail, detail
    ok, detail = overrun_check(r3, traces=tr)
    assert not ok and "LLS: 1 runs" in detail and "RLP-b: 1 runs" in detail and "CRI: 1" not in detail.split("|")[0]
    ok, detail = overrun_check(r3, {"LLS": "x", "RLP-b": "y"}, traces=tr)
    assert ok, detail


def test_evaluate_at_budget():
    """A run that improved only after its budget + tolerance is credited with the incumbent it had then (and its
    trace is cut there); a run with no schedule by then, or one that found nothing later, is unchanged."""
    import pandas as pd
    from cri.analysis.audit import overrun_check
    from cri.analysis.metrics import evaluate_at_budget
    base = dict(experiment="E4a_equal_budgets", instance="i1", budget=1.0)
    r = pd.DataFrame([dict(base, method="CRI", info_class="CRI", seed=0, time=1.17, objective=10.0),
                      dict(base, method="RLP-b", info_class="RLP", seed=0, time=2.9, objective=12.0),
                      dict(base, method="LLS", info_class="LLS", seed=0, time=1.20, objective=9.5),
                      dict(base, method="G-b", info_class="G", seed=0, time=1.00, objective=13.0)])
    tr = {("E4a_equal_budgets", "i1", "CRI", 1.0, 0): [(0.5, 10.4), (1.17, 10.0)],
          ("E4a_equal_budgets", "i1", "RLP-b", 1.0, 0): [(2.9, 12.0)],
          ("E4a_equal_budgets", "i1", "LLS", 1.0, 0): [(0.3, 9.5)],
          ("E4a_equal_budgets", "i1", "G-b", 1.0, 0): [(0.2, 13.0), (1.0, 13.0)]}
    assert evaluate_at_budget(r, tr) == 1
    assert list(r.objective) == [10.4, 12.0, 9.5, 13.0] and list(r.objective_final) == [10.0, 12.0, 9.5, 13.0]
    assert list(r.evaluated_at_budget) == [True, False, False, False]
    assert tr[("E4a_equal_budgets", "i1", "CRI", 1.0, 0)] == [(0.5, 10.4)]
    assert evaluate_at_budget(r, tr) == 0 and list(r.objective) == [10.4, 12.0, 9.5, 13.0]      # idempotent
    ok, detail = overrun_check(r, traces=tr)                 # only RLP-b (no schedule by the budget) remains
    assert not ok and "RLP-b: 1 runs" in detail and "no gain after the budget: {'CRI': 1, 'LLS': 1}" in detail
    assert overrun_check(r, {"RLP-b": "its LP"}, traces=tr)[0]


def test_charge_wall_time():
    """The Gurobi runs of the 2026-10-23 campaign are charged their wall time (it includes the read-out of the
    schedule that the solver wrapper did not count); the other runs and later Gurobi runs are unchanged."""
    import numpy as np
    import pandas as pd
    from cri.analysis.metrics import charge_wall_time
    r = pd.DataFrame({"method": ["GUROBI-agg", "GUROBI-std", "CRI", "GUROBI-agg"],
                      "info_class": ["GUROBI", "GUROBI", "CRI", "GUROBI"],
                      "time": [1.04, 1.30, 1.00, 2.00], "own_time": [1.04, 1.30, 0.40, 2.00],
                      "info_wall": [1.94, 1.25, 1.60, np.nan]})
    out = charge_wall_time(r.copy())
    assert list(out.time) == [1.94, 1.30, 1.00, 2.00] and list(out.own_time) == [1.94, 1.30, 0.40, 2.00]
    assert charge_wall_time(out.copy()).equals(out)                      # idempotent
    assert charge_wall_time(None) is None
    assert charge_wall_time(r.drop(columns="info_wall")).equals(r.drop(columns="info_wall"))


def test_context_cache_per_campaign(tmp_path):
    """A fresh results folder gets its own, empty context cache (clean run from A to Z); the same folder finds
    it again (resume); a results folder of before 2026-10-24 keeps the shared cache folder."""
    r1, _ = _runner(tmp_path, wait_min=0.001)
    cid = r1.campaign_id
    assert cid and r1.cache_dir == os.path.join(str(tmp_path / "cache"), cid, "contexts")
    assert os.path.isdir(r1.cache_dir) and not os.listdir(r1.cache_dir)
    r2, _ = _runner(tmp_path, wait_min=0.001)
    assert r2.campaign_id == cid and r2.cache_dir == r1.cache_dir
    old = tmp_path / "old"
    (old / "results" / "01_raw_runs" / "E0_sanity").mkdir(parents=True)
    (old / "results" / "01_raw_runs" / "E0_sanity" / "job.pkl").write_bytes(b"")
    r3, _ = _runner(old, wait_min=0.001)
    assert r3.campaign_id == "" and r3.cache_dir == os.path.join(str(old / "cache"), "contexts")
    assert (old / "results" / "05_logs" / "campaign_id.txt").read_text(encoding="utf-8").strip() == ""


def test_environment_recorded(tmp_path):
    """Every start of `run` appends the machine and the software versions to 05_logs/environment.jsonl."""
    import json
    from cri.core.resources import describe_environment
    r, lines = _runner(tmp_path, wait_min=0.001)
    os.makedirs(tmp_path / "results" / "05_logs", exist_ok=True)
    env = r.record_environment()
    r.record_environment()
    rows = [json.loads(x) for x in (tmp_path / "results" / "05_logs" / "environment.jsonl").read_text(
        encoding="utf-8").splitlines()]
    assert len(rows) == 2 and rows[0]["campaign"] == r.campaign_id
    assert env["host"] and env["cpu"] and env["python"] and env["physical_cores"] >= 1
    assert any("environment: " + env["host"] in m for m in lines)
    assert describe_environment(rows[0]) == describe_environment(env)


def test_stops_cleanly_without_licence(tmp_path):
    r, lines = _runner(tmp_path, wait_min=0.001)
    r.problem = _FlakyEnv(fails=10 ** 9)
    with pytest.raises(SolverUnavailable):
        r.check_solver("E3")
    assert any("stopping" in m for m in lines)
