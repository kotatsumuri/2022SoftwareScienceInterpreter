import sys
from src.parser.parser import parser

code = [line for line in sys.stdin]
parser(code)
