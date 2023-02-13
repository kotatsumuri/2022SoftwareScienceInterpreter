import unittest
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr
from src.expression.Assignment import Assignment
from src.expression.Ident import Ident


class TestIdent(unittest.TestCase):
    def test_type(self):
        self.assertEqual(Ident("a").type, "Ident")

    def test_ident(self):
        env = {}

        Assignment("a", Int(0)).evaluate(env)
        self.assertEqual(Ident("a").evaluate(env), 0)
        self.assertEqual(env, {"a": 0})

        Assignment("b", Int(1)).evaluate(env)
        self.assertEqual(Ident("b").evaluate(env), 1)
        self.assertEqual(env, {"a": 0, "b": 1})

    def test_binExpr(self):
        env = {}

        Assignment("a", Int(1)).evaluate(env)
        Assignment("b", Int(2)).evaluate(env)
        Assignment("c", BinExpr("+", Ident("a"), Ident("b"))).evaluate(env)

        self.assertEqual(env, {"a": 1, "b": 2, "c": 3})
