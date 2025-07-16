from Models.modelS import ModelS
import time
from Algorithms.utils import calculate_expected_profit, solve_deterministic_knapsack

def iterative_algorithm_p(n_items, capacity, weights, profits, survival_probs, mt):
    best_heu_sol = None
    best_heu_val = 0
    last_exact_probability = 1
    j = 0
    start_time = time.time()
    previous_solutions = []
    is_heuristic = True

    model = ModelS(j=0, n=n_items, c=capacity, w=weights, p=profits, q=survival_probs,
                   best_heu_value=best_heu_val, last_exact_probability=last_exact_probability,
                   previous_solutions=previous_solutions, ml=1)

    while (time.time() - start_time) < mt:
        optimality, x, obj_value = model.optimize()

        if optimality:
            last_exact_probability = obj_value
        else:
            is_heuristic = False
            break

        y = solve_deterministic_knapsack(x, weights, profits, capacity, survival_probs)
        z = [(x_i or y_i) for x_i,y_i in zip(x,y)]

        val = calculate_expected_profit(z, profits, survival_probs)
        if val > best_heu_val:
            best_heu_sol = z
            best_heu_val = val
        previous_solutions.append(x)
        j+=1
        model = ModelS(j=j, n=n_items, c=capacity, w=weights, p=profits, q=survival_probs,
               best_heu_value=best_heu_val, last_exact_probability=last_exact_probability,
               previous_solutions=previous_solutions, ml=1)
    return best_heu_sol, best_heu_val, "exact" if not is_heuristic else "heuristic", j , (time.time() - start_time)