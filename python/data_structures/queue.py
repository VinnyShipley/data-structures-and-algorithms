from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Queue is a linear data structure that stores items in a First-In/First Out(FIFO) manner. In queue, the data element that is inserted first will be removed first.
    """

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    # Adds item to queue
    def enqueue(self, value):
        # Creates new node to be added to rear
        new_rear = Node(value)

        #places the new node at the rear if there is no rear, and also declared the rear as the new front
        if not self.rear:
            self.rear = new_rear
            self.front = new_rear

        # places the new node at the rear of the queue
        else:
            new_rear.next = None
            self.rear.next = new_rear
            self.rear = new_rear


    #removes the node from the front of the queue
    def dequeue(self):

        # #checks if queue is empty, and returns error if empty
        # if self.is_empty():
        #     raise InvalidOperationError('InvalidOperationError')

        # # if non-empty list
        # if self.front == self.rear:
        #     self.rear is None
        # else:
        #     temp = self.front
        #     self.front = self.front.next
        #     temp.next = None
        # return temp.value

        if self.is_empty():
            raise InvalidOperationError("InvalidOperationError")
        prev_rear = self.front
        if self.front is self.rear:
            self.rear = None
        self.front = self.front.next
        prev_rear.next = None
        return prev_rear.value


    #peek method
    def peek(self):
        if self.is_empty():
            raise InvalidOperationError('Method not allowed on empty collection')
        else:
            return self.front.value


    # asserts that the front of the list is None. Is essentially a logic value to check against.
    def is_empty(self):
        return self.front is None

    # def __str__(self):
    #     temp = Queue()
    #     string_rep = "Front -> "
    #     while not self.is_empty():
    #         curr = self.dequeue()
    #         string_rep += f"{curr.value} -> "
    #         temp.enqueue(curr)
    #     self = temp
    #     return string_rep
