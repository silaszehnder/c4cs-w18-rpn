#!/usr/bin/env python3
#rpn: reverse polish notation

import operator
import logging
import sys

#typically just name it the module you're in
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

#Implemented the same way as the Microsoft link
def percentage(arg1, arg2):
    return arg1 + ( (arg2 / 100) * arg1) 


operators = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    '%': percentage, 
    '^': operator.pow,
    '.': operator.floordiv,
    '&': operator.and_,
    '|': operator.or_,
    '~': operator.not_,
}

stack = list()
def calculate(arg):
    for token in arg.split():
        if token == 'copy':
            stack.append(stack[-1])
            logger.debug(stack)
            return stack[-1] == stack[-2]
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            if token == '~':
                result = function(arg2)
                return result
            else:
                arg1 = stack.pop()
                result = function(arg1, arg2)
            stack.append(result)
        logger.debug(stack)

    return stack[-1]

def main():
    while True:
        print(calculate(input('rpm calc> ')))


if __name__ == '__main__':
    main()
