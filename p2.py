import sys
from operator import add, truediv, sub, mul
operators = {
    "add": add,
    "multiply": mul,
    "subtract": sub,
    "divide": truediv,
}
expr = sys.argv[1:]
oper = expr[0]
operand = expr[1:]
try:

    print(operators[oper](int(operand[0]), int(operand[1])))
except KeyError:
    print("Wrong input")