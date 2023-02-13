import unittest
from src.expression.Assignment import Assignment
from src.expression.Int import Int


class TestAssignment(unittest.TestCase):
    def test_type(self):
        env = {}
        self.assertEqual(Assignment("a", Int(0)).type, "Assignment")

    def test_assignment(self):
        env = {}

        self.assertEqual(Assignment("a", Int(0)).evaluate(env), 0)
        self.assertEqual(env, {"a": 0})

        self.assertEqual(Assignment("b", Int(1)).evaluate(env), 1)
        self.assertEqual(env, {"a": 0, "b": 1})
