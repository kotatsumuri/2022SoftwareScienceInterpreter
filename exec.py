import sys
from src.parser.interpreter import interpreter

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = open(sys.argv[1], "r")
        code = f.read()
        interpreter(code)
    