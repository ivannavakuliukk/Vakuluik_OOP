import sys

try:
    print(eval("".join(sys.argv[1:])))
except (SyntaxError, ValueError, TypeError):
    print("error")

