import unittest
from src.expression.Int import Int
from src.expression.BinExpr import BinExpr
from src.expression.Assignment import Assignment
from src.expression.Ident import Ident
from src.expression.Seq import Seq
from src.expression.If import If
from src.expression.While import While
from src.expression.Func import Func
from src.expression.Call import Call


class TestFuncCall(unittest.TestCase):
    def test_type(self):
        self.assertEqual(Func("f", [], Int(1)).type, "Func")
        self.assertEqual(Call("f").type, "Call")

    def test_func_call(self):
        env = {}

        Seq(
            Func(
                "func_sum",
                ["start", "end"],
                Seq(
                    Assignment("i", Ident("start")),
                    Assignment("sum", Int(0)),
                    While(
                        BinExpr("<=", Ident("i"), Ident("end")),
                        Seq(
                            Assignment("sum", BinExpr("+", Ident("sum"), Ident("i"))),
                            Assignment("i", BinExpr("+", Ident("i"), Int(1))),
                        ),
                    ),
                    Ident("sum"),
                ),
            ),
            Assignment("ret", Call("func_sum", Int(1), Int(10))),
        ).evaluate(env)

        self.assertEqual(env["ret"], 55)
