from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    # push method puts a value at the top of the stack
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    # pop method takes the node at the top of the stack off of the stack
    def pop(self):
        if self.is_empty() == True:
            raise InvalidOperationError('Method not allowed on empty collection')
        temp = self.top

        #reassigns the new top to be the value of top.next
        self.top = self.top.next
        temp.next = None
        return temp.value

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


    #checks the value at the top of the stack
    def peek(self):
        if self.is_empty() == True:
            raise InvalidOperationError('Method not allowed on empty collection')
        else:
            return self.top.value


