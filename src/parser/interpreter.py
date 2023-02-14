import sys
from src.parser.parser import parser


def interpreter(code):
    lines = [[t for t in line.split(" ")] for line in code.split("\n")]
    print(lines)
    env = {}
    ret = parser(lines).evaluate(env)
    return (env, ret)
