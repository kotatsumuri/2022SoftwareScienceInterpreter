import unittest
from src.parser.interpreter import interpreter


class TestAssignmentParser(unittest.TestCase):
    def test_simple(self):
        env = {}
        code = "var a = 1 + 1"
        env = interpreter(code)
        self.assertEqual(env, {"a": 2})

    def test_complex(self):
        env = {}
        code = "var a = 1 + 1\nvar b = 2 + 1\nvar a = 3 + 2"
        env = interpreter(code)
        self.assertEqual(env, {"a": 5, "b": 3})

    def test_call_var(self):
        env = {}
        code = "var a = 0\nvar a = a + 1"
        env = interpreter(code)
        self.assertEqual(env, {"a": 1})
