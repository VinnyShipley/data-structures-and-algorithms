from data_structures.stack import Stack
from data_structures.linked_list import Node


class PseudoQueue(Stack):
    def enqueue(self, new_val):
        new_node = Node(new_val)
        stack_one = self
        stack_two = Stack()
        while stack_one.top:
            popped = stack_one.pop()
            stack_two.push(popped)
        stack_one.push(new_node)
        while stack_two.top:
            popped_two = stack_two.pop()
            stack_one.push(popped_two)


    def dequeue(self):
        temp = self.pop()
        return temp.value

