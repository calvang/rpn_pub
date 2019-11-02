#!/usr/bin/env python3

import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,  
}

def calculate(myarg):
    stack = list()
    # TODO more intelligent split
    arg_list = split_arges(myarg)
    # TODO convert matrix string into np.array
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            # TODO handle stack of brackets 
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()