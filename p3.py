import sys
from operator import add, sub
operators = {
    '+': add,
    '-': sub,
}
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
def get_result(expression, index = 0, count = 0):
    if expression[index] not in operators and expression[index] not in numbers:
        return False, None
    # condition of exit from recursion
    if index == len(expression) - 1:
        return True, count
    # add a sign before positive number
    if expression[0] not in operators:
        expression = '+' + expression
    if index == 0:
        count = operators[expression[0]](0, int(expression[1]))
        index+=1
    # body of recursion
    if expression[index] in operators:
        if expression[index+1] in numbers:
            count = operators[expression[index]](count, int(expression[index+1]))
        else:
            return False, None
    return get_result(expression, index + 1, count)

expression = "".join(sys.argv[1:])
print(get_result(expression))