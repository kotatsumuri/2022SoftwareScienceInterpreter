from src.expression.Expr import Expr
from typing import TypeVar

Self = TypeVar("Self", bound="Func")

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

    def evaluate(self, env: dict[str, int | Self]) -> int:
        env[self.name] = self # type: ignore        
        return 1

    def __str__(self):
        return "Func(name:%s, params:%s, body:%s)" % (self.name, str(self.params), str(self.body))
    