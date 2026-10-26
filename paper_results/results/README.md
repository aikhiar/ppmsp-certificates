# Results of the campaign

| folder | content |
|---|---|
| `01_raw_runs/` | the source of truth: one pickle per (experiment block, instance) job, a list of runs with their peak, charged time, trace, guarantee, lower bound and status; `_references/` holds the exact references and `_contexts/` the bound summaries of each instance |
| `02_aggregated_data/` | tables rebuilt from `01_raw_runs/` by `python -m cri report` (runs, enriched runs with every gap measure as .pkl and .csv, traces, Gurobi bound traces, solutions, references, instances, tuning tables, tuned defaults) |
| `03_report/` | `report.html` / `report.md` (open these first), `index.md` (every table and figure with its caption) and one folder per section and experiment block: `tables/` (.csv, .md, .tex), `statistics/` (tests, ranks, effect sizes, their diagrams) and `figures/` (.png, .pdf) |
| `04_faithfulness_check/` | the original code against the re-implementation of the earlier methods |
| `05_logs/` | `run_log.txt` (every block, job and worker), `config_used.json`, `environment.jsonl` (machine, processor, cores, RAM and software versions of every start of `run`; recorded by this version of the framework), `audit.md`, `theory_verification.csv`/`.md` (step 3 of `run_all.bat`), the step markers of `run_all.bat` |

Nothing in `02_aggregated_data/` or `03_report/` needs to be kept: both are rebuilt from `01_raw_runs/`.
