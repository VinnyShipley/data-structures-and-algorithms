class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    # To string function
    def __str__(self):
        if self.head is None:
            return 'NULL'
        current = self.head
        text = ''

        while current:
            text += '{ ' + str(current.value) + ' } -> '
            current = current.next
        return text + 'NULL'

    # Insert Function
    def insert(self, val):
            old_head = self.head
            self.head = Node(val)
            self.head.next = old_head

    # Includes function
    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # Append function
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            if current.next is not None:
                current = current.next
            current.next = Node(value)

    # Insert before function
    def insert_before(self, val, new_val):
        current = self.head
        while current.next != None:
            if current.next.new_val == val:
                current = Node(value = new_val)
                current.next = current.next

    # kth from the end function
    def kth_from_end(self, k):
        length = 0
        current = self.head
        if k < 0:
            raise TargetError
        if current == None:
            raise TargetError
        while current != None:
            length += 1
            current = current.next
        needed_steps = (length - 1) - k
        if needed_steps < 0:
            raise TargetError
        current = self.head
        while needed_steps > 0:
            needed_steps -= 1
            current = current.next
        print(current)
        return current.value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class TargetError(Exception):
    pass
