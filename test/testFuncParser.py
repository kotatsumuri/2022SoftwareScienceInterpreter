import unittest
from src.parser.interpreter import interpreter

class TestFuncParser(unittest.TestCase):
    def test_def_call(self):
        code = "fn sum ( start, fin )\n"\
               "    i = start\n" \
               "    ret = 0\n" \
               "    while i <= fin\n" \
               "         ret = ret + i\n" \
               "         i = i + 1\n"\
               "    end\n"\
               "    ret\n"\
               "end\n"\
               "a = 10\n"\
               "sum ( 1, a )"

        self.assertEqual(interpreter(code)[1], 55)
