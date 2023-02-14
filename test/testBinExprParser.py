import unittest
from src.parser.parser import parser


class TestBinExprParser(unittest.TestCase):
    def test_add(self):
        code = ["1 + 2"]
        self.assertEqual(parser(code).evaluate({}), 3)

    def test_sub(self):
        code = ["1 - 2"]
        self.assertEqual(parser(code).evaluate({}), -1)

    def test_mul(self):
        code = ["1 * 2"]
        self.assertEqual(parser(code).evaluate({}), 2)

    def test_div(self):
        code = ["1 / 2"]
        self.assertEqual(parser(code).evaluate({}), 0)

    def test_minus(self):
        code = ["1 * -2"]
        self.assertEqual(parser(code).evaluate({}), -2)

    def test_eq(self):
        code = ["1 == 2"]
        self.assertEqual(parser(code).evaluate({}), 0)
        code = ["1 == 1"]
        self.assertEqual(parser(code).evaluate({}), 1)

    def test_neq(self):
        code = ["1 != 2"]
        self.assertEqual(parser(code).evaluate({}), 1)
        code = ["1 != 1"]
        self.assertEqual(parser(code).evaluate({}), 0)

    def test_leq(self):
        code = ["1 <= 2"]
        self.assertEqual(parser(code).evaluate({}), 1)
        code = ["1 <= 1"]
        self.assertEqual(parser(code).evaluate({}), 1)
        code = ["2 <= 1"]
        self.assertEqual(parser(code).evaluate({}), 0)

    def test_geq(self):
        code = ["1 >= 2"]
        self.assertEqual(parser(code).evaluate({}), 0)
        code = ["1 >= 1"]
        self.assertEqual(parser(code).evaluate({}), 1)
        code = ["2 >= 1"]
        self.assertEqual(parser(code).evaluate({}), 1)

    def test_lesser(self):
        code = ["1 < 2"]
        self.assertEqual(parser(code).evaluate({}), 1)
        code = ["1 < 1"]
        self.assertEqual(parser(code).evaluate({}), 0)
        code = ["2 < 1"]
        self.assertEqual(parser(code).evaluate({}), 0)

    def test_greater(self):
        code = ["1 > 2"]
        self.assertEqual(parser(code).evaluate({}), 0)
        code = ["1 > 1"]
        self.assertEqual(parser(code).evaluate({}), 0)
        code = ["2 > 1"]
        self.assertEqual(parser(code).evaluate({}), 1)

    def test_complex(self):
        code = ["-1 * ( 2 + 1 ) == 2 * ( 5 - -1 )"]
        self.assertEqual(parser(code).evaluate({}), 0)
