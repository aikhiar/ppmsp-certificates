# Report folders

Open `report.html` (or `report.md`) first; `index.md` lists every table and figure with its caption. Inside each folder: `tables/` (.csv .md .tex), `statistics/` (tests, ranks, effect sizes and their diagrams) and `figures/` (.png .pdf).

| folder | content | subfolders |
|---|---|---|
| `00_campaign_overview/` | campaign status, machines, method library, default and tuned parameters, headline results of every block |  |
| `01_instances/` | instance sets and their features |  |
| `02_exact_references_and_bounds/` | exact references (proven optima, dual bounds) and the cost of the Certify artifacts |  |
| `03_validity_checks/` | feasibility of every schedule, a priori guarantees, certified lower bounds, budgets, abnormal runs |  |
| `04_faithfulness_of_earlier_methods/` | the original code of the earlier methods against their re-implementation |  |
| `05_theory_verification/` | numerical verification of every statement of Sections 3-4 (theory/verify_theory.py) |  |
| `10_E0_sanity/` | Every method once on a few small instances (feasibility, statuses, timing). | `budget_5s/` |
| `11_E1_certificates/` | Every lower and upper certificate (Sections 3-4) against the optimum or the best known value; validity, tightness, cost, instances proved optimal a priori. | `certificates/` |
| `12_E8a_tuning_faithful/` | Faithful tuning of the earlier SA (and, through tuned_as, of its hybrids) with its original grid (243 points, iteration mode), on the separate tuning set (never on evaluation instances). | `tuning/` |
| `13_E8b_tuning_budget/` | Tuning of the budget-mode methods (SA-b and the SA-b hybrids, LLS, W-LNS) at 10 s on the separate tuning set; the chosen LLS and W-LNS values become the class defaults (used inside CRI). | `tuning/` |
| `14_E2_head_to_head/` | Earlier methods in their original form (each method's own stopping rule) against their certified counterparts, namely RR vs MT, RLP vs CE and IR, G vs CE, and SA vs its hybrids. | `head_to_head/`, `single_run/` |
| `15_E2b_head_to_head_budgets/` | The same pairs at equal budgets (1 s and 10 s), where the earlier methods use the whole budget (restarts, more trials, more iterations); MT repeats with new seeds. | `across_budgets/`, `budget_10s/`, `budget_1s/`, `head_to_head/` |
| `16_E4a_equal_budgets/` | Every method and Gurobi (standard and aggregated models, one thread each) at the same wall-clock budgets of 1 s and 10 s. | `across_budgets/`, `budget_10s/`, `budget_1s/`, `gurobi_status_and_bounds/` |
| `17_E4b_equal_budgets_60s/` | The anytime methods and Gurobi at 60 s; anytime curves over the whole run. | `budget_60s/`, `gurobi_status_and_bounds/` |
| `18_E3_long_runs/` | Long runs (600 s) of CRI and Gurobi, one instance per family and size of the medium and large sets; anytime curves and dual bounds. | `budget_600s/`, `gurobi_status_and_bounds/` |
| `19_E3x_long_runs_xlarge/` | Long runs (600 s) of CRI and Gurobi on the xlarge instances (n = 5,000-10,000, T up to 288), where Gurobi struggles, with objective-versus-runtime curves and dual bounds at full length (E6 stops at 120 s). Own block so that its memory need does not reduce the workers of E3. | `budget_600s/`, `gurobi_status_and_bounds/` |
| `20_E5_ablation/` | Contribution of each CRI component (Round only, + LLS, + W-LNS, + SA, both); marginal matrix (LP, cover cuts, configuration LP); rounding family (CE, MT, IR, greedy); SA initialisation (the former hybrids are SA started from G, RR, RLP or the CRI Round stage). | `budget_10s/` |
| `21_E5b_ablation_60s/` | The improvement-stage ablation at 60 s. | `budget_60s/` |
| `22_E6_scalability/` | Scaling up to n = 10,000 vehicles and T = 288 slots, with the time of the Certify stage and of each method and the gap to the certified lower bound. Workers sized automatically from the free RAM (8 GB per worker for these models). | `budget_120s/`, `gurobi_status_and_bounds/`, `scalability/` |
| `23_E7_gurobi_threads/` | Gurobi with 4 threads against single-thread CRI at 10 s and 60 s. Workers sized automatically, 4 cores each (physical cores - 1, divided by 4), so that Gurobi has its threads. | `across_budgets/`, `budget_10s/`, `budget_60s/`, `gurobi_status_and_bounds/` |
| `24_E9_managerial/` | Peak reduction against uncontrolled charging (ASAP) and non-preemptive charging (GNP); load profiles. | `managerial/` |
| `25_E10a_state_of_the_art/` | Baselines from the literature at 10 s, namely NFDH (Ranjan et al. 2014), the heuristic and the ILS of Zaidi et al. (EJOR 2024; as published and restarted until the budget), the online alpha-policy of Hunsaker et al. (2003), the branch and bound of Afshar-Nadjafi et al. (2013), the hybrid metaheuristics of Aristotelous and Nearchou (2024; SER and PAR with LS2, and SER with their leveling objective), the classical Burgess-Killebrew leveling; against CRI and Gurobi (runs reused from E4a). | `budget_10s/` |
| `26_E10b_state_of_the_art_60s/` | The anytime state-of-the-art baselines at 60 s, against CRI and Gurobi (runs reused from E4b). | `budget_60s/` |
| `30_budget_ladders/` | time-quality ladders across blocks: every method at every budget from the shortest to the longest runs, on common instances | `equal_budgets_1s_to_600s/`, `state_of_the_art_10s_to_60s/` |

**Subfolders of a block**

| subfolder | content |
|---|---|
| `budget_<B>s/`, `single_run/` | comparison at one budget: tables/ (summary with 95% CIs, breakdowns by family, size and n, charged time, all quality measures, seed variability, per-instance peaks, time to target), statistics/ (Friedman and Iman-Davenport test, average ranks overall and by family, Nemenyi critical difference diagram, pairwise Wilcoxon signed-rank tests with Holm correction, sign test, Cliff's delta and Vargha-Delaney A12, p-value heatmap, win matrix, control against each method), figures/ (performance profile, gap and time box plots, quality against time, gap against n, anytime curves, Gurobi dual bound over time) |
| `certificates/` | every lower and upper certificate against the optimum or best known value |
| `head_to_head/` | the pairs of the block (earlier method against its certified counterpart) |
| `scalability/` | charged time, gap and Certify costs against n |
| `gurobi_status_and_bounds/` | Gurobi: termination status, proven optima, MIP gaps, dual bounds, per-instance table, incumbent and bound over time |
| `tuning/` | the tuning grid of each method and the marginal effect of each parameter |
| `managerial/` | peak reduction against uncontrolled and non-preemptive charging, load profiles |
| `across_budgets/` | every method at every budget of the block: mean gap and charged time by budget, gap against the budget (does a longer run improve the solution?) |
