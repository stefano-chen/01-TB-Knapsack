from Algorithms.algorithm1 import iterative_algorithm_p
from Algorithms.algorithm2 import iterative_algorithm_s

# 01 Time-bomb Knapsack testing instance
n_items = 4
capacity = 5
weights = [2, 3, 1, 4]
profits = [10, 20, 15, 40]
survival_probs = [0.9, 1, 0.8, 1]

# Maximum computation time in seconds
MT = 3600

print("\nTesting Instance")
print(f"\tnumber of items : {n_items}")
print(f"\tknapsack's capacity : {capacity}")
print(f"\titems weights : {weights}")
print(f"\titems profits : {profits}")
print(f"\titems survival probabilities : {survival_probs}")

best_hue_sol, expected_profit, ub, n_iter, duration = iterative_algorithm_p(n_items, capacity, weights, profits, survival_probs, MT)

print("\nIterativeAlgorithmP")
print(f"\tsolution : {best_hue_sol}")
print(f"\texpected profit : {expected_profit}")
print(f"\tupper bound : {ub}")
print(f"\tnumber of iterations : {n_iter}")
print(f"\tcomputational time : {duration:.3f} seconds")

best_hue_sol, expected_profit, sol_type, n_iter, duration = iterative_algorithm_s(n_items, capacity, weights, profits, survival_probs, MT)

print("\nIterativeAlgorithmS")
print(f"\tsolution : {best_hue_sol}")
print(f"\texpected profit : {expected_profit}")
print(f"\tsolution type : {sol_type}")
print(f"\tnumber of iterations : {n_iter}")
print(f"\tcomputational time : {duration:.3f} seconds")