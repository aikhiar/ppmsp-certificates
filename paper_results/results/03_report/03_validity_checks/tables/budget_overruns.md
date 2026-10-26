| experiment | method | budget | runs | worst | mean | n | improved_after_budget | no_schedule_by_budget | evaluated_at_budget | reason |
|---|---|---|---|---|---|---|---|---|---|---|
| E2b_head_to_head_budgets | CE-conf-comp | 1.00 | 24 | 18.92 | 5.90 | 50-200 | 24 | 24 | 0 | single-shot method: its certificate artifacts alone exceed the budget |
| E2b_head_to_head_budgets | CE-conf-comp | 10.00 | 5 | 1.89 | 1.55 | 100-100 | 5 | 5 | 0 | single-shot method: its certificate artifacts alone exceed the budget |
| E2b_head_to_head_budgets | IR | 1.00 | 5 | 1.47 | 1.39 | 200-200 | 5 | 5 | 0 | single-shot method: its certificate artifacts alone exceed the budget |
| E2b_head_to_head_budgets | MT-lp-b | 1.00 | 3 | 1.48 | 1.47 | 10-10 | 0 | 0 | 0 | single-shot method: its certificate artifacts alone exceed the budget |
| E4a_equal_budgets | CRI | 1.00 | 2 | 1.17 | 1.16 | 1000-2000 | 0 | 0 | 2 | 2 run(s) improved only after the budget: evaluated at the budget, the later improvements are not counted; the others gained nothing after the budget |
| E4a_equal_budgets | GUROBI-agg | 1.00 | 24 | 3.05 | 1.64 | 200-2000 | 0 | 0 | 0 | no improvement after the budget (anytime trace): the extra time changed no result |
| E4a_equal_budgets | GUROBI-agg | 10.00 | 6 | 1.23 | 1.16 | 1000-2000 | 0 | 0 | 0 | no improvement after the budget (anytime trace): the extra time changed no result |
| E4a_equal_budgets | GUROBI-std | 1.00 | 6 | 1.36 | 1.27 | 1000-2000 | 0 | 0 | 0 | no improvement after the budget (anytime trace): the extra time changed no result |
| E4a_equal_budgets | HSC-b | 1.00 | 9 | 1.23 | 1.20 | 40-200 | 0 | 0 | 0 | no improvement after the budget (anytime trace): the extra time changed no result |
| E4a_equal_budgets | LLS | 1.00 | 2 | 1.22 | 1.19 | 2000-2000 | 0 | 0 | 0 | no improvement after the budget (anytime trace): the extra time changed no result |
| E4a_equal_budgets | RLP-b | 1.00 | 30 | 2.89 | 1.92 | 500-2000 | 30 | 30 | 0 | its LP relaxation is solved once before the first rounding trial; on n >= 500 that LP alone takes 1.5-2.9 s, longer than the 1 s budget |
| E4a_equal_budgets | WLNS | 1.00 | 10 | 1.41 | 1.26 | 1000-2000 | 0 | 0 | 2 | 2 run(s) improved only after the budget: evaluated at the budget, the later improvements are not counted; the others gained nothing after the budget |
| E7_gurobi_threads | GUROBI-agg-4t | 10.00 | 2 | 1.19 | 1.15 | 1000-2000 | 0 | 0 | 0 | no improvement after the budget (anytime trace): the extra time changed no result |
