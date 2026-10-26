| result | statement | tests | failures | detail |
|---|---|---|---|---|
| Prop 3.1 | P_LP <= P* | 44 | 0 | n/a |
| Prop 3.2 | PPMSP with p_i=1, common window = P\|\|Cmax (brute force) | 30 | 0 | n/a |
| Thm 3.3 | aggregated MILP = binary MILP; recovered schedule integral, feasible, optimal | 42 | 0 | n/a |
| Cor 3.4 | single power class: P* = w ceil(P_LP / w) | 48 | 0 | n/a |
| Lem 4.2 | systematic sampling: exact sizes, exact marginals (outcome law), sampler frequencies | 459 | 0 | max \|z\| = 2.95 |
| Lem 4.3 | exact slot laws vs Monte Carlo | 180 | 0 | max \|z\| = 3.00 |
| Lem 4.6 | sub-Gaussian proxy valid on the grid and optimal (sup_lambda 2 psi / lambda^2 = sigma^2) | 199 | 0 | max relative gap to optimality 2.3e-07 |
| Lem 4.8 | independence across components and of non-adjacent slots (correlation z-tests) | 3318 | 0 | max \|z\| independent pairs 3.26; max \|z\| adjacent pairs 141.4 (detection check) |
| Lem 4.9 | LP vertex: \|J\| <= \|T=\| - 1 and sum_t \|V_t\| <= 2\|T=\| - 2 | 60 | 0 | n/a |
| Lem 4.10 | LP vertex: every component of the fractional support has #edges <= #vertices | 60 | 0 | n/a |
| Thm 4.11 | closed forms (a), (b), (c) x (sub-Gaussian, Bernstein) >= P* at 5 matrices | 1122 | 0 | n/a |
| Cor 4.12 | distribution-free forms >= localized forms (same alpha) and >= P* | 748 | 0 | n/a |
| Rem 4.13 | local lemma closed form beats union bound iff e d_alpha < m_alpha | 187 | 0 | n/a |
| Eq (22) | P* - P_LP <= w_max sqrt(k* ln T / 2) | 44 | 0 | n/a |
| Thm 4.14 | union, componentwise, LLL certificates >= P*; U_Gamma <= U_union | 176 | 0 | n/a |
| Thm 4.14 | least fixed point of the LLL iteration satisfies condition (iii) | 176 | 0 | n/a |
| Thm 4.14 | success probability bound <= Monte Carlo success frequency | 88 | 0 | n/a |
| Thm 4.15 | P* <= E[max] (MC) <= U_EGamma <= U_E | 80 | 0 | n/a |
| Thm 4.15 | U_E = min_u {u + sum_t E[(S_t - u)^+]} (identity, exact) | 80 | 0 | n/a |
| Thm 4.17 | dependent-rounding certificates and class ceiling >= P* | 60 | 0 | n/a |
| Thm 4.17 | dependent rounding meets u with probability >= 1 - sum_t P(S~_t > u) (MC) | 60 | 0 | n/a |
| Thm 4.18 | P* <= U_R <= U_exists <= U_Gamma, U_LLL;  U_exists <= E[max] <= U_EGamma | 127 | 0 | n/a |
| Thm 4.18 | optimal rounding by dynamic programming = brute-force optimal rounding | 57 | 0 | n/a |
| Thm 4.18 | exact P(max <= u) and exact E[max] vs Monte Carlo | 304 | 0 | max \|z\| probability 3.04, expectation 2.33 |
| Thm 4.19 | every load-feasible slot configuration satisfies every cover inequality (brute force) | 12749740 | 0 | n/a |
| Thm 4.19 | max(ceil P_LP, w_max) <= LB_cut <= P* | 44 | 0 | n/a |
| Thm 4.19 | feasibility of the cut LP is monotone in the level P | 44 | 0 | n/a |
| Rem (Sec 4.6) | P\|\|Cmax special case: LB_cut >= max_k (w_(kT-k+1) + ... + w_(kT+1)) | 25 | 0 | n/a |
| Thm 4.20 | LB_cut <= LB_conf <= P* | 44 | 0 | n/a |
| Thm 4.20 | column generation decides feasibility exactly (vs explicit enumeration of configurations) | 97 | 0 | n/a |
| Thm 4.21 | iterative rounding: rule applies, schedule feasible, peak <= P_LP + w_max, #LP within bound | 44 | 0 | n/a |
| Ex 4.22 | P_LP = L + w/2, P* = L + w, LB_cut = P* on the gap family | 3 | 0 | n/a |
| Thm 4.23 | LB_conf <= P* <= U (rounded) | 44 | 0 | n/a |
| Cor 4.24 | U / P_LP <= 1 + min(w_max, w_max sqrt(k* ln T / 2)) / P_LP; trend with n at fixed T | 12 | 0 | overnight n=50: U/P_LP = 1.1317 (bound 1.2201); overnight n=100: U/P_LP = 1.0822 (bound 1.1071); overnight n=200: U/P_LP = 1.0557 (bound 1.0668); overnight n=400: U/P_LP = 1.0209 (bound 1.0282); overnight n=800: U/P_LP = 1.0097 (bound 1.0145); overnight n=1600: U/P_LP = 1.0059 (bound 1.0070); staggered n=50: U/P_LP = 1.1707 (bound 1.4293); staggered n=100: U/P_LP = 1.0923 (bound 1.2435); staggered n=200: U/P_LP = 1.0739 (bound 1.1392); staggered n=400: U/P_LP = 1.0498 (bound 1.0763); staggered n=800: U/P_LP = 1.0265 (bound 1.0363); staggered n=1600: U/P_LP = 1.0142 (bound 1.0190) |
| Thm 4.25(a) | Moser-Tardos: peak <= u, mean resamplings <= sum xi/(1-xi) (+3 SE) | 80 | 0 | n/a |
| Thm 4.25(b) | conditional expectations: peaks within their guarantees | 80 | 0 | n/a |
| Thm 4.25(c) | repeated dependent rounding: mean rounds <= 1/(1 - sum_t P(S~_t > u)) (+3 SE) | 80 | 0 | n/a |
