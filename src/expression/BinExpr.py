from src.expression.Expr import Expr


class BinExpr(Expr):
    type: str
    op: str
    left_expr: Expr
    right_expr: Expr

    def __init__(self, op: str, left_expr: Expr, right_expr: Expr):
        self.type = "BinExpr"

        match op:
            case "+" | "-" | "/" | "*":
                self.op = op
            case _:
                raise ValueError

        match left_expr:
            case Expr():
                self.left_expr = left_expr
            case _:
                raise TypeError

        match right_expr:
            case Expr():
                self.right_expr = right_expr
            case _:
                raise TypeError

    def evaluate(self) -> int:
        match self.op:
            case "+":
                return self.left_expr.evaluate() + self.right_expr.evaluate()
            case "-":
                return self.left_expr.evaluate() - self.right_expr.evaluate()
            case "/":
                return self.left_expr.evaluate() // self.right_expr.evaluate()
            case "*":
                return self.left_expr.evaluate() * self.right_expr.evaluate()
        return 0

    def __str__(self) -> str:
        return "%s(%s, %s, %s)" % (
            self.type,
            self.op,
            str(self.left_expr),
            str(self.right_expr),
        )
