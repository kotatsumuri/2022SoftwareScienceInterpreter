from src.expression.Expr import Expr


class Int(Expr):
    type: str
    value: int

    def __init__(self, value: int):
        self.type = "Int"

        match value:
            case int():
                self.value = value
            case _:
                raise TypeError("Type error.")

    def evaluate(self, env: dict[str, int]) -> int:
        return self.value

    def __str__(self) -> str:
        return "%s(%d)" % (self.type, self.value)
