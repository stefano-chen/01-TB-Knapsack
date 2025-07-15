from Algorithms.algorithm1 import iterative_algorithm_p

best_hue_sol, last_extract_profit, n_iter, duration = iterative_algorithm_p(4, 7, [2, 3, 2, 5], [10, 20, 15, 30], [0.9, 0.85, 0.8, 0.6], 10)

print(best_hue_sol, last_extract_profit, n_iter, duration)