from Algorithms.algorithm1 import iterative_algorithm_p
from Algorithms.utils import calculate_expected_profit

# 01 Time-bomb Knapsack testing instance
n_items = 4
capacity = 7
weights = [2, 3, 2, 5]
profits = [10, 20, 15, 30]
survival_probs = [0.9, 0.85, 0.8, 0.6]

# Maximum computation time in seconds
ML = 5

print("\nTesting Instance")
print(f"\tnumber of items : {n_items}")
print(f"\tknapsack's capacity : {capacity}")
print(f"\titems weights : {weights}")
print(f"\titems profits : {profits}")
print(f"\titems survival probabilities : {survival_probs}")

best_hue_sol, last_extract_profit, n_iter, duration = iterative_algorithm_p(n_items, capacity, weights, profits, survival_probs, ML)

expected_profit = calculate_expected_profit(best_hue_sol, profits, survival_probs)

print("\nIterativeAlgorithmP")
print(f"\tsolution : {best_hue_sol}")
print(f"\texpected profit : {expected_profit:.2f}")
print(f"\toptimal solution upper bound : {last_extract_profit}")
print(f"\tnumber of iterations : {n_iter}")
print(f"\tcomputational time : {duration:.3f} seconds")