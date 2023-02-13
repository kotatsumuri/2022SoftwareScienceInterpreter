import unittest
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr
from src.expression.Assignment import Assignment
from src.expression.Ident import Ident
from src.expression.Seq import Seq
from src.expression.If import If


class TestIf(unittest.TestCase):
    def test_type(self):
        self.assertEqual(If(Int(1), Int(1), Int(1)).type, "If")

    def test_simple(self):
        self.assertEqual(If(Int(1), Int(1), Int(0)).evaluate({}), 1)
        self.assertEqual(If(Int(0), Int(1), Int(0)).evaluate({}), 0)

    def test_complex(self):
        env = {}

        Seq(
            Assignment("a", Int(1)),
            Assignment("b", Int(2)),
            If(
                BinExpr("==", Ident("a"), Ident("b")),
                Assignment("a", BinExpr("+", Ident("a"), Int(1))),
                Assignment("a", BinExpr("-", Ident("a"), Int(1))),
            ),
        ).evaluate(env)

        self.assertEqual(env, {"a": 0, "b": 2})
