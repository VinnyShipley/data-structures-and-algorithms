class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return 'NULL'
        current = self.head
        text = ''

        while current:
            text += '{ ' + str(current.value) + ' } -> '
            current = current.next
        return text + 'NULL'

    def insert(self, val):
            old_head = self.head
            self.head = Node(val)
            self.head.next = old_head

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class TargetError:
    pass
