import unittest
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr

env = {}


class TestBinExpr(unittest.TestCase):
    def test_type(self):
        self.assertEqual(BinExpr("+", Int(1), Int(2)).type, "BinExpr")

    def test_add(self):
        self.assertEqual(BinExpr("+", Int(1), Int(2)).evaluate(env), 3)

    def test_sub(self):
        self.assertEqual(BinExpr("-", Int(1), Int(2)).evaluate(env), -1)

    def test_mul(self):
        self.assertEqual(BinExpr("*", Int(1), Int(2)).evaluate(env), 2)

    def test_div(self):
        self.assertEqual(BinExpr("/", Int(1), Int(2)).evaluate(env), 0)

    def test_mod(self):
        self.assertEqual(BinExpr("%", Int(1), Int(2)).evaluate(env), 1)

    def test_eq(self):
        self.assertEqual(BinExpr("==", Int(1), Int(2)).evaluate(env), 0)
        self.assertEqual(BinExpr("==", Int(1), Int(1)).evaluate(env), 1)

    def test_neq(self):
        self.assertEqual(BinExpr("!=", Int(1), Int(2)).evaluate(env), 1)
        self.assertEqual(BinExpr("!=", Int(1), Int(1)).evaluate(env), 0)

    def test_lesser(self):
        self.assertEqual(BinExpr("<", Int(1), Int(2)).evaluate(env), 1)
        self.assertEqual(BinExpr("<", Int(1), Int(1)).evaluate(env), 0)
        self.assertEqual(BinExpr("<", Int(2), Int(1)).evaluate(env), 0)

    def test_greater(self):
        self.assertEqual(BinExpr(">", Int(1), Int(2)).evaluate(env), 0)
        self.assertEqual(BinExpr(">", Int(1), Int(1)).evaluate(env), 0)
        self.assertEqual(BinExpr(">", Int(2), Int(1)).evaluate(env), 1)

    def test_leq(self):
        self.assertEqual(BinExpr("<=", Int(1), Int(2)).evaluate(env), 1)
        self.assertEqual(BinExpr("<=", Int(1), Int(1)).evaluate(env), 1)
        self.assertEqual(BinExpr("<=", Int(2), Int(1)).evaluate(env), 0)

    def test_geq(self):
        self.assertEqual(BinExpr(">=", Int(1), Int(2)).evaluate(env), 0)
        self.assertEqual(BinExpr(">=", Int(1), Int(1)).evaluate(env), 1)
        self.assertEqual(BinExpr(">=", Int(2), Int(1)).evaluate(env), 1)

    def test_op(self):
        with self.assertRaises(ValueError):
            BinExpr("~", Int(1), Int(2))
