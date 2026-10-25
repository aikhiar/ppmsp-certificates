"""
Verification protocol of the framework: one round = every check below, in order; a scorecard is printed
and written to <work>/verification_protocol.md; exit code 1 if any check fails. Run it after every change
(verify, rectify, run again until every check passes).

  P1  static        every module compiles; pyflakes reports no error (unused imports aside)
  P2  tests         the whole test suite (pytest, in parallel when pytest-xdist is installed)
  P3  campaign      a fresh quick campaign through the real command line (python -m cri all config_quick.yaml),
                    new output folder and empty context cache
  P4  audit         python -m cri audit on it: runs complete and valid, folder layout, the outputs every analysis
                    must produce, files, links, index, LaTeX labels, path lengths, statistics sanity
  P5  resume        a second `run` finds nothing to do in any block
  P6  rebuild       `report` rebuilt from the raw pkl files gives the same tables as `all`
  P6b rerun         `forget` of one method in one block, then `run`: exactly those runs are recomputed (the
                    other blocks and methods are kept), and the rebuilt report passes the audit
  P7  smoke         the smoke test (parallel, two medium instances, 1 s)
  P8  launcher      run_all.bat control flow with a stand-in interpreter (Windows): fresh machine, second run,
                    a failing verification step, a stopped campaign, a failing audit; `run_all.bat tiny`
                    passes the tiny settings and its own results folder to every step
  P9  theory        (--heavy) the quick theory verification in parallel, 0 failures
  P10 clean         no results folder created inside the code folders

    python tools/verify_protocol.py [--workers 2] [--heavy] [--keep] [--work DIR]
"""

import argparse
import datetime as dt
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAB = os.path.join(ROOT, "theory")
PY = sys.executable
ROWS = []


def record(phase, check, ok, detail="", seconds=None):
    ROWS.append({"phase": phase, "check": check, "ok": bool(ok), "detail": str(detail)[:300],
                 "seconds": seconds})
    print(f"[{'PASS' if ok else 'FAIL'}] {phase:9s} {check}" + (f"  -- {detail}" if detail else "")
          + (f"  ({seconds:.0f} s)" if seconds is not None else ""), flush=True)
    return ok


LOGDIR = None


def sh(args, cwd=ROOT, env=None, timeout=7200, log=None):
    t0 = time.time()
    e = dict(os.environ)
    e.update(env or {})
    p = subprocess.run(args, cwd=cwd, env=e, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       timeout=timeout)
    out = p.stdout + p.stderr
    if log and LOGDIR:
        with open(os.path.join(LOGDIR, log + ".txt"), "w", encoding="utf-8") as f:
            f.write(out)
    return p.returncode, out, time.time() - t0


def p1_static():
    code, out, t = sh([PY, "-m", "compileall", "-q", "cri", "tests", "tools", LAB])
    record("P1", "every module compiles", code == 0, out.strip()[-200:], t)
    code, out, t = sh([PY, "-m", "pyflakes", "cri", "tests", "tools", LAB])
    errs = [ln for ln in out.splitlines() if ln.strip() and "imported but unused" not in ln
            and "reference_old" not in ln and "is assigned to but never used" not in ln]
    record("P1", "pyflakes: no error", not errs, "; ".join(errs[:3]), t)


def p2_tests():
    xd = ["-n", "auto"] if sh([PY, "-c", "import xdist"])[0] == 0 else []
    code, out, t = sh([PY, "-m", "pytest", "-q", "-rf", *xd, "tests"], log="P2_tests")
    m = re.findall(r"(\d+) passed", out)
    f = re.findall(r"(\d+) failed", out)
    names = re.findall(r"FAILED (\S+)", out)
    record("P2", f"test suite ({'parallel' if xd else 'serial'})", code == 0 and not f,
           f"{m[-1] if m else 0} passed, {f[-1] if f else 0} failed" + (f": {names[:3]}" if names else ""), t)


