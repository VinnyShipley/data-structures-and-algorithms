from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    # push method
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty() == True:
            raise InvalidOperationError('Method not allowed on empty collection')
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


    def peek(self):
        if self.is_empty() == True:
            raise InvalidOperationError('Method not allowed on empty collection')
        else:
            return self.top.value


