import unittest
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr
from src.expression.Assignment import Assignment
from src.expression.Ident import Ident
from src.expression.Seq import Seq


class TestSeq(unittest.TestCase):
    def test_type(self):
        self.assertEqual(Seq().type, "Seq")

    def test_Seq(self):
        env = {}

        Seq(
            Assignment("a", Int(1)),
            Assignment("b", Int(2)),
            Assignment("c", BinExpr("+", Ident("a"), Ident("b"))),
        ).evaluate(env)

        self.assertEqual(env, {"a": 1, "b": 2, "c": 3})
