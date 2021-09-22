import sys
from operator import add, sub
operators = {
    '+': add,
    '-': sub,
}
def get_result(expression, index = 0, count = 0):
    # condition of exit from recursion
    if index == len(expression):
        return True, count
    # if there is at least one letter - formula is incorrect
    if expression[index].isalpha():
        return False, None
    # add a sign before positive number
    if expression[0] not in operators:
        expression = '+' + expression
    if index == 0:
        count = operators[expression[0]](0, int(expression[1]))
        index = 2
    # body of recursion
    if expression[index] in operators:
        if expression[index+1].isdigit():
            count = operators[expression[index]](count, int(expression[index+1]))
            return get_result(expression, index+2, count)
        else:
            return False, None
    else:
        return True, int(expression)

expression = "".join(sys.argv[1:])
print(get_result(expression))