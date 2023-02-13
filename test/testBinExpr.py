import unittest
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr


class TestBinExpr(unittest.TestCase):
    def test_type(self):
        self.assertEqual(BinExpr("+", Int(1), Int(2)).type, "BinExpr")

    def test_add(self):
        self.assertEqual(BinExpr("+", Int(1), Int(2)).evaluate(), 3)

    def test_sub(self):
        self.assertEqual(BinExpr("-", Int(1), Int(2)).evaluate(), -1)

    def test_mul(self):
        self.assertEqual(BinExpr("*", Int(1), Int(2)).evaluate(), 2)

    def test_div(self):
        self.assertEqual(BinExpr("/", Int(1), Int(2)).evaluate(), 0)

    def test_mod(self):
        self.assertEqual(BinExpr("%", Int(1), Int(2)).evaluate(), 1)

    def test_op(self):
        with self.assertRaises(ValueError):
            BinExpr("~", Int(1), Int(2))