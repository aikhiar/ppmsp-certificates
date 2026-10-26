# Results of the computational study

The campaign behind Section 6 of the paper *Preemptive Peak Power Scheduling with A Priori
Certificates: Bounds, Certified Algorithms and Large-Scale Experiments* (A. Khiar, M. E. A. Brahmia,
A. Oulamara, M. Golabi, A. Azerine and L. Idoumghar, submitted to *Omega*): 41,801 runs on 195
instances, in 17 experiment blocks, with the numerical verification of the theory. Every table and
figure of the paper and of its Supplementary Material, and every number quoted in them, is computed
from these files.

## Contents

```
README.md               this file
campaign_config.yaml    the configuration the campaign ran with, as recorded (frozen copy of
                        results/05_logs/config_used.json)
report_config.yaml      the configuration of the report: the repository's config.yaml, with the same
                        settings as campaign_config.yaml and the final wording
results/
  README.md             what each folder holds
  01_raw_runs/          the source of truth: one pickle per (block, instance) job, a list of runs with
                        their peak, charged time, trace, guarantee, lower bound and status
  02_aggregated_data/   runs_enriched.csv: every run with every gap measure; instance_references.csv:
                        LB*, best known and optimal peaks per instance; tuned_defaults.json: the
                        parameters chosen on the tuning set and used by the later blocks
  03_report/            report.html and report.md (open first), then one folder per section and block:
                        tables (.csv, .md, .tex), statistics (tests, ranks, effect sizes) and figures
  04_faithfulness_check/  the original code of the earlier methods against their re-implementation
  05_logs/              run log, configuration used, audit, theory verification, campaign identifier,
                        step markers of run_all.bat
```

The two CSV files of `02_aggregated_data/` can be read with any tool. The pickles of
`01_raw_runs/` hold the framework's own records and are read with the code of the repository (the
`cri` package). The other aggregated tables (runs, traces, bound traces, solutions, instances, as
pickles) are not stored: the report rebuilds them from `01_raw_runs/` in a few minutes.

## The campaign

- **Code:** the repository of the paper, https://github.com/aikhiar/ppmsp-certificates, run end to
  end with `run_all.bat` on the campaign machine: the correctness tests, the smoke test, the
  numerical verification of the theory, the faithfulness check against the original code of the
  earlier methods, the campaign and the report (step markers in `results/05_logs/`).
- **Machine:** a virtual machine with 32 cores of two Intel Xeon Gold 6330 processors (2.0 GHz) and
  32 GB of RAM, under Windows Server 2022; Python 3.10, Numba 0.61, Gurobi 13. Every run records its
  host.
- **Date and identifier:** 25 October 2026, campaign `20261025_021515_9388`
  (`results/05_logs/campaign_id.txt`), a fresh run from the first step to the last, with its own
  context cache.
- **Code version:** the campaign ran with the code of 25 October 2026. The later changes to the
  repository concern its layout (one folder), the wording of descriptions and reports, the
  formatting of the report tables, the warm-up of the compiled kernels before the first measured
  run, and the verification tools; none of them changes a setting that drives a run.
  `report_config.yaml` and the recorded `results/05_logs/config_used.json` have the same settings,
  and differ only in descriptions, the blocks' "addresses", the report title and the cache folder.
- **Report and audit:** rebuilt on 26 October 2026 with the code of the repository as of that day.
  The tables and figures of the paper rebuilt from them are identical to those of the paper.

## Validity

- **Audit:** 72 of 72 checks pass (`results/05_logs/audit.md`): every planned run stored, every
  schedule feasible (41,543), no a priori guarantee violated (10,891 checked), no lower bound above
  a feasible peak, every budget overrun explained, folders, files, links and statistics consistent.
- **Theory:** every statement of Sections 3 and 4 of the paper verified numerically, 12,758,086
  tests and no failure (`results/05_logs/theory_verification.md`).
- **Faithfulness:** the re-implemented earlier methods against their original code
  (`results/04_faithfulness_check/faithfulness.md`).

## Rebuilding the report and the tables of the paper

From the root of the repository, with the requirements installed (in the repository this folder is
`paper_results/`):

```
python -m cri report paper_results/report_config.yaml     # aggregated data and 03_report
python -m cri audit  paper_results/report_config.yaml     # results/05_logs/audit.md
python tools/paper_artifacts.py paper_results/results <paper folder> --numbers numbers.md
```

The last command writes the tables and figures of Section 6 of the paper and of its Supplementary
Material to `<paper folder>/tables/` and `<paper folder>/figures/`, and lists every number quoted in
the text.

## Notes

- The report applies the evaluation rule of the framework: every run is credited with what it had
  found by its budget + 10% + 0.05 s. In this campaign the rule changes 4 runs (2 of CRI and 2 of
  W-LNS, at 1 s on n >= 1,000); every other budget overrun is listed with its reason in
  `results/03_report/03_validity_checks/`.
- `campaign_config.yaml`, `results/05_logs/config_used.json` and `results/05_logs/run_log.txt` are
  kept as they were written. The descriptions of the two configurations carry labels from the
  preparation of the revision (`report_config.yaml` has the final wording), and the run log names
  the folders of the machines where it was written: the campaign machine and the machine that
  rebuilt the report.
- License: MIT, as the repository.
