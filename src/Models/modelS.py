import math

from gurobipy import Model, GRB, quicksum, Env

class ModelS:
    def __init__(self, *, j, n, c, w, p, q, best_heu_value=0, last_exact_probability=1, previous_solutions=None, ml):
        self.env = Env(empty=True)
        self.env.setParam("OutputFlag", 0)
        self.env.setParam("TimeLimit", ml)
        self.env.start()

        self.n = n
        self.model = Model("ModelS", env=self.env)

        self.x = self.model.addVars(n, vtype=GRB.BINARY, name="x")

        # Set Objective Function
        self.model.setObjective(quicksum([math.log(q[k])*self.x[k] for k in range(n)]), GRB.MAXIMIZE)

        # Capacity Constraint
        self.model.addConstr(quicksum([w[k]*self.x[k] for k in range(n)]) <= c)

        # Constraint to force the solution to have a total profit higher than (or equal to) the ration
        # The logic behind this constraint is:
        # The value of the objective function will be lower than or equal to that found in the previous iteration solved to optimality
        # in order to improve a heuristic solution with cost best_heu_value, we need a total profit greater than or equal to the ratio.
        self.model.addConstr(quicksum([p[k]*self.x[k] for k in range(n)]) >= (best_heu_value / last_exact_probability) + 2.220446049250313e-5)

        # This constraint force the solution of the model to be different from the solutions retrieved in the previous iterations
        # by imposing that at least one variable flips its value
        for i in range(j):
            self.model.addConstr(quicksum([self.x[k] if previous_solutions[i][k] == 1 else (1-self.x[k]) for k in range(n)]) <= n-1)

    def optimize(self):
        self.model.optimize()
        optimality = self.model.Status == GRB.OPTIMAL
        solution = [self.x[k].X for k in range(self.n)] if optimality else None
        obj_value = self.model.ObjVal if optimality else None
        result =  (optimality, solution, obj_value)
        self.model.dispose()
        self.env.dispose()
        return result