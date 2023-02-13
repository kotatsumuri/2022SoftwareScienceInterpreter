from src.expression.Expr import Expr

class Func(Expr):
    type: str
    name: str
    params: list[str]
    body: Expr

    def __init__(self, name: str, params: list[str], body: Expr):
        self.type = "Func"
        self.name = name
        self.params = params
        self.body = body

    def evaluate(self, env: dict[str, int | Expr]) -> int:
        env[self.name] = self
        return 1
    