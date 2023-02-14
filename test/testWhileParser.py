import unittest
from src.parser.interpreter import interpreter

class TestWhileParser(unittest.TestCase):
    def test_while(self):
        code = "i = 1\n" \
               "sum = 0\n" \
               "while i <= 10\n" \
               "    sum = sum + i\n" \
               "    i = i + 1\n" \
               "end\n" \
               "sum"
        self.assertEqual(interpreter(code)[1], 55)