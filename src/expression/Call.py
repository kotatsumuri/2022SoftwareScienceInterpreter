from src.expression.Expr import Expr
from src.expression.Func import Func
from copy import deepcopy


class Call(Expr):
    type: str
    name: str
    args: tuple[Expr]

    def __init__(self, name: str, *args: Expr):
        self.type = "Call"
        self.name = name
        self.args = args

    def evaluate(self, env: dict[str, int | Func]) -> int:
        new_env: dict[str, int | Func] = deepcopy(env)
        for arg, param in zip(self.args, env[self.name].params):  # type: ignore
            new_env[param] = arg.evaluate(env)
        return env[self.name].body.evaluate(new_env)  # type: ignore
