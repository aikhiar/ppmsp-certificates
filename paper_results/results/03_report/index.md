# Every table and figure of the report (278 tables, 170 figures)

Tables exist as .csv, .md and .tex; figures as .png and .pdf.

| kind | file | caption |
|---|---|---|
| table | 00_campaign_overview/tables/campaign_hosts.csv | Runs per experiment and machine (time comparisons are meaningful only between runs of the same machine) |
| table | 00_campaign_overview/tables/campaign_status.csv | Runs per experiment and status |
| table | 00_campaign_overview/tables/class_defaults.csv | Default parameters per method class |
| table | 00_campaign_overview/tables/headline_results.csv | Per block and budget: best method by the mean gap over instances, the control's mean gap and average rank, and the Friedman p-value (details in each block's statistics/) |
| table | 00_campaign_overview/tables/method_library.csv | Method library (explicit parameters; the class defaults of the configuration apply otherwise) |
| table | 01_instances/tables/instance_sets.csv | Instance sets (means over the instances of each group) |
| table | 02_exact_references_and_bounds/tables/certify_costs_by_family_and_n.csv | Median computing time (s) of the Certify artifacts |
| table | 02_exact_references_and_bounds/tables/exact_references_summary.csv | Exact references (aggregated model, time limit 300 s) |
| table | 03_validity_checks/tables/budget_overruns.csv | Runs whose charged time exceeds the budget by more than 10% (+0.05 s), per block, method and budget: number of runs, worst and mean ratio charged time / budget, range of n, runs whose credited result still comes after the budget, runs with no schedule by the budget, runs evaluated at the budget, and the reason (budget = budget + 10% + 0.05 s) |
| table | 03_validity_checks/tables/validity_summary.csv | Validity checks of the whole campaign |
| table | 04_faithfulness_of_earlier_methods/tables/faithfulness_detail.csv | Faithfulness per instance and method |
| table | 04_faithfulness_of_earlier_methods/tables/faithfulness_summary.csv | Faithfulness per method |
| table | 05_theory_verification/tables/theory_verification.csv | Verification of each statement |
| figure | 10_E0_sanity/budget_5s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 10_E0_sanity/budget_5s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 10_E0_sanity/budget_5s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 10_E0_sanity/budget_5s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 10_E0_sanity/budget_5s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 10_E0_sanity/budget_5s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 10_E0_sanity/budget_5s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 10_E0_sanity/budget_5s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 10_E0_sanity/budget_5s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 10_E0_sanity/budget_5s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 351 pairs in the files, the 0 most significant of the 0 significant ones shown |
| table | 10_E0_sanity/budget_5s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 10_E0_sanity/budget_5s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 10_E0_sanity/budget_5s/tables/charged_time.csv | Charged time (s) |
| table | 10_E0_sanity/budget_5s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 10_E0_sanity/budget_5s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 10_E0_sanity/budget_5s/tables/summary.csv | E0_sanity, budget 5 s: gap_lb (per-instance mean over seeds) |
| figure | 11_E1_certificates/certificates/figures/lower_certificates_tightness.png | Tightness of the lower certificates (1 = the optimum) |
| figure | 11_E1_certificates/certificates/figures/upper_certificates_tightness.png | Tightness of the upper certificates (1 = the optimum) |
| table | 11_E1_certificates/certificates/tables/a_priori_optimal_instances.csv | Instances proved optimal by the certificates alone (U_best = LB): no search and no MILP |
| table | 11_E1_certificates/certificates/tables/all_certificates_vs_optimum.csv | Every certificate against the optimum (or best known value): a violation is an upper certificate below a proven optimum or a lower one above a feasible value |
| table | 11_E1_certificates/certificates/tables/certificate_ratios_by_family_and_n.csv | Mean certificate / OPT (or best known) by family and size |
| table | 11_E1_certificates/certificates/tables/certificate_step_costs.csv | Median cost of each certificate step (s) |
| table | 11_E1_certificates/certificates/tables/certificates_within_tolerance.csv | Share of instances (%) where the certificate is within 0.5 / 1 / 5 % of OPT (or best known) |
| table | 11_E1_certificates/certificates/tables/two_sided_certified_interval.csv | Two-sided certificate: mean (U_best - LB)/LB, U_best above and LB below the optimum / best known value (%) |
| table | 12_E8a_tuning_faithful/tuning/tables/grid_SA.csv | Tuning grid of SA (mean relative gap to the best value per tuning instance) |
| table | 12_E8a_tuning_faithful/tuning/tables/marginal_effects_SA.csv | Marginal effect of each parameter of SA (mean over the other parameters) |
| table | 13_E8b_tuning_budget/tuning/tables/grid_LLS.csv | Tuning grid of LLS (mean relative gap to the best value per tuning instance) |
| table | 13_E8b_tuning_budget/tuning/tables/grid_SA-b.csv | Tuning grid of SA-b (mean relative gap to the best value per tuning instance) |
| table | 13_E8b_tuning_budget/tuning/tables/grid_WLNS.csv | Tuning grid of WLNS (mean relative gap to the best value per tuning instance) |
| table | 13_E8b_tuning_budget/tuning/tables/marginal_effects_LLS.csv | Marginal effect of each parameter of LLS (mean over the other parameters) |
| table | 13_E8b_tuning_budget/tuning/tables/marginal_effects_SA-b.csv | Marginal effect of each parameter of SA-b (mean over the other parameters) |
| table | 13_E8b_tuning_budget/tuning/tables/marginal_effects_WLNS.csv | Marginal effect of each parameter of WLNS (mean over the other parameters) |
| table | 14_E2_head_to_head/head_to_head/tables/pairs_wilcoxon_holm.csv | Head-to-head: earlier method (A) against its certified counterpart (B) |
| figure | 14_E2_head_to_head/single_run/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 14_E2_head_to_head/single_run/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 14_E2_head_to_head/single_run/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 14_E2_head_to_head/single_run/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 14_E2_head_to_head/single_run/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 14_E2_head_to_head/single_run/statistics/CE-cut-excess_vs_each_method.csv | CE-cut-excess against every other method (wins = instances where the control is strictly better) |
| table | 14_E2_head_to_head/single_run/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 14_E2_head_to_head/single_run/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 14_E2_head_to_head/single_run/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 14_E2_head_to_head/single_run/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 14_E2_head_to_head/single_run/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 14_E2_head_to_head/single_run/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 190 pairs in the files, the 40 most significant of the 163 significant ones shown |
| table | 14_E2_head_to_head/single_run/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 14_E2_head_to_head/single_run/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 14_E2_head_to_head/single_run/tables/charged_time.csv | Charged time (s) |
| table | 14_E2_head_to_head/single_run/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 14_E2_head_to_head/single_run/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 14_E2_head_to_head/single_run/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 14_E2_head_to_head/single_run/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 14_E2_head_to_head/single_run/tables/seed_variability.csv | Variability over seeds (per-instance standard deviation and range) |
| table | 14_E2_head_to_head/single_run/tables/summary.csv | E2_head_to_head, budget single run: gap_lb (per-instance mean over seeds) |
| figure | 15_E2b_head_to_head_budgets/across_budgets/figures/gap_vs_budget.png | Median gap_lb (IQR band) against the time budget: the time-quality trade-off of each method |
| table | 15_E2b_head_to_head_budgets/across_budgets/tables/mean_charged_time_by_budget.csv | Mean charged time (s) at every budget |
| table | 15_E2b_head_to_head_budgets/across_budgets/tables/mean_gap_by_budget.csv | Mean gap_lb (per-instance mean over seeds) of every method at every budget |
| figure | 15_E2b_head_to_head_budgets/budget_10s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 15_E2b_head_to_head_budgets/budget_10s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 15_E2b_head_to_head_budgets/budget_10s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 15_E2b_head_to_head_budgets/budget_10s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 15_E2b_head_to_head_budgets/budget_10s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 15_E2b_head_to_head_budgets/budget_10s/statistics/CRI-R_vs_each_method.csv | CRI-R against every other method (wins = instances where the control is strictly better) |
| table | 15_E2b_head_to_head_budgets/budget_10s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 15_E2b_head_to_head_budgets/budget_10s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 15_E2b_head_to_head_budgets/budget_10s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 15_E2b_head_to_head_budgets/budget_10s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 15_E2b_head_to_head_budgets/budget_10s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 15_E2b_head_to_head_budgets/budget_10s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 45 pairs in the files, the 33 most significant of the 33 significant ones shown |
| table | 15_E2b_head_to_head_budgets/budget_10s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 15_E2b_head_to_head_budgets/budget_10s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 15_E2b_head_to_head_budgets/budget_10s/tables/charged_time.csv | Charged time (s) |
| table | 15_E2b_head_to_head_budgets/budget_10s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 15_E2b_head_to_head_budgets/budget_10s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 15_E2b_head_to_head_budgets/budget_10s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 15_E2b_head_to_head_budgets/budget_10s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 15_E2b_head_to_head_budgets/budget_10s/tables/seed_variability.csv | Variability over seeds (per-instance standard deviation and range) |
| table | 15_E2b_head_to_head_budgets/budget_10s/tables/summary.csv | E2b_head_to_head_budgets, budget 10 s: gap_lb (per-instance mean over seeds) |
| figure | 15_E2b_head_to_head_budgets/budget_1s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 15_E2b_head_to_head_budgets/budget_1s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 15_E2b_head_to_head_budgets/budget_1s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 15_E2b_head_to_head_budgets/budget_1s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 15_E2b_head_to_head_budgets/budget_1s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 15_E2b_head_to_head_budgets/budget_1s/statistics/CRI-R_vs_each_method.csv | CRI-R against every other method (wins = instances where the control is strictly better) |
| table | 15_E2b_head_to_head_budgets/budget_1s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 15_E2b_head_to_head_budgets/budget_1s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 15_E2b_head_to_head_budgets/budget_1s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 15_E2b_head_to_head_budgets/budget_1s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 15_E2b_head_to_head_budgets/budget_1s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 15_E2b_head_to_head_budgets/budget_1s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 45 pairs in the files, the 32 most significant of the 32 significant ones shown |
| table | 15_E2b_head_to_head_budgets/budget_1s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 15_E2b_head_to_head_budgets/budget_1s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 15_E2b_head_to_head_budgets/budget_1s/tables/charged_time.csv | Charged time (s) |
| table | 15_E2b_head_to_head_budgets/budget_1s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 15_E2b_head_to_head_budgets/budget_1s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 15_E2b_head_to_head_budgets/budget_1s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 15_E2b_head_to_head_budgets/budget_1s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 15_E2b_head_to_head_budgets/budget_1s/tables/seed_variability.csv | Variability over seeds (per-instance standard deviation and range) |
| table | 15_E2b_head_to_head_budgets/budget_1s/tables/summary.csv | E2b_head_to_head_budgets, budget 1 s: gap_lb (per-instance mean over seeds) |
| table | 15_E2b_head_to_head_budgets/head_to_head/tables/pairs_wilcoxon_holm.csv | Head-to-head: earlier method (A) against its certified counterpart (B) |
| figure | 16_E4a_equal_budgets/across_budgets/figures/gap_vs_budget.png | Median gap_lb (IQR band) against the time budget: the time-quality trade-off of each method |
| table | 16_E4a_equal_budgets/across_budgets/tables/mean_charged_time_by_budget.csv | Mean charged time (s) at every budget |
| table | 16_E4a_equal_budgets/across_budgets/tables/mean_gap_by_budget.csv | Mean gap_lb (per-instance mean over seeds) of every method at every budget |
| figure | 16_E4a_equal_budgets/budget_10s/figures/anytime_median_gap_all.png | Median (IQR band) gap to LB* over time, all; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 16_E4a_equal_budgets/budget_10s/figures/anytime_median_gap_omega.png | Median (IQR band) gap to LB* over time, omega; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 16_E4a_equal_budgets/budget_10s/figures/anytime_median_gap_overnight.png | Median (IQR band) gap to LB* over time, overnight; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 16_E4a_equal_budgets/budget_10s/figures/anytime_median_gap_staggered.png | Median (IQR band) gap to LB* over time, staggered; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 16_E4a_equal_budgets/budget_10s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 16_E4a_equal_budgets/budget_10s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 16_E4a_equal_budgets/budget_10s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 16_E4a_equal_budgets/budget_10s/figures/gurobi_dual_bound_over_time.png | Median distance of Gurobi's dual bound below the best known lower bound over time (0 = as strong as LB*) |
| figure | 16_E4a_equal_budgets/budget_10s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 16_E4a_equal_budgets/budget_10s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 16_E4a_equal_budgets/budget_10s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 16_E4a_equal_budgets/budget_10s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 16_E4a_equal_budgets/budget_10s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 16_E4a_equal_budgets/budget_10s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 16_E4a_equal_budgets/budget_10s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 16_E4a_equal_budgets/budget_10s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 16_E4a_equal_budgets/budget_10s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 66 pairs in the files, the 40 most significant of the 60 significant ones shown |
| table | 16_E4a_equal_budgets/budget_10s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 16_E4a_equal_budgets/budget_10s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 16_E4a_equal_budgets/budget_10s/tables/charged_time.csv | Charged time (s) |
| table | 16_E4a_equal_budgets/budget_10s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 16_E4a_equal_budgets/budget_10s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 16_E4a_equal_budgets/budget_10s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 16_E4a_equal_budgets/budget_10s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 16_E4a_equal_budgets/budget_10s/tables/seed_variability.csv | Variability over seeds (per-instance standard deviation and range) |
| table | 16_E4a_equal_budgets/budget_10s/tables/summary.csv | E4a_equal_budgets, budget 10 s: gap_lb (per-instance mean over seeds) |
| table | 16_E4a_equal_budgets/budget_10s/tables/time_to_target_and_primal_integral.csv | Time to targets (median s; inf = not reached), share of runs reaching each target (%), mean primal integral (normalized by the budget) |
| figure | 16_E4a_equal_budgets/budget_1s/figures/anytime_median_gap_all.png | Median (IQR band) gap to LB* over time, all; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 16_E4a_equal_budgets/budget_1s/figures/anytime_median_gap_omega.png | Median (IQR band) gap to LB* over time, omega; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 16_E4a_equal_budgets/budget_1s/figures/anytime_median_gap_overnight.png | Median (IQR band) gap to LB* over time, overnight; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 16_E4a_equal_budgets/budget_1s/figures/anytime_median_gap_staggered.png | Median (IQR band) gap to LB* over time, staggered; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 16_E4a_equal_budgets/budget_1s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 16_E4a_equal_budgets/budget_1s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 16_E4a_equal_budgets/budget_1s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 16_E4a_equal_budgets/budget_1s/figures/gurobi_dual_bound_over_time.png | Median distance of Gurobi's dual bound below the best known lower bound over time (0 = as strong as LB*) |
| figure | 16_E4a_equal_budgets/budget_1s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 16_E4a_equal_budgets/budget_1s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 16_E4a_equal_budgets/budget_1s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 16_E4a_equal_budgets/budget_1s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 16_E4a_equal_budgets/budget_1s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 16_E4a_equal_budgets/budget_1s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 16_E4a_equal_budgets/budget_1s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 16_E4a_equal_budgets/budget_1s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 16_E4a_equal_budgets/budget_1s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 66 pairs in the files, the 40 most significant of the 61 significant ones shown |
| table | 16_E4a_equal_budgets/budget_1s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 16_E4a_equal_budgets/budget_1s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 16_E4a_equal_budgets/budget_1s/tables/charged_time.csv | Charged time (s) |
| table | 16_E4a_equal_budgets/budget_1s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 16_E4a_equal_budgets/budget_1s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 16_E4a_equal_budgets/budget_1s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 16_E4a_equal_budgets/budget_1s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 16_E4a_equal_budgets/budget_1s/tables/seed_variability.csv | Variability over seeds (per-instance standard deviation and range) |
| table | 16_E4a_equal_budgets/budget_1s/tables/summary.csv | E4a_equal_budgets, budget 1 s: gap_lb (per-instance mean over seeds) |
| table | 16_E4a_equal_budgets/budget_1s/tables/time_to_target_and_primal_integral.csv | Time to targets (median s; inf = not reached), share of runs reaching each target (%), mean primal integral (normalized by the budget) |
| figure | 16_E4a_equal_budgets/gurobi_status_and_bounds/figures/incumbent_and_bound_example_0.png | Incumbents (solid) and dual bounds (dashed), large_omega_n1000_T96_000 |
| figure | 16_E4a_equal_budgets/gurobi_status_and_bounds/figures/incumbent_and_bound_example_1.png | Incumbents (solid) and dual bounds (dashed), large_omega_n1000_T96_001 |
| figure | 16_E4a_equal_budgets/gurobi_status_and_bounds/figures/incumbent_and_bound_example_2.png | Incumbents (solid) and dual bounds (dashed), large_omega_n1000_T96_002 |
| table | 16_E4a_equal_budgets/gurobi_status_and_bounds/tables/by_model_budget_family_size.csv | Gurobi per model, budget, family and size: proven optima, MIP gap reported by Gurobi (incumbent vs its own bound), gap to LB*, and its dual bound relative to our certified LB (negative: our certificate is stronger) |
| table | 16_E4a_equal_budgets/gurobi_status_and_bounds/tables/per_instance_bounds_and_gaps.csv | Per instance: Gurobi incumbent, dual bound, MIP gap, status (Minor comment 1) |
| table | 16_E4a_equal_budgets/gurobi_status_and_bounds/tables/termination_status.csv | Gurobi termination status |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/anytime_median_gap_all.png | Median (IQR band) gap to LB* over time, all; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/anytime_median_gap_omega.png | Median (IQR band) gap to LB* over time, omega; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/anytime_median_gap_overnight.png | Median (IQR band) gap to LB* over time, overnight; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/anytime_median_gap_staggered.png | Median (IQR band) gap to LB* over time, staggered; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/gurobi_dual_bound_over_time.png | Median distance of Gurobi's dual bound below the best known lower bound over time (0 = as strong as LB*) |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 17_E4b_equal_budgets_60s/budget_60s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 17_E4b_equal_budgets_60s/budget_60s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 17_E4b_equal_budgets_60s/budget_60s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 17_E4b_equal_budgets_60s/budget_60s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 17_E4b_equal_budgets_60s/budget_60s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 17_E4b_equal_budgets_60s/budget_60s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 17_E4b_equal_budgets_60s/budget_60s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 17_E4b_equal_budgets_60s/budget_60s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 36 pairs in the files, the 32 most significant of the 32 significant ones shown |
| table | 17_E4b_equal_budgets_60s/budget_60s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 17_E4b_equal_budgets_60s/budget_60s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 17_E4b_equal_budgets_60s/budget_60s/tables/charged_time.csv | Charged time (s) |
| table | 17_E4b_equal_budgets_60s/budget_60s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 17_E4b_equal_budgets_60s/budget_60s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 17_E4b_equal_budgets_60s/budget_60s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 17_E4b_equal_budgets_60s/budget_60s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 17_E4b_equal_budgets_60s/budget_60s/tables/seed_variability.csv | Variability over seeds (per-instance standard deviation and range) |
| table | 17_E4b_equal_budgets_60s/budget_60s/tables/summary.csv | E4b_equal_budgets_60s, budget 60 s: gap_lb (per-instance mean over seeds) |
| table | 17_E4b_equal_budgets_60s/budget_60s/tables/time_to_target_and_primal_integral.csv | Time to targets (median s; inf = not reached), share of runs reaching each target (%), mean primal integral (normalized by the budget) |
| figure | 17_E4b_equal_budgets_60s/gurobi_status_and_bounds/figures/incumbent_and_bound_example_0.png | Incumbents (solid) and dual bounds (dashed), large_omega_n1000_T96_000 |
| figure | 17_E4b_equal_budgets_60s/gurobi_status_and_bounds/figures/incumbent_and_bound_example_1.png | Incumbents (solid) and dual bounds (dashed), large_omega_n1000_T96_001 |
| figure | 17_E4b_equal_budgets_60s/gurobi_status_and_bounds/figures/incumbent_and_bound_example_2.png | Incumbents (solid) and dual bounds (dashed), large_omega_n1000_T96_002 |
| table | 17_E4b_equal_budgets_60s/gurobi_status_and_bounds/tables/by_model_budget_family_size.csv | Gurobi per model, budget, family and size: proven optima, MIP gap reported by Gurobi (incumbent vs its own bound), gap to LB*, and its dual bound relative to our certified LB (negative: our certificate is stronger) |
| table | 17_E4b_equal_budgets_60s/gurobi_status_and_bounds/tables/per_instance_bounds_and_gaps.csv | Per instance: Gurobi incumbent, dual bound, MIP gap, status (Minor comment 1) |
| table | 17_E4b_equal_budgets_60s/gurobi_status_and_bounds/tables/termination_status.csv | Gurobi termination status |
| figure | 18_E3_long_runs/budget_600s/figures/anytime_median_gap_all.png | Median (IQR band) gap to LB* over time, all; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 18_E3_long_runs/budget_600s/figures/anytime_median_gap_omega.png | Median (IQR band) gap to LB* over time, omega; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 18_E3_long_runs/budget_600s/figures/anytime_median_gap_overnight.png | Median (IQR band) gap to LB* over time, overnight; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 18_E3_long_runs/budget_600s/figures/anytime_median_gap_staggered.png | Median (IQR band) gap to LB* over time, staggered; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 18_E3_long_runs/budget_600s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 18_E3_long_runs/budget_600s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 18_E3_long_runs/budget_600s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 18_E3_long_runs/budget_600s/figures/gurobi_dual_bound_over_time.png | Median distance of Gurobi's dual bound below the best known lower bound over time (0 = as strong as LB*) |
| figure | 18_E3_long_runs/budget_600s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 18_E3_long_runs/budget_600s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 18_E3_long_runs/budget_600s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 18_E3_long_runs/budget_600s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 18_E3_long_runs/budget_600s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 18_E3_long_runs/budget_600s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 18_E3_long_runs/budget_600s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 18_E3_long_runs/budget_600s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 18_E3_long_runs/budget_600s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 6 pairs in the files, the 5 most significant of the 5 significant ones shown |
| table | 18_E3_long_runs/budget_600s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 18_E3_long_runs/budget_600s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 18_E3_long_runs/budget_600s/tables/charged_time.csv | Charged time (s) |
| table | 18_E3_long_runs/budget_600s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 18_E3_long_runs/budget_600s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 18_E3_long_runs/budget_600s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 18_E3_long_runs/budget_600s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 18_E3_long_runs/budget_600s/tables/summary.csv | E3_long_runs, budget 600 s: gap_lb (per-instance mean over seeds) |
| table | 18_E3_long_runs/budget_600s/tables/time_to_target_and_primal_integral.csv | Time to targets (median s; inf = not reached), share of runs reaching each target (%), mean primal integral (normalized by the budget) |
| figure | 18_E3_long_runs/gurobi_status_and_bounds/figures/incumbent_and_bound_example_0.png | Incumbents (solid) and dual bounds (dashed), large_omega_n1000_T96_000 |
| figure | 18_E3_long_runs/gurobi_status_and_bounds/figures/incumbent_and_bound_example_1.png | Incumbents (solid) and dual bounds (dashed), large_omega_n2000_T96_000 |
| figure | 18_E3_long_runs/gurobi_status_and_bounds/figures/incumbent_and_bound_example_2.png | Incumbents (solid) and dual bounds (dashed), large_omega_n500_T96_000 |
| figure | 18_E3_long_runs/gurobi_status_and_bounds/figures/incumbent_and_bound_example_3.png | Incumbents (solid) and dual bounds (dashed), large_overnight_n1000_T96_000 |
| figure | 18_E3_long_runs/gurobi_status_and_bounds/figures/incumbent_and_bound_example_4.png | Incumbents (solid) and dual bounds (dashed), large_overnight_n2000_T96_000 |
| figure | 18_E3_long_runs/gurobi_status_and_bounds/figures/incumbent_and_bound_example_5.png | Incumbents (solid) and dual bounds (dashed), large_overnight_n500_T96_000 |
| table | 18_E3_long_runs/gurobi_status_and_bounds/tables/by_model_budget_family_size.csv | Gurobi per model, budget, family and size: proven optima, MIP gap reported by Gurobi (incumbent vs its own bound), gap to LB*, and its dual bound relative to our certified LB (negative: our certificate is stronger) |
| table | 18_E3_long_runs/gurobi_status_and_bounds/tables/per_instance_bounds_and_gaps.csv | Per instance: Gurobi incumbent, dual bound, MIP gap, status (Minor comment 1) |
| table | 18_E3_long_runs/gurobi_status_and_bounds/tables/termination_status.csv | Gurobi termination status |
| figure | 19_E3x_long_runs_xlarge/budget_600s/figures/anytime_median_gap_all.png | Median (IQR band) gap to LB* over time, all; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 19_E3x_long_runs_xlarge/budget_600s/figures/anytime_median_gap_omega.png | Median (IQR band) gap to LB* over time, omega; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 19_E3x_long_runs_xlarge/budget_600s/figures/anytime_median_gap_overnight.png | Median (IQR band) gap to LB* over time, overnight; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 19_E3x_long_runs_xlarge/budget_600s/figures/anytime_median_gap_staggered.png | Median (IQR band) gap to LB* over time, staggered; the curve of a method starts when its first schedule exists (artifact time included) |
| figure | 19_E3x_long_runs_xlarge/budget_600s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 19_E3x_long_runs_xlarge/budget_600s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 19_E3x_long_runs_xlarge/budget_600s/figures/gurobi_dual_bound_over_time.png | Median distance of Gurobi's dual bound below the best known lower bound over time (0 = as strong as LB*) |
| figure | 19_E3x_long_runs_xlarge/budget_600s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 19_E3x_long_runs_xlarge/budget_600s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 19_E3x_long_runs_xlarge/budget_600s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 19_E3x_long_runs_xlarge/budget_600s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 19_E3x_long_runs_xlarge/budget_600s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 19_E3x_long_runs_xlarge/budget_600s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 19_E3x_long_runs_xlarge/budget_600s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 19_E3x_long_runs_xlarge/budget_600s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 19_E3x_long_runs_xlarge/budget_600s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 6 pairs in the files, the 0 most significant of the 0 significant ones shown |
| table | 19_E3x_long_runs_xlarge/budget_600s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 19_E3x_long_runs_xlarge/budget_600s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 19_E3x_long_runs_xlarge/budget_600s/tables/charged_time.csv | Charged time (s) |
| table | 19_E3x_long_runs_xlarge/budget_600s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 19_E3x_long_runs_xlarge/budget_600s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 19_E3x_long_runs_xlarge/budget_600s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 19_E3x_long_runs_xlarge/budget_600s/tables/summary.csv | E3x_long_runs_xlarge, budget 600 s: gap_lb (per-instance mean over seeds) |
| table | 19_E3x_long_runs_xlarge/budget_600s/tables/time_to_target_and_primal_integral.csv | Time to targets (median s; inf = not reached), share of runs reaching each target (%), mean primal integral (normalized by the budget) |
| figure | 19_E3x_long_runs_xlarge/gurobi_status_and_bounds/figures/incumbent_and_bound_example_0.png | Incumbents (solid) and dual bounds (dashed), xlarge_omega_n10000_T96_000 |
| figure | 19_E3x_long_runs_xlarge/gurobi_status_and_bounds/figures/incumbent_and_bound_example_1.png | Incumbents (solid) and dual bounds (dashed), xlarge_omega_n5000_T96_000 |
| figure | 19_E3x_long_runs_xlarge/gurobi_status_and_bounds/figures/incumbent_and_bound_example_2.png | Incumbents (solid) and dual bounds (dashed), xlarge_overnight_n5000_T96_000 |
| figure | 19_E3x_long_runs_xlarge/gurobi_status_and_bounds/figures/incumbent_and_bound_example_3.png | Incumbents (solid) and dual bounds (dashed), xlarge_staggered_n10000_T288_000 |
| figure | 19_E3x_long_runs_xlarge/gurobi_status_and_bounds/figures/incumbent_and_bound_example_4.png | Incumbents (solid) and dual bounds (dashed), xlarge_staggered_n5000_T288_000 |
| table | 19_E3x_long_runs_xlarge/gurobi_status_and_bounds/tables/by_model_budget_family_size.csv | Gurobi per model, budget, family and size: proven optima, MIP gap reported by Gurobi (incumbent vs its own bound), gap to LB*, and its dual bound relative to our certified LB (negative: our certificate is stronger) |
| table | 19_E3x_long_runs_xlarge/gurobi_status_and_bounds/tables/per_instance_bounds_and_gaps.csv | Per instance: Gurobi incumbent, dual bound, MIP gap, status (Minor comment 1) |
| table | 19_E3x_long_runs_xlarge/gurobi_status_and_bounds/tables/termination_status.csv | Gurobi termination status |
| figure | 20_E5_ablation/budget_10s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 20_E5_ablation/budget_10s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 20_E5_ablation/budget_10s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 20_E5_ablation/budget_10s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 20_E5_ablation/budget_10s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 20_E5_ablation/budget_10s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 20_E5_ablation/budget_10s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 20_E5_ablation/budget_10s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 20_E5_ablation/budget_10s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 20_E5_ablation/budget_10s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 20_E5_ablation/budget_10s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 20_E5_ablation/budget_10s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 136 pairs in the files, the 40 most significant of the 96 significant ones shown |
| table | 20_E5_ablation/budget_10s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 20_E5_ablation/budget_10s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 20_E5_ablation/budget_10s/tables/charged_time.csv | Charged time (s) |
| table | 20_E5_ablation/budget_10s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 20_E5_ablation/budget_10s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 20_E5_ablation/budget_10s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 20_E5_ablation/budget_10s/tables/seed_variability.csv | Variability over seeds (per-instance standard deviation and range) |
| table | 20_E5_ablation/budget_10s/tables/summary.csv | E5_ablation, budget 10 s: gap_lb (per-instance mean over seeds) |
| figure | 21_E5b_ablation_60s/budget_60s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 21_E5b_ablation_60s/budget_60s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 21_E5b_ablation_60s/budget_60s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 21_E5b_ablation_60s/budget_60s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 21_E5b_ablation_60s/budget_60s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 21_E5b_ablation_60s/budget_60s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 21_E5b_ablation_60s/budget_60s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 21_E5b_ablation_60s/budget_60s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 21_E5b_ablation_60s/budget_60s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 21_E5b_ablation_60s/budget_60s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 21_E5b_ablation_60s/budget_60s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 21_E5b_ablation_60s/budget_60s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 6 pairs in the files, the 5 most significant of the 5 significant ones shown |
| table | 21_E5b_ablation_60s/budget_60s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 21_E5b_ablation_60s/budget_60s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 21_E5b_ablation_60s/budget_60s/tables/charged_time.csv | Charged time (s) |
| table | 21_E5b_ablation_60s/budget_60s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 21_E5b_ablation_60s/budget_60s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 21_E5b_ablation_60s/budget_60s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 21_E5b_ablation_60s/budget_60s/tables/summary.csv | E5b_ablation_60s, budget 60 s: gap_lb (per-instance mean over seeds) |
| figure | 22_E6_scalability/budget_120s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 22_E6_scalability/budget_120s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 22_E6_scalability/budget_120s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 22_E6_scalability/budget_120s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 22_E6_scalability/budget_120s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 22_E6_scalability/budget_120s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 22_E6_scalability/budget_120s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 22_E6_scalability/budget_120s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 22_E6_scalability/budget_120s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 22_E6_scalability/budget_120s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 22_E6_scalability/budget_120s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 22_E6_scalability/budget_120s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 55 pairs in the files, the 0 most significant of the 0 significant ones shown |
| table | 22_E6_scalability/budget_120s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 22_E6_scalability/budget_120s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 22_E6_scalability/budget_120s/tables/charged_time.csv | Charged time (s) |
| table | 22_E6_scalability/budget_120s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 22_E6_scalability/budget_120s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 22_E6_scalability/budget_120s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 22_E6_scalability/budget_120s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 22_E6_scalability/budget_120s/tables/summary.csv | E6_scalability, budget 120 s: gap_lb (per-instance mean over seeds) |
| figure | 22_E6_scalability/gurobi_status_and_bounds/figures/incumbent_and_bound_example_0.png | Incumbents (solid) and dual bounds (dashed), large_omega_n1000_T96_000 |
| figure | 22_E6_scalability/gurobi_status_and_bounds/figures/incumbent_and_bound_example_1.png | Incumbents (solid) and dual bounds (dashed), large_omega_n2000_T96_000 |
| figure | 22_E6_scalability/gurobi_status_and_bounds/figures/incumbent_and_bound_example_2.png | Incumbents (solid) and dual bounds (dashed), large_omega_n500_T96_000 |
| table | 22_E6_scalability/gurobi_status_and_bounds/tables/by_model_budget_family_size.csv | Gurobi per model, budget, family and size: proven optima, MIP gap reported by Gurobi (incumbent vs its own bound), gap to LB*, and its dual bound relative to our certified LB (negative: our certificate is stronger) |
| table | 22_E6_scalability/gurobi_status_and_bounds/tables/per_instance_bounds_and_gaps.csv | Per instance: Gurobi incumbent, dual bound, MIP gap, status (Minor comment 1) |
| table | 22_E6_scalability/gurobi_status_and_bounds/tables/termination_status.csv | Gurobi termination status |
| figure | 22_E6_scalability/scalability/figures/gap_vs_n.png | Median gap_lb against n |
| figure | 22_E6_scalability/scalability/figures/time_vs_n.png | Median time (IQR band) against n |
| table | 22_E6_scalability/scalability/tables/certify_costs_by_n.csv | Median Certify costs (s) by n |
| table | 22_E6_scalability/scalability/tables/median_gap_by_n.csv | Median gap_lb by n |
| table | 22_E6_scalability/scalability/tables/median_time_by_n.csv | Median charged time (s) by n |
| figure | 23_E7_gurobi_threads/across_budgets/figures/gap_vs_budget.png | Median gap_lb (IQR band) against the time budget: the time-quality trade-off of each method |
| table | 23_E7_gurobi_threads/across_budgets/tables/mean_charged_time_by_budget.csv | Mean charged time (s) at every budget |
| table | 23_E7_gurobi_threads/across_budgets/tables/mean_gap_by_budget.csv | Mean gap_lb (per-instance mean over seeds) of every method at every budget |
| figure | 23_E7_gurobi_threads/budget_10s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 23_E7_gurobi_threads/budget_10s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 23_E7_gurobi_threads/budget_10s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 23_E7_gurobi_threads/budget_10s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 23_E7_gurobi_threads/budget_10s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 23_E7_gurobi_threads/budget_10s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 23_E7_gurobi_threads/budget_10s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 23_E7_gurobi_threads/budget_10s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 23_E7_gurobi_threads/budget_10s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 23_E7_gurobi_threads/budget_10s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 23_E7_gurobi_threads/budget_10s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 23_E7_gurobi_threads/budget_10s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 3 pairs in the files, the 3 most significant of the 3 significant ones shown |
| table | 23_E7_gurobi_threads/budget_10s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 23_E7_gurobi_threads/budget_10s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 23_E7_gurobi_threads/budget_10s/tables/charged_time.csv | Charged time (s) |
| table | 23_E7_gurobi_threads/budget_10s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 23_E7_gurobi_threads/budget_10s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 23_E7_gurobi_threads/budget_10s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 23_E7_gurobi_threads/budget_10s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 23_E7_gurobi_threads/budget_10s/tables/summary.csv | E7_gurobi_threads, budget 10 s: gap_lb (per-instance mean over seeds) |
| figure | 23_E7_gurobi_threads/budget_60s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 23_E7_gurobi_threads/budget_60s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 23_E7_gurobi_threads/budget_60s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 23_E7_gurobi_threads/budget_60s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 23_E7_gurobi_threads/budget_60s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 23_E7_gurobi_threads/budget_60s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 23_E7_gurobi_threads/budget_60s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 23_E7_gurobi_threads/budget_60s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 23_E7_gurobi_threads/budget_60s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 23_E7_gurobi_threads/budget_60s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 23_E7_gurobi_threads/budget_60s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 23_E7_gurobi_threads/budget_60s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 3 pairs in the files, the 3 most significant of the 3 significant ones shown |
| table | 23_E7_gurobi_threads/budget_60s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 23_E7_gurobi_threads/budget_60s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 23_E7_gurobi_threads/budget_60s/tables/charged_time.csv | Charged time (s) |
| table | 23_E7_gurobi_threads/budget_60s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 23_E7_gurobi_threads/budget_60s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 23_E7_gurobi_threads/budget_60s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 23_E7_gurobi_threads/budget_60s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 23_E7_gurobi_threads/budget_60s/tables/summary.csv | E7_gurobi_threads, budget 60 s: gap_lb (per-instance mean over seeds) |
| figure | 23_E7_gurobi_threads/gurobi_status_and_bounds/figures/incumbent_and_bound_example_0.png | Incumbents (solid) and dual bounds (dashed), large_omega_n1000_T96_000 |
| figure | 23_E7_gurobi_threads/gurobi_status_and_bounds/figures/incumbent_and_bound_example_1.png | Incumbents (solid) and dual bounds (dashed), large_omega_n2000_T96_000 |
| figure | 23_E7_gurobi_threads/gurobi_status_and_bounds/figures/incumbent_and_bound_example_2.png | Incumbents (solid) and dual bounds (dashed), large_omega_n500_T96_000 |
| table | 23_E7_gurobi_threads/gurobi_status_and_bounds/tables/by_model_budget_family_size.csv | Gurobi per model, budget, family and size: proven optima, MIP gap reported by Gurobi (incumbent vs its own bound), gap to LB*, and its dual bound relative to our certified LB (negative: our certificate is stronger) |
| table | 23_E7_gurobi_threads/gurobi_status_and_bounds/tables/per_instance_bounds_and_gaps.csv | Per instance: Gurobi incumbent, dual bound, MIP gap, status (Minor comment 1) |
| table | 23_E7_gurobi_threads/gurobi_status_and_bounds/tables/termination_status.csv | Gurobi termination status |
| figure | 24_E9_managerial/managerial/figures/load_profile_example_0.png | Charging load over the day, large_omega_n1000_T96_000 |
| figure | 24_E9_managerial/managerial/figures/load_profile_example_1.png | Charging load over the day, large_omega_n1000_T96_001 |
| figure | 24_E9_managerial/managerial/figures/load_profile_example_2.png | Charging load over the day, large_omega_n1000_T96_002 |
| table | 24_E9_managerial/managerial/tables/mean_peak_by_family.csv | Mean peak (kW) by family |
| table | 24_E9_managerial/managerial/tables/peak_reduction_vs_reference_policies.csv | Peak reduction of CRI against the reference policies |
| figure | 25_E10a_state_of_the_art/budget_10s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 25_E10a_state_of_the_art/budget_10s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 25_E10a_state_of_the_art/budget_10s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 25_E10a_state_of_the_art/budget_10s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 25_E10a_state_of_the_art/budget_10s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 25_E10a_state_of_the_art/budget_10s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 25_E10a_state_of_the_art/budget_10s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 25_E10a_state_of_the_art/budget_10s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 25_E10a_state_of_the_art/budget_10s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 25_E10a_state_of_the_art/budget_10s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 25_E10a_state_of_the_art/budget_10s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 25_E10a_state_of_the_art/budget_10s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 78 pairs in the files, the 40 most significant of the 73 significant ones shown |
| table | 25_E10a_state_of_the_art/budget_10s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 25_E10a_state_of_the_art/budget_10s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 25_E10a_state_of_the_art/budget_10s/tables/charged_time.csv | Charged time (s) |
| table | 25_E10a_state_of_the_art/budget_10s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 25_E10a_state_of_the_art/budget_10s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 25_E10a_state_of_the_art/budget_10s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 25_E10a_state_of_the_art/budget_10s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 25_E10a_state_of_the_art/budget_10s/tables/seed_variability.csv | Variability over seeds (per-instance standard deviation and range) |
| table | 25_E10a_state_of_the_art/budget_10s/tables/summary.csv | E10a_state_of_the_art, budget 10 s: gap_lb (per-instance mean over seeds) |
| figure | 26_E10b_state_of_the_art_60s/budget_60s/figures/charged_time_boxplot.png | Distribution of the charged time per run |
| figure | 26_E10b_state_of_the_art_60s/budget_60s/figures/gap_boxplot.png | Distribution of the per-instance gap_lb |
| figure | 26_E10b_state_of_the_art_60s/budget_60s/figures/gap_vs_n.png | Mean gap_lb against the number of vehicles, per method |
| figure | 26_E10b_state_of_the_art_60s/budget_60s/figures/performance_profile.png | Dolan-More performance profile of the peak (per-instance mean) |
| figure | 26_E10b_state_of_the_art_60s/budget_60s/figures/quality_vs_time.png | Mean quality against mean charged time (one point per method) |
| table | 26_E10b_state_of_the_art_60s/budget_60s/statistics/CRI_vs_each_method.csv | CRI against every other method (wins = instances where the control is strictly better) |
| table | 26_E10b_state_of_the_art_60s/budget_60s/statistics/friedman_average_ranks.csv | Average ranks (1 = best) |
| table | 26_E10b_state_of_the_art_60s/budget_60s/statistics/friedman_iman_davenport_test.csv | Friedman test with the Iman-Davenport correction and the Nemenyi critical difference |
| table | 26_E10b_state_of_the_art_60s/budget_60s/statistics/friedman_ranks_by_family.csv | Average ranks by family, with the Friedman p-value of each family |
| figure | 26_E10b_state_of_the_art_60s/budget_60s/statistics/holm_pvalue_heatmap.png | Pairwise Holm-adjusted Wilcoxon p-values (* significant) |
| figure | 26_E10b_state_of_the_art_60s/budget_60s/statistics/nemenyi_critical_difference_diagram.png | Average ranks; methods joined by a bar are not significantly different (Nemenyi) |
| table | 26_E10b_state_of_the_art_60s/budget_60s/statistics/pairwise_wilcoxon_holm_effect_sizes.csv | Pairwise Wilcoxon signed-rank tests (Holm), sign test, effect sizes (negative delta: A better); 21 pairs in the files, the 18 most significant of the 18 significant ones shown |
| table | 26_E10b_state_of_the_art_60s/budget_60s/statistics/win_matrix.csv | Win matrix: entry (row, column) = instances where the row method is strictly better than the column method |
| table | 26_E10b_state_of_the_art_60s/budget_60s/tables/all_quality_measures.csv | All quality measures (means over instances): gap to the best lower bound LB*, to the best known value, to the proven optimum, to our own certified lower bound, to the LP bound, relative difference to the exact solver's incumbent; instances proved optimal by our certificate alone and by the method's own bound |
| table | 26_E10b_state_of_the_art_60s/budget_60s/tables/charged_time.csv | Charged time (s) |
| table | 26_E10b_state_of_the_art_60s/budget_60s/tables/mean_gap_by_family.csv | Mean gap_lb by family |
| table | 26_E10b_state_of_the_art_60s/budget_60s/tables/mean_gap_by_n.csv | Mean gap_lb by n |
| table | 26_E10b_state_of_the_art_60s/budget_60s/tables/mean_gap_by_size_class.csv | Mean gap_lb by size class |
| table | 26_E10b_state_of_the_art_60s/budget_60s/tables/per_instance_mean_peak.csv | Per-instance mean peak (kW) of every method |
| table | 26_E10b_state_of_the_art_60s/budget_60s/tables/seed_variability.csv | Variability over seeds (per-instance standard deviation and range) |
| table | 26_E10b_state_of_the_art_60s/budget_60s/tables/summary.csv | E10b_state_of_the_art_60s, budget 60 s: gap_lb (per-instance mean over seeds) |
| figure | 30_budget_ladders/equal_budgets_1s_to_600s/figures/gap_vs_budget.png | Median gap_lb (IQR band) against the time budget: the time-quality trade-off of each method |
| table | 30_budget_ladders/equal_budgets_1s_to_600s/tables/mean_charged_time_by_budget.csv | Mean charged time (s) at every budget |
| table | 30_budget_ladders/equal_budgets_1s_to_600s/tables/mean_gap_by_budget.csv | Mean gap_lb (per-instance mean over seeds) of every method at every budget |
| figure | 30_budget_ladders/state_of_the_art_10s_to_60s/figures/gap_vs_budget.png | Median gap_lb (IQR band) against the time budget: the time-quality trade-off of each method |
| table | 30_budget_ladders/state_of_the_art_10s_to_60s/tables/mean_charged_time_by_budget.csv | Mean charged time (s) at every budget |
| table | 30_budget_ladders/state_of_the_art_10s_to_60s/tables/mean_gap_by_budget.csv | Mean gap_lb (per-instance mean over seeds) of every method at every budget |
