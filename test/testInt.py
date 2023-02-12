import unittest
from src.expression.Int import Int


class TestInt(unittest.TestCase):
    def test_type(self):
        self.assertEqual(Int(0).type, "Int")

    def test_zero(self):
        self.assertEqual(Int(0).evaluate(), 0)

    def test_str(self):
        with self.assertRaises(TypeError):
            Int("zero")
