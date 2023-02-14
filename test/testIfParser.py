import unittest
from src.parser.interpreter import interpreter


class TestIfParser(unittest.TestCase):
    def test_if(self):
        code = "if 1 == 1\n" \
               "    1\n" \
               "end"
        self.assertEqual(interpreter(code)[1], 1)

    def test_if_else(self):
        code = "if 1 == 0\n" \
               "    1\n" \
               "else\n" \
               "    0\n" \
               "end"
        self.assertEqual(interpreter(code)[1], 0)
    
    def test_if_if_else(self):
        code ="if 1 == 1\n" \
              "    a = 0\n" \
              "    if a == 0\n" \
              "        a = a + 1\n" \
              "    end\n" \
              "else\n" \
              "end"
        self.assertEqual(interpreter(code)[0], {"a": 1})

