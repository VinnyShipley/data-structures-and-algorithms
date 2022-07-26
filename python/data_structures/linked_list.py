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

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            if current.next is not None:
                current = current.next
            current.next = Node(value)

    def insert_before(self, val, new_val):
        current = self.head
        while current.next != None:
            if current.next.new_val == val:
                current = Node(value = new_val)
                current.next = current.next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class TargetError:
    pass
