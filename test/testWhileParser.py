import unittest
from src.parser.interpreter import interpreter

class TestWhileParser(unittest.TestCase):
    def test_while(self):
        code = "var i = 1\n" \
               "var sum = 0\n" \
               "while i <= 10\n" \
               "    var sum = sum + i\n" \
               "    var i = i + 1\n" \
               "end\n" \
               "sum"
        self.assertEqual(interpreter(code)[1], 55)