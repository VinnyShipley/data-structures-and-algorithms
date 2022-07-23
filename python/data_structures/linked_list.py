class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None



    def insert(self, val):
        if self.name is None:
            return 'NULL'
        if self.head == None:
            self.head = Node(val)
        else:
            Node.next = self.head
            self.head = Node(val)





class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class TargetError:
    pass
