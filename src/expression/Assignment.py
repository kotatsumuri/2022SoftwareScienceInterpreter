from src.expression.Expr import Expr


class Assignment(Expr):
    type: str
    name: str
    expression: Expr

    def __init__(self, name: str, expression: Expr):
        self.type = "Assignment"
        self.name = name
        self.expression = expression

    def evaluate(self, env: dict[str, int | Expr]) -> int | Expr:
        env[self.name] = self.expression.evaluate(env)
        return env[self.name]
