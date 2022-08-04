from data_structures.queue import Queue
from data_structures.stack import Stack
import re


def multi_bracket_validation(string):
    stack = Stack()
    list = re.findall('[[|{|(|)|}|\]]', string)

    for i in list:

        if i == '[' or '{' or '(':
            print(i)
            stack.push(i)
            break
        if i == ']' or '}' or ')':

            if stack.top == None:
                return False
            top_of_stack = stack.pop()
            print('this is top of stack',top_of_stack)
            if not char_matcher(top_of_stack, i):
                return False
    if len(stack) != 0:
            return False
    return True

def char_matcher(opener, closer):
    if opener == '(' and closer == ')':
        return True

    if opener == '{' and closer == '}':
        return True

    if opener == '[' and closer == ']':
        return True

    return False

