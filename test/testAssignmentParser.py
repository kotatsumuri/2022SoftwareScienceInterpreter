import unittest
from src.parser.parser import parser


class TestAssignmentParser(unittest.TestCase):
    def test_simple(self):
        env = {}
        code = ["var a = 1 + 1"]
        parser(code).evaluate(env)
        self.assertEqual(env, {"a": 2})

    def test_complex(self):
        env = {}
        code = ["var a = 1 + 1", "var b = 2 + 1", "var a = 3 + 2"]
        parser(code).evaluate(env)
        self.assertEqual(env, {"a": 5, "b": 3})
