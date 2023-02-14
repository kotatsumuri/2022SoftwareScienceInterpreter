import unittest
from src.parser.interpreter import interpreter


class TestAssignmentParser(unittest.TestCase):
    def test_simple(self):
        env = {}
        code = "a = 1 + 1"
        env = interpreter(code)[0]
        self.assertEqual(env, {"a": 2})

    def test_complex(self):
        env = {}
        code = "a = 1 + 1\n" \
               "b = 2 + 1\n" \
               "a = 3 + 2"
        env = interpreter(code)[0]
        self.assertEqual(env, {"a": 5, "b": 3})

    def test_call_var(self):
        env = {}
        code = "a = 0\n"\
               "a = a + 1"
        env = interpreter(code)[0]
        self.assertEqual(env, {"a": 1})
