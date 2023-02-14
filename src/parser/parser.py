from src.expression.Expr import Expr
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr
from src.expression.Assignment import Assignment
from src.expression.Ident import Ident
from src.expression.Seq import Seq
from src.expression.If import If
from src.expression.While import While
from src.expression.Func import Func
from src.expression.Call import Call
from src.parser.BinExprParser import BinExprParser


def parser(code: list[str]) -> Seq:
    lines = [[t.strip("\n") for t in line.split(" ")] for line in code]

    vars = []
    fns = []
    cmd = []
    for line in lines:
        cmd.append(BinExprParser(line).parser())

    return Seq(*cmd)
