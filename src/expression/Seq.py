from src.expression.Expr import Expr


class Seq(Expr):
    type: str
    bodies: tuple[Expr]

    def __init__(self, *bodies: Expr):
        self.type = "Seq"
        self.bodies = bodies

    def evaluate(self, env: dict[str, int | Expr]) -> int:
        ret = 0
        for expr in self.bodies:
            ret = expr.evaluate(env)
        return ret
