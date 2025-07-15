import math

from gurobipy import Model, GRB, quicksum, Env

class ModelP:
    def __init__(self, *, j, n, c, w, p, q, best_heu_value=0, last_exact_profit=float("+inf"), previous_solutions=None, ml):
        self.env = Env(empty=True)
        self.env.setParam("OutputFlag", 0)
        self.env.setParam("TimeLimit", ml)
        self.env.start()

        self.n = n
        self.model = Model("ModelP", env=self.env)

        self.x = self.model.addVars(n, vtype=GRB.BINARY, name="x")

        self.model.setObjective(quicksum([p[k]*self.x[k] for k in range(n)]), GRB.MAXIMIZE)

        self.model.addConstr(quicksum([w[k]*self.x[k] for k in range(n)]) <= c)

        if best_heu_value > 0:
            self.model.addConstr(quicksum([math.log(q[k])*self.x[k] for k in range(n)]) >= math.log(best_heu_value/last_exact_profit))

        for i in range(j):
            self.model.addConstr(quicksum([self.x[k] if previous_solutions[i][k] else (1-self.x[k]) for k in range(n)]) <= n-1)

    def optimize(self):
        self.model.optimize()
        result =  (self.model.Status == GRB.OPTIMAL, self.model.Status not in [GRB.INFEASIBLE, GRB.INF_OR_UNBD, GRB.UNBOUNDED],
                [self.x[k].X for k in range(self.n)], self.model.ObjVal)
        self.model.dispose()
        self.env.dispose()
        return result