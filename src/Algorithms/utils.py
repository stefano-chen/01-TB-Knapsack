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
    residual_capacity = capacity - sum(w if x else 0 for x, w in zip(selected_items, weights))

    items_idx = [i for i in range(len(survival_probs)) if selected_items[i] == 0 and survival_probs[i] == 1]

    env = Env(empty=True)
    env.setParam("OutputFlag", 0)
    env.start()

    model = Model("ResidualKP", env=env)

    x = model.addVars(len(items_idx), vtype=GRB.BINARY, name="x")

    model.setObjective(quicksum([profits[i] * x[i] for i in items_idx]), GRB.MAXIMIZE)

    model.addConstr(quicksum([weights[i] * x[i] for i in items_idx]) <= residual_capacity)

    model.optimize()

    y = [0] * len(selected_items)

    for i, index in enumerate(items_idx):
        if x[i].X == 1:
            y[index] = 1

    return y