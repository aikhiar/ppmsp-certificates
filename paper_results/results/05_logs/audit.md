# Audit of the results folder of campaign 20261025_021515_9388

72 of 72 checks pass.

| area | check | result | detail |
|---|---|---|---|
| runs | every planned run is stored | PASS | all stored |
| runs | aggregated runs table exists | PASS | 41801 runs |
| runs | every run ended with status ok (or not_available) | PASS |  |
| runs | every schedule is feasible | PASS | 41543 schedules |
| runs | every a priori guarantee holds | PASS | 0 violated of 10891 |
| runs | no lower bound above a feasible value | PASS | 0 violations of 4902 |
| runs | no unexpected budget overrun (>10% + 0.05 s) | PASS | no gain after the budget: {'GUROBI-agg': 30, 'WLNS': 10, 'HSC-b': 9, 'GUROBI-std': 6, 'CRI': 2, 'LLS': 2, 'GUROBI-agg-4t': 2} / documented overruns: {'RLP-b': 30} / expected single-shot overruns: {'CE-conf-comp': 29, 'IR': 5, 'MT-lp-b': 3} |
| layout | results folder 01_raw_runs/ | PASS | 01_raw_runs |
| layout | results folder 02_aggregated_data/ | PASS | 02_aggregated_data |
| layout | results folder 03_report/ | PASS | 03_report |
| layout | results folder 05_logs/ | PASS | 05_logs |
| layout | results README.md | PASS |  |
| layout | run log | PASS |  |
| layout | report report.md | PASS |  |
| layout | report report.html | PASS |  |
| layout | report index.md | PASS |  |
| layout | report README.md | PASS |  |
| layout | report section 00_campaign_overview/ | PASS |  |
| layout | report section 01_instances/ | PASS |  |
| layout | report section 02_exact_references_and_bounds/ | PASS |  |
| layout | report section 03_validity_checks/ | PASS |  |
| layout | budget ladder equal_budgets_1s_to_600s | PASS | 30_budget_ladders\equal_budgets_1s_to_600s\tables\mean_gap_by_budget.csv |
| layout | budget ladder state_of_the_art_10s_to_60s | PASS | 30_budget_ladders\state_of_the_art_10s_to_60s\tables\mean_gap_by_budget.csv |
| outputs | E0_sanity: block folder | PASS | 03_report\10_E0_sanity |
| outputs | E0_sanity: 14 expected outputs of comparison | PASS | all present |
| outputs | E1_certificates: block folder | PASS | 03_report\11_E1_certificates |
| outputs | E1_certificates: 4 expected outputs of certificates | PASS | all present |
| outputs | E8a_tuning_faithful: block folder | PASS | 03_report\12_E8a_tuning_faithful |
| outputs | E8a_tuning_faithful: 1 expected outputs of tuning | PASS | all present |
| outputs | E8b_tuning_budget: block folder | PASS | 03_report\13_E8b_tuning_budget |
| outputs | E8b_tuning_budget: 1 expected outputs of tuning | PASS | all present |
| outputs | E2_head_to_head: block folder | PASS | 03_report\14_E2_head_to_head |
| outputs | E2_head_to_head: 16 expected outputs of comparison, head_to_head | PASS | all present |
| outputs | E2b_head_to_head_budgets: block folder | PASS | 03_report\15_E2b_head_to_head_budgets |
| outputs | E2b_head_to_head_budgets: 33 expected outputs of comparison, head_to_head | PASS | all present |
| outputs | E4a_equal_budgets: block folder | PASS | 03_report\16_E4a_equal_budgets |
| outputs | E4a_equal_budgets: 40 expected outputs of comparison, anytime, gurobi | PASS | all present |
| outputs | E4b_equal_budgets_60s: block folder | PASS | 03_report\17_E4b_equal_budgets_60s |
| outputs | E4b_equal_budgets_60s: 20 expected outputs of comparison, anytime, gurobi | PASS | all present |
| outputs | E3_long_runs: block folder | PASS | 03_report\18_E3_long_runs |
| outputs | E3_long_runs: 20 expected outputs of comparison, anytime, gurobi | PASS | all present |
| outputs | E3x_long_runs_xlarge: block folder | PASS | 03_report\19_E3x_long_runs_xlarge |
| outputs | E3x_long_runs_xlarge: 20 expected outputs of comparison, anytime, gurobi | PASS | all present |
| outputs | E5_ablation: block folder | PASS | 03_report\20_E5_ablation |
| outputs | E5_ablation: 15 expected outputs of comparison | PASS | all present |
| outputs | E5b_ablation_60s: block folder | PASS | 03_report\21_E5b_ablation_60s |
| outputs | E5b_ablation_60s: 15 expected outputs of comparison | PASS | all present |
| outputs | E6_scalability: block folder | PASS | 03_report\22_E6_scalability |
| outputs | E6_scalability: 19 expected outputs of scalability, comparison, gurobi | PASS | all present |
| outputs | E7_gurobi_threads: block folder | PASS | 03_report\23_E7_gurobi_threads |
| outputs | E7_gurobi_threads: 34 expected outputs of comparison, gurobi | PASS | all present |
| outputs | E9_managerial: block folder | PASS | 03_report\24_E9_managerial |
| outputs | E9_managerial: 2 expected outputs of managerial | PASS | all present |
| outputs | E10a_state_of_the_art: block folder | PASS | 03_report\25_E10a_state_of_the_art |
| outputs | E10a_state_of_the_art: 15 expected outputs of sota | PASS | all present |
| outputs | E10b_state_of_the_art_60s: block folder | PASS | 03_report\26_E10b_state_of_the_art_60s |
| outputs | E10b_state_of_the_art_60s: 15 expected outputs of sota | PASS | all present |
| files | 278 tables exist as .csv, .md and .tex | PASS | [] |
| files | every table is readable | PASS | [] |
| files | no empty table | PASS | [] |
| files | no table whose numbers are all missing | PASS | [] |
| files | 170 figures are valid PNG files | PASS | [] |
| files | every figure also exists as PDF | PASS | [] |
| report | no analysis failed | PASS | [] |
| report | 448 links of report.md resolve | PASS | [] |
| report | index.md lists every table and figure | PASS | [] |
| report | index.md lists only existing files | PASS | [] |
| report | 278 LaTeX labels are unique | PASS | [] |
| report | file names without spaces | PASS | [] |
| report | paths inside the results folder at most 150 characters (fits the Windows limit of 260 with a results folder path of up to 109 characters) | PASS | longest 109 |
| report | absolute paths shorter than 260 characters where the results are | PASS | longest 209; the results folder path has 99 characters |
| statistics | p-values, Holm adjustment, ranks and effect sizes are consistent | PASS | [] |
