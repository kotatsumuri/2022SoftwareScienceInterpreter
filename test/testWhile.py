import unittest
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr
from src.expression.Assignment import Assignment
from src.expression.Ident import Ident
from src.expression.Seq import Seq
from src.expression.If import If
from src.expression.While import While


class TestWhile(unittest.TestCase):
    def test_type(self):
        self.assertEqual(While(Int(1), Int(1)).type, "While")

    def test_while(self):
        env = {}

        Seq(
            Assignment("i", Int(1)),
            Assignment("sum", Int(0)),
            While(
                BinExpr("<=", Ident("i"), Int(10)),
                Seq(
                    Assignment("sum", BinExpr("+", Ident("sum"), Ident("i"))),
                    Assignment("i", BinExpr("+", Ident("i"), Int(1))),
                ),
            ),
        ).evaluate(env)

        self.assertEqual(env, {"i": 11, "sum": 55})
