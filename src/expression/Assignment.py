from src.expression.Expr import Expr
from src.expression.Func import Func


class Assignment(Expr):
    type: str
    name: str
    expression: Expr

    def __init__(self, name: str, expression: Expr):
        self.type = "Assignment"
        self.name = name
        self.expression = expression

    def evaluate(self, env: dict[str, int | Func]) -> int | Expr:
        env[self.name] = self.expression.evaluate(env)
        return env[self.name]

    def __str__(self):
        return "Assignment(name:%s, Expr:%s)" % (self.name, str(self.expression))
