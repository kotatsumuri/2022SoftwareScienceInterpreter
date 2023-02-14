from src.expression.Expr import Expr
from src.expression.Func import Func


class Ident(Expr):
    type: str
    name: str

    def __init__(self, name: str):
        self.type = "Ident"
        self.name = name

    def evaluate(self, env: dict[str, int | Func]) -> int:
        return env[self.name]  # type: ignore

    def __str__(self):
        return "Ident(name:%s)" % (self.name)