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
from src.parser.AssignmentParser import AssignmentParser


def parser(lines: list[list[str]]) -> Seq:
    cmd = []
    while len(lines) > 0:
        line = lines[0]
        
        while line[0] == "" and len(line) > 0:
            del line[0]
        if len(line) == 0:
            del lines[0]
            continue

        match line[0]:
            case "var":
                cmd.append(AssignmentParser(line[1:]).parser())
                del lines[0]
            case "if":
                condition = BinExprParser(line[1:]).parser()
                del lines[0]
                thenClause = parser(lines)
                elseClause = Int(0)
                if lines[0] == "end":
                    del lines[0]
                if lines[0] == "else":
                    del lines[0]
                    elseClause = parser(lines)
                    del lines[0]
                cmd.append(If(condition, thenClause, elseClause))
            case "end" | "else":
                return Seq(*cmd)
            case _:
                cmd.append(BinExprParser(line).parser())
                del lines[0]

    return Seq(*cmd)
