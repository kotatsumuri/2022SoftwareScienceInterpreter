from src.expression.Expr import Expr
from src.expression.Func import Func


class BinExpr(Expr):
    type: str
    op: str
    left_expr: Expr
    right_expr: Expr

    def __init__(self, op: str, left_expr: Expr, right_expr: Expr):
        self.type = "BinExpr"

        match op:
            case "+" | "-" | "/" | "*" | "%" | "<" | ">" | "<=" | ">=" | "==" | "!=" | "|" | "&":
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

    def evaluate(self, env: dict[str, int | Func]) -> int | bool:
        match self.op:
            case "+":
                return self.left_expr.evaluate(env) + self.right_expr.evaluate(env)
            case "-":
                return self.left_expr.evaluate(env) - self.right_expr.evaluate(env)
            case "/":
                return self.left_expr.evaluate(env) // self.right_expr.evaluate(env)
            case "*":
                return self.left_expr.evaluate(env) * self.right_expr.evaluate(env)
            case "%":
                return self.left_expr.evaluate(env) % self.right_expr.evaluate(env)
            case "<":
                return self.left_expr.evaluate(env) < self.right_expr.evaluate(env)
            case ">":
                return self.left_expr.evaluate(env) > self.right_expr.evaluate(env)
            case "<=":
                return self.left_expr.evaluate(env) <= self.right_expr.evaluate(env)
            case ">=":
                return self.left_expr.evaluate(env) >= self.right_expr.evaluate(env)
            case "==":
                return self.left_expr.evaluate(env) == self.right_expr.evaluate(env)
            case "!=":
                return self.left_expr.evaluate(env) != self.right_expr.evaluate(env)
            case "|":
                return self.left_expr.evaluate(env) or self.right_expr.evaluate(env)
            case "&":
                return self.left_expr.evaluate(env) and self.right_expr.evaluate(env)
        return 0

    def __str__(self) -> str:
        return "%s(%s, %s, %s)" % (
            self.type,
            self.op,
            str(self.left_expr),
            str(self.right_expr),
        )
