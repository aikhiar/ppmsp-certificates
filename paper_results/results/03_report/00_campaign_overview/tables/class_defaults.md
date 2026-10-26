| class | defaults |
|---|---|
| G | {"mode": "single"} |
| RR | {"N": 10000, "chunk": 2000, "stop": "iterations"} |
| RLP | {"stop": "trials", "trials": 50} |
| SA | {"L": 50, "N": 10000, "T0": 100.0, "Tmin": 0.01, "alpha_c": 0.95, "alpha_p": 0.3, "chunk": 5000, "eps": 0.0, "stop": "iterations"} |
| CE | {"passes": 3} |
| MT | {"max_steps": 1000000, "mode": "single"} |
| LLS | {"chunk": 20, "kick_size": 3, "max_checks": 200000} |
| WLNS | {"adaptive": true, "min_width": 6, "sub_time_limit": 2.0, "threads": 1, "width": 12} |
| CRI | {"complete": false, "complete_model": "aggregated", "complete_share": 0.25, "improve_slice": 5.0, "threads": 1} |
| GUROBI | {"model": "standard", "threads": 1} |