def cli(cmd, work, workers, extra=()):
    args = [PY, "-u", "-m", "cri", cmd, "config_quick.yaml", "--output", os.path.join(work, "results"),
            "--cache", os.path.join(work, "cache"), *extra]
    if workers and cmd in ("all", "run"):
        args += ["--workers", str(workers)]
    return sh(args, log=f"{cmd}_{len(os.listdir(LOGDIR)) if LOGDIR else 0}")


def p3_campaign(work, workers):
    code, out, t = cli("all", work, workers)
    errs = [ln for ln in out.splitlines() if "worker error" in ln or "Traceback" in ln]
    record("P3", "fresh quick campaign (python -m cri all)", code == 0 and not errs,
           errs[0][:200] if errs else f"exit {code}", t)
    open(os.path.join(work, "campaign_output.txt"), "w", encoding="utf-8").write(out)


def p4_audit(work, phase="P4", label="audit of the campaign output"):
    code, out, t = cli("audit", work, None)
    fails = [ln for ln in out.splitlines() if ln.startswith("[FAIL]")]
    summary = re.findall(r"audit: (\d+) of (\d+) checks pass", out)
    record(phase, label, code == 0 and not fails,
           (summary[0][0] + "/" + summary[0][1] + " pass" if summary else "") + ("; " + " | ".join(fails[:4]) if fails else ""),
           t)
    return fails


def p5_resume(work, workers):
    code, out, t = cli("run", work, workers)
    todo = [ln for ln in out.splitlines() if re.search(r": \d+ runs on \d+ instances", ln)]
    record("P5", "second run: nothing to do in any block", code == 0 and not todo, todo[0][:160] if todo else "", t)


def p6_rebuild(work):
    rep = os.path.join(work, "results", "03_report")
    keep = os.path.join(work, "report_from_all")
    shutil.rmtree(keep, ignore_errors=True)
    shutil.copytree(rep, keep)
    code, out, t = cli("report", work, None)
    a = {os.path.relpath(p, keep) for p in glob.glob(os.path.join(keep, "**", "*"), recursive=True) if os.path.isfile(p)}
    b = {os.path.relpath(p, rep) for p in glob.glob(os.path.join(rep, "**", "*"), recursive=True) if os.path.isfile(p)}
    diff = [f for f in a & b if f.endswith((".csv", ".tex")) and
            open(os.path.join(keep, f), "rb").read() != open(os.path.join(rep, f), "rb").read()]
    ok = code == 0 and a == b and not diff
    record("P6", "report rebuilt from the pkl files equals the one of `all`", ok,
           f"{len(b)} files; only before {len(a - b)}, only after {len(b - a)}, differing tables {len(diff)} {diff[:3]}", t)


def p6b_rerun(work, workers, block="E4a_equal_budgets", method="CRI+C"):
    """The procedure for recomputing one method after a fix (python -m cri forget ... then run)."""
    code, out, t = cli("forget", work, None, ["--only", block, "--methods", method])
    m = re.findall(r"forgot (\d+) runs", out)
    n = int(m[-1]) if m else 0
    code2, out2, t2 = cli("run", work, workers)
    done = re.findall(r"\] (\S+): (\d+) runs on \d+ instances", out2)
    ok = code == 0 and code2 == 0 and n > 0 and done == [(block, str(n))]
    record("P6b", f"forget {method} in {block}, run: only those runs are recomputed", ok,
           f"forgot {n}; recomputed {done}", t + t2)
    code3, out3, t3 = cli("report", work, None)
    if code3 != 0:
        record("P6b", "audit after the rerun", False, f"report failed (exit {code3})", t3)
        return False
    return not p4_audit(work, phase="P6b", label="audit after the rerun")


