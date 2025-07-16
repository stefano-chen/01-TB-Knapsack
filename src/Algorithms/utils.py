from gurobipy import Env, Model, GRB, quicksum

def calculate_expected_profit(solution, profits, survival_probs):
    profits_sum = 0
    prob_product = 1
    for i, x in enumerate(solution):
        if x:
            profits_sum += profits[i]
            prob_product *= survival_probs[i]

    return profits_sum * prob_product

def solve_deterministic_knapsack(selected_items, weights, profits, capacity, survival_probs):
    y = [0] * len(selected_items)

    # calculate residual capacity
    residual_capacity = capacity - sum(w if x == 1 else 0 for x, w in zip(selected_items, weights))

    # store indexes of the not selected not bomb items
    items_idx = [i for i in range(len(survival_probs)) if selected_items[i] == 0 and survival_probs[i] == 1]

    if len(items_idx) == 0 or residual_capacity <= 0:
        return y

    env = Env(empty=True)
    env.setParam("OutputFlag", 0)
    env.start()

    model = Model("ResidualKP", env=env)

    x = {i: model.addVar(vtype=GRB.BINARY, name=f"x_{i}") for i in items_idx}

    model.setObjective(quicksum([profits[i] * x[i] for i in items_idx]), GRB.MAXIMIZE)

    model.addConstr(quicksum([weights[i] * x[i] for i in items_idx]) <= residual_capacity)

    model.optimize()

    for i in items_idx:
        if x[i].X == 1:
            y[i] = 1

    return y