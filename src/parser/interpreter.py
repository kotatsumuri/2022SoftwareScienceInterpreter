import sys
from src.parser.parser import parser


def interpreter(code):
    lines = [[t for t in line.split(" ")] for line in code.split("\n")]
    env = {}
    program = parser(lines)
    ret = program.evaluate(env)
    return (env, ret)
