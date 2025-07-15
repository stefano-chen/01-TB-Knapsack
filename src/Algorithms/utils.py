def calculate_expected_profit(solution, profits, survival_probs):
    profits_sum = 0
    prob_product = 1
    for i, x in enumerate(solution):
        if x:
            profits_sum += profits[i]
            prob_product *= survival_probs[i]

    return profits_sum * prob_product