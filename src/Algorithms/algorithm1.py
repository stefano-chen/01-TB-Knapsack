from Models.modelP import ModelP
import time
from Algorithms.utils import calculate_expected_profit

def iterative_algorithm_p(n_items, capacity, weights, profits, survival_probs, mt):
    best_heu_sol = None
    best_heu_val = 0
    last_exact_profit = 2.220446049250313e+16
    j = 0
    start_time = time.time()
    previous_solutions = []
    ub = float("+inf")

    model = ModelP(j=0, n=n_items, c=capacity, w=weights, p=profits, q=survival_probs,
                   best_heu_value=best_heu_val, last_exact_profit=last_exact_profit,
                   previous_solutions=previous_solutions, ml=1)

    while best_heu_val < last_exact_profit and (time.time() - start_time) < mt:
        optimality, sol, obj_value = model.optimize()

        if optimality:
            ub = last_exact_profit
            last_exact_profit = obj_value
        else:
            break

        if best_heu_val < last_exact_profit:
            val = calculate_expected_profit(sol, profits, survival_probs)
            if val > best_heu_val:
                best_heu_sol = sol
                best_heu_val = val
            previous_solutions.append(sol)
            j+=1
            model = ModelP(j=j, n=n_items, c=capacity, w=weights, p=profits, q=survival_probs,
                           best_heu_value=best_heu_val, last_exact_profit=last_exact_profit,
                           previous_solutions=previous_solutions, ml=1)
    return best_heu_sol, best_heu_val, ub , j , (time.time() - start_time)

