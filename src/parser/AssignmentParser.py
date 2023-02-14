from src.expression.Expr import Expr
from src.expression.Assignment import Assignment
from src.parser.BinExprParser import BinExprParser


class AssignmentParser:
    line: list[str]

    def __init__(self, line: list[str]):
        self.line = line

    def parser(self) -> Expr:
        return Assignment(self.line[0], BinExprParser(self.line[2:]).parser())
