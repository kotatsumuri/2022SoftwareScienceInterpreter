from src.expression.Expr import Expr
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr


class BinExprParser:
    line: list[str]

    def __init__(self, line: list[str]):
        self.line = line

    def parser(self) -> Expr:
        return self.comp()

    def comp(self) -> Expr:
        left_expr = self.expr()
        while len(self.line) > 0 and (
            self.line[0] == "=="
            or self.line[0] == "!="
            or self.line[0] == ">="
            or self.line[0] == "<="
            or self.line[0] == ">"
            or self.line[0] == "<"
        ):
            op = self.line[0]
            self.line = self.line[1:]
            right_expr = self.expr()
            left_expr = BinExpr(op, left_expr, right_expr)
        return left_expr

    def expr(self) -> Expr:
        left_expr = self.term()
        while len(self.line) > 0 and (self.line[0] == "+" or self.line[0] == "-"):
            op = self.line[0]
            self.line = self.line[1:]
            right_expr = self.term()
            left_expr = BinExpr(op, left_expr, right_expr)
        return left_expr

    def term(self) -> Expr:
        left_expr = self.factor()
        while len(self.line) > 0 and (
            self.line[0] == "*" or self.line[0] == "/" or self.line[0] == "%"
        ):
            op = self.line[0]
            self.line = self.line[1:]
            right_expr = self.factor()
            left_expr = BinExpr(op, left_expr, right_expr)
        return left_expr

    def factor(self) -> Expr:
        if is_num(self.line[0]):
            return self.number()

        self.line = self.line[1:]
        ret = self.expr()
        self.line = self.line[1:]
        return ret

    def number(self) -> Expr:
        ret = Int(int(self.line[0]))
        self.line = self.line[1:]
        return ret


def is_num(s: str) -> bool:
    try:
        int(s)
    except:
        return False
    return True
