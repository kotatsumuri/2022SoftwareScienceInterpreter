from src.expression.Expr import Expr
from src.expression.Func import Func


class If(Expr):
    type: str
    condition: Expr
    thenClause: Expr
    elseClause: Expr

    def __init__(self, condition: Expr, thenClause: Expr, elseClause: Expr):
        self.type = "If"
        self.condition = condition
        self.thenClause = thenClause
        self.elseClause = elseClause

    def evaluate(self, env: dict[str, int | Func]) -> int:
        if self.condition.evaluate(env):
            return self.thenClause.evaluate(env)
        return self.elseClause.evaluate(env)

    def __str__(self):
        return "If(condition:%s, thenClause:%s, elseClause:%s)" % (str(self.condition), str(self.thenClause), str(self.elseClause))
