from data_structures.queue import Queue
import re

wrong_tuple = ('[', '(', '{')

def multi_bracket_validation(string):
    regex = re.findall('[[|{|(|)|}|\]]', string)
    for i in regex:
        if regex[i] == '[' or '(' or '{':
            check_bracket(regex[i], regex, i)



def check_bracket(open, list, index):
    index += 1
    wrong_list_full = list(wrong_tuple)
    if open == '[':

    wrong_list_target =
    for i in list:
        i = list[i]
        if i == '[' or '{' or '(':
            check_bracket(i, list, index)
        if i ==
