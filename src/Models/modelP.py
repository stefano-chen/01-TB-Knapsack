import math

from gurobipy import Model, GRB, quicksum, Env

class ModelP:
    def __init__(self, *, j, n, c, w, p, q, best_heu_value=0, last_exact_profit=2.220446049250313e+16, previous_solutions=None, ml):
        self.env = Env(empty=True)
        self.env.setParam("OutputFlag", 0)
        self.env.setParam("TimeLimit", ml)
        self.env.start()

        self.n = n
        self.model = Model("ModelP", env=self.env)

        self.x = self.model.addVars(n, vtype=GRB.BINARY, name="x")

        self.model.setObjective(quicksum([p[k]*self.x[k] for k in range(n)]), GRB.MAXIMIZE)

        self.model.addConstr(quicksum([w[k]*self.x[k] for k in range(n)]) <= c)

        self.model.addConstr(quicksum([math.log(q[k])*self.x[k] for k in range(n)]) >= math.log((best_heu_value+2.220446049250313e-16)/last_exact_profit)+2.220446049250313e-5)

        for i in range(j):
            self.model.addConstr(quicksum([self.x[k] if previous_solutions[i][k] else (1-self.x[k]) for k in range(n)]) <= n-1)

    def optimize(self):
        self.model.optimize()
        optimality = self.model.Status == GRB.OPTIMAL
        solution = [self.x[k].X for k in range(self.n)] if optimality else None
        obj_value = self.model.ObjVal if optimality else None
        result = (optimality, solution, obj_value)
        self.model.dispose()
        self.env.dispose()
        return result