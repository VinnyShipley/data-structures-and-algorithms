from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear


    def enqueue(self, value):
        new_rear = Node(value)

        if not self.rear:
            self.rear = new_rear
            self.front = new_rear

        else:
            new_rear.next = None
            self.rear.next = new_rear


    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError('InvalidOperationError')
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError('InvalidOperationError')
        else:
            return self.front.value

    def is_empty(self):
        if self.front == None:
            return True

