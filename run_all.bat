@echo off
setlocal
REM ============================================================================
REM  run_all.bat -- everything, end to end, on this machine (Windows)
REM
REM    run_all.bat              the full run: verification, campaign, report -> results\
REM    run_all.bat tiny         the same six steps on tiny data, to check a machine
REM                             first (20-40 min) -> results_quick\
REM    run_all.bat --workers 8  extra arguments go to the campaign (also after "tiny")
REM
REM    Every step uses the cores: tests (pytest-xdist), smoke test (one process per
REM    instance), theory and faithfulness checks (process pools), campaign (one
REM    worker per physical core but one, sized by memory per block).
REM    Verification (each step once per machine; the campaign does not start
REM    if one of them fails):
REM      [1/6] correctness tests                        (pytest tests, in parallel, ~1-3 min)
REM      [2/6] smoke test on large campaign instances   (~10 min)
REM      [3/6] numerical verification of the theory     (theory\verify_theory.py, 15 min to 1 h)
REM      [4/6] faithfulness check against the published code (~10 min)
REM    Experiments:
REM      [5/6] the campaign: every block of config.yaml (resumes from the stored runs)
REM      [6/6] the report, rebuilt from the raw pkl files -> results\03_report\report.html,
REM            then its audit (runs, folders, expected outputs, files, links, statistics)
REM            -> results\05_logs\audit.md
REM
REM  If anything stops it (licence, disk space, restart of the machine), run this
REM  file again: finished steps and stored runs are skipped.
REM  A fresh results folder (none of its step markers, no stored run) is a clean
REM  run from A to Z: every step runs and the campaign gets its own, empty context
REM  cache (05_logs\campaign_id.txt). The tiny run uses its own results folder and
REM  cache, so a full run afterwards starts from zero.
REM  Settings (environment variables; the full run when not set): CFG, OUT, PY,
REM  SMOKE_ARGS, THEORY_ARGS, FAITH_ARGS.
REM  Keep this window open while it runs (closing it stops the campaign).
REM ============================================================================
cd /d "%~dp0"
set "MODE=full"
set "ARGS=%*"
if /i "%~1"=="tiny" (
  set "MODE=tiny"
  set "ARGS=%ARGS:~4%"
)
if "%MODE%"=="tiny" (
  set "CFG=config_quick.yaml"
  if not defined OUT set "OUT=results_quick"
  set "SMOKE_ARGS=--instances large_staggered_n300_T96_000,medium_omega_n50_T48_000 --budget 2"
  set "THEORY_ARGS=--quick"
  set "FAITH_ARGS=--instances 2 --runs 3"
)
if not defined CFG set "CFG=config.yaml"
if not defined OUT set "OUT=results"
if not defined FAITH_ARGS set "FAITH_ARGS=--instances 6 --runs 20"
if not defined PY (
  set "PY=python"
  where python >nul 2>&1 || set "PY=py -3"
)
if not exist "%OUT%" mkdir "%OUT%"
for %%I in ("%OUT%") do set "OUTABS=%%~fI"
set "MK=%OUT%\05_logs"
if not exist "%MK%" mkdir "%MK%"
REM tests in parallel when pytest-xdist is installed (requirements.txt), else one after the other
set "XD="
%PY% -c "import xdist" >nul 2>&1 && set "XD=-n auto"
echo Campaign (%MODE% run) - %date% %time% - config %CFG%, results in %OUT%, step markers in %MK%
set "FRESH=1"
if exist "%MK%\step_*.txt" set "FRESH="
if exist "%OUT%\01_raw_runs" set "FRESH="
if defined FRESH (
  echo Fresh run from A to Z: nothing is stored in %OUT% yet, every step runs.
) else (
  echo Resuming %OUT%: finished steps and stored runs are skipped.
)

echo.
echo ===== [1/6] Correctness tests =====
if exist "%MK%\step_1_tests_passed.txt" (
  echo already passed on this machine - skipped
) else (
  %PY% -m pytest -q %XD% tests || goto failed
  echo passed %date% %time%> "%MK%\step_1_tests_passed.txt"
)

echo.
echo ===== [2/6] Smoke test on large campaign instances =====
if exist "%MK%\step_2_smoke_test_passed.txt" (
  echo already passed on this machine - skipped
) else (
  %PY% -m tests.smoke_large %CFG% %SMOKE_ARGS% || goto failed
  echo passed %date% %time%> "%MK%\step_2_smoke_test_passed.txt"
)

echo.
echo ===== [3/6] Numerical verification of the theory (theory\verify_theory.py) =====
if exist "%MK%\step_3_theory_verification_passed.txt" (
  echo already passed on this machine - skipped
) else (
  pushd "theory"
  %PY% verify_theory.py %THEORY_ARGS% --out "%OUTABS%\05_logs"
  if errorlevel 1 (
    popd
    goto failed
  )
  popd
  %PY% -c "import sys, pandas as pd; f = int(pd.read_csv(sys.argv[1]).failures.sum()); print('theory verification failures:', f); sys.exit(1 if f else 0)" "%OUTABS%\05_logs\theory_verification.csv"
  if errorlevel 1 goto failed
  echo passed %date% %time%> "%MK%\step_3_theory_verification_passed.txt"
)

echo.
echo ===== [4/6] Faithfulness check against the published code =====
if exist "%MK%\step_4_faithfulness_check_done.txt" (
  echo already done on this machine - skipped
) else (
  %PY% -m tests.test_faithful %FAITH_ARGS% --out "%OUT%\04_faithfulness_check" || goto failed
  echo done %date% %time%> "%MK%\step_4_faithfulness_check_done.txt"
)

echo.
echo ===== [5/6] Campaign (resumes from the stored runs) =====
%PY% -m cri plan %CFG% --output "%OUT%" %ARGS%
%PY% -m cri run %CFG% --output "%OUT%" %ARGS% || goto failed

echo.
echo ===== [6/6] Report (rebuilt from the raw pkl files), then its audit =====
%PY% -m cri report %CFG% --output "%OUT%" || goto failed
%PY% -m cri audit %CFG% --output "%OUT%"
if errorlevel 1 (
  echo The audit found problems: see %MK%\audit.md ^(the report is written^)
  goto failed
)

echo.
echo FINISHED %date% %time%. Report: %OUT%\03_report\report.html
goto end

:failed
echo.
echo STOPPED at the step above (see its messages, and %MK%\run_log.txt for the campaign).
echo Fix the cause if needed, then run run_all.bat again: finished steps and stored runs are skipped.

:end
pause
endlocal
