from src.expression.Expr import Expr


class Ident(Expr):
    type: str
    name: str

    def __init__(self, name: str):
        self.type = "Ident"
        self.name = name

    def evaluate(self, env: dict[str, int]) -> int:
        return env[self.name]