def p7_smoke(work):
    cfg = os.path.join(work, "smoke_cfg.yaml")
    with open(cfg, "w", encoding="utf-8") as f:
        f.write(f"base: {os.path.join(ROOT, 'config.yaml').replace(os.sep, '/')}\nrun:\n  output: smoke_results\n"
                "  cache: smoke_cache\n")
    code, out, t = sh([PY, "-m", "tests.smoke_large", cfg, "--instances",
                       "medium_omega_n50_T96_000,medium_staggered_n50_T96_000", "--budget", "1", "--workers", "2"])
    m = re.findall(r"(\d+) method runs to check", out)
    record("P7", "smoke test (2 instances in parallel)", code == 0 and m and m[-1] == "0",
           f"{m[-1] if m else '?'} runs to check", t)


def p8_launcher(work):
    if os.name != "nt":
        record("P8", "run_all.bat control flow", True, "skipped (not Windows)")
        return
    d = os.path.join(work, "launcher")
    os.makedirs(d, exist_ok=True)
    stub = os.path.join(d, "stub.py")
    with open(stub, "w", encoding="utf-8") as f:
        f.write("import os, sys\nargs = ' '.join(sys.argv[1:])\n"
                "open(os.environ['STUB_LOG'], 'a', encoding='utf-8').write(os.path.basename(os.getcwd()) + ' | ' + args + '\\n')\n"
                "fail = os.environ.get('FAIL_AT', '')\nsys.exit(1 if fail and fail in args else 0)\n")
    bat = os.path.join(ROOT, "run_all.bat")
    log = os.path.join(d, "calls.txt")

    def case(fail, fresh, args="", out_dir=os.path.join(d, "out")):
        if fresh:
            shutil.rmtree(out_dir, ignore_errors=True)
        if os.path.exists(log):
            os.remove(log)
        env = {"PY": f'"{PY}" "{stub}"', "OUT": out_dir, "STUB_LOG": log, "FAIL_AT": fail}
        code, out, _ = sh(f'cmd /c ""{bat}" {args} < nul"', env=env)
        calls = open(log, encoding="utf-8").read().splitlines() if os.path.exists(log) else []
        return out, [c.split(" | ", 1)[1] for c in calls]

    out, calls = case("", True)
    expect = ["-m pytest", "-m tests.smoke_large", "verify_theory.py", "-m tests.test_faithful", "-m cri plan",
              "-m cri run", "-m cri report", "-m cri audit"]
    seq = [next((e for e in expect if c.startswith(e)), None) for c in calls]
    seq = [s for s in seq if s]
    o = os.path.join(d, "out")
    full = (any(c.startswith("-m tests.test_faithful --instances 6 --runs 20 --out") and o in c for c in calls)
            and any(c.startswith("verify_theory.py") and os.path.join(o, "05_logs") in c for c in calls)
            and all(f'--output {o}' in c for c in calls if c.startswith("-m cri")))
    ok1 = seq == expect and "FINISHED" in out and "Fresh run from A to Z" in out and full
    out2, calls2 = case("", False)
    ok2 = not any(c.startswith(("-m pytest", "-m tests.smoke_large", "verify_theory.py", "-m tests.test_faithful"))
                  for c in calls2) and "FINISHED" in out2 and "Resuming" in out2
    out3, calls3 = case("smoke_large", True)
    ok3 = "STOPPED" in out3 and not any(c.startswith("-m cri run") for c in calls3)
    out4, calls4 = case("cri run", False)
    ok4 = "STOPPED" in out4 and not any(c.startswith("-m cri report") for c in calls4)
    out5, calls5 = case("cri audit", False)
    ok5 = "STOPPED" in out5 and "audit found problems" in out5
    record("P8", "run_all.bat: fresh / second run / failed smoke / stopped campaign / failed audit",
           ok1 and ok2 and ok3 and ok4 and ok5, f"{ok1} {ok2} {ok3} {ok4} {ok5}")
    ot = os.path.join(d, "out_tiny")
    out6, calls6 = case("", True, "tiny", ot)
    want = ["-m tests.smoke_large config_quick.yaml --instances ",
            "verify_theory.py --quick --out " + os.path.join(ot, "05_logs"),
            "-m tests.test_faithful --instances 2 --runs 3 --out " + os.path.join(ot, "04_faithfulness_check"),
            "-m cri plan config_quick.yaml --output " + ot, "-m cri run config_quick.yaml --output " + ot,
            "-m cri report config_quick.yaml --output " + ot, "-m cri audit config_quick.yaml --output " + ot]
    miss = [w for w in want if not any(c.startswith(w) for c in calls6)]
    ok6 = not miss and "FINISHED" in out6 and os.path.isdir(os.path.join(ot, "05_logs")) \
        and not os.path.exists(os.path.join(ROOT, "results_quick"))
    record("P8", "run_all.bat tiny: tiny settings and its own results folder at every step", ok6,
           f"missing {miss}" if miss else "")


