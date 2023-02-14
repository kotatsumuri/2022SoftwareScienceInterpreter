from src.expression.Expr import Expr
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr
from src.expression.Ident import Ident
from src.expression.Call import Call


class BinExprParser:
    line: list[str]

    def __init__(self, line: list[str]):
        self.line = line

    def parser(self) -> Expr:
        return self.o()
    
    def o(self) -> Expr:
        left_expr = self.a()
        while len(self.line) > 0 and self.line[0] == "|":
            op = self.line[0]
            self.line = self.line[1:]
            right_expr = self.a()
            left_expr = BinExpr(op, left_expr, right_expr)
        return left_expr
    
    def a(self) -> Expr:
        left_expr = self.comp()
        while len(self.line) > 0 and self.line[0] == "&":
            op = self.line[0]
            self.line = self.line[1:]
            right_expr = self.comp()
            left_expr = BinExpr(op, left_expr, right_expr)
        return left_expr

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
        elif self.line[0].isalpha():
            if len(self.line) > 1 and self.line[1] == "(":
                return self.fn()
            else:
                return self.var()

        self.line = self.line[1:]
        ret = self.expr()
        self.line = self.line[1:]
        return ret

    def number(self) -> Expr:
        ret = Int(int(self.line[0]))
        self.line = self.line[1:]
        return ret

    def var(self) -> Expr:
        ret = Ident(self.line[0])
        self.line = self.line[1:]
        return ret
    
    def fn(self) -> Expr:
        name = self.line[0]
        args = []
        self.line = self.line[2:]
        i = 0
        j = 0
        
        while True:
            if self.line[j][-1] == ",":
                self.line[j] = self.line[j][:-1]
                _line = self.line[i:j + 1]
                print(_line)
                args.append(BinExprParser(_line).parser())
                i = j + 1
            if self.line[j] == ")":
                _line = self.line[i:j]
                args.append(BinExprParser(_line).parser())
                break
            j += 1
        self.line = self.line[j+1:]
        return Call(name, *args)

def is_num(s: str) -> bool:
    try:
        int(s)
    except:
        return False
    return True
