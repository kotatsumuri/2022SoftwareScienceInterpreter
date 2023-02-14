import unittest
from src.parser.interpreter import interpreter

class TestFuncParser(unittest.TestCase):
    def test_def_call(self):
        code = "fn sum ( start, fin )\n"\
               "    var i = start\n" \
               "    var ret = 0\n" \
               "    while i <= fin\n" \
               "         var ret = ret + i\n" \
               "         var i = i + 1\n"\
               "    end\n"\
               "    ret\n"\
               "end\n"\
               "var a = 10\n"\
               "sum ( 1, a )"

        self.assertEqual(interpreter(code)[1], 55)