def p9_theory(work, workers):
    res = os.path.join(work, "theory")
    os.makedirs(res, exist_ok=True)
    code, out, t = sh([PY, "-c", "import sys; sys.argv = ['verify_theory.py', '--quick', '--workers', '%d']; "
                       "sys.path.insert(0, '.'); import verify_theory as V; V.RES = r'%s'; V.main()"
                       % (max(2, workers or 2), res)], cwd=LAB)
    m = re.findall(r"TOTAL failures: (\d+) over (\d+) tests", out)
    record("P9", "quick theory verification (parallel)", code == 0 and m and m[-1][0] == "0",
           f"{m[-1][0]} failures over {m[-1][1]} tests" if m else out[-200:], t)


def p10_clean(before):
    after = {p for p in glob.glob(os.path.join(ROOT, "results*")) + glob.glob(os.path.join(LAB, "results*"))}
    new = sorted(after - before)
    record("P10", "no results folder created in the code folders", not new, new)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=0, help="campaign workers (default: automatic)")
    ap.add_argument("--heavy", action="store_true", help="also the quick theory verification")
    ap.add_argument("--keep", action="store_true", help="keep the work folder")
    ap.add_argument("--work", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    work = a.work or os.path.join(tempfile.gettempdir(), "cri_verify_" + dt.datetime.now().strftime("%Y%m%d_%H%M%S"))
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    global LOGDIR
    LOGDIR = os.path.join(work, "phase_logs")
    os.makedirs(LOGDIR)
    print(f"verification protocol, work folder {work}", flush=True)
    before = {p for p in glob.glob(os.path.join(ROOT, "results*")) + glob.glob(os.path.join(LAB, "results*"))}
    t0 = time.time()
    p1_static()
    p2_tests()
    p3_campaign(work, a.workers)
    p4_audit(work)
    p5_resume(work, a.workers)
    p6_rebuild(work)
    p6b_rerun(work, a.workers)
    p7_smoke(work)
    p8_launcher(work)
    if a.heavy:
        p9_theory(work, a.workers)
    p10_clean(before)
    n_ok = sum(r["ok"] for r in ROWS)
    lines = [f"# Verification protocol ({dt.datetime.now():%Y-%m-%d %H:%M}), {n_ok} of {len(ROWS)} checks pass, "
             f"{(time.time() - t0) / 60:.1f} min", "", "| phase | check | result | detail |", "|---|---|---|---|"]
    lines += [f"| {r['phase']} | {r['check']} | {'PASS' if r['ok'] else 'FAIL'} | {r['detail'].replace('|', '/')} |"
              for r in ROWS]
    with open(os.path.join(work, "verification_protocol.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    audit_md = os.path.join(work, "results", "05_logs", "audit.md")
    if os.path.exists(audit_md):
        shutil.copy(audit_md, os.path.join(work, "audit.md"))
    print(f"\n{n_ok} of {len(ROWS)} checks pass ({(time.time() - t0) / 60:.1f} min); scorecard: "
          f"{os.path.join(work, 'verification_protocol.md')}")
    if not a.keep and n_ok == len(ROWS):
        for d in ("results", "cache", "report_from_all", "smoke_results", "smoke_cache", "launcher", "theory"):
            shutil.rmtree(os.path.join(work, d), ignore_errors=True)
    return 0 if n_ok == len(ROWS) else 1


if __name__ == "__main__":
    sys.exit(main())
