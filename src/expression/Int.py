from Expr import Expr


class Int(Expr):
    type: "Int"
    value: int

    def __init__(self, value: int):
        self.value = value

    def evaluate(self) -> int:
        return self.value
