from src.expression.Expr import Expr
from src.expression.BinExpr import BinExpr


class If(Expr):
    type: str
    condition: BinExpr
    thenClause: Expr
    elseClause: Expr

    def __init__(self, condition: BinExpr, thenClause: Expr, elseClause: Expr):
        self.type = "If"
        self.condition = condition
        self.thenClause = thenClause
        self.elseClause = elseClause

    def evaluate(self, env: dict[str, int]) -> int:
        if self.condition.evaluate(env):
            return self.thenClause.evaluate(env)
        return self.elseClause.evaluate(env)
