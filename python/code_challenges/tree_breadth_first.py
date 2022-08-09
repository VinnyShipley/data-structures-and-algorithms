from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    new_queue = Queue()
    output_list = []
    root = tree.root

    new_queue.enqueue(root)

    if root is None:
        return output_list

    while not new_queue.is_empty():
        current = new_queue.dequeue()
        output_list.append(current.value)

        if current.left:
            new_queue.enqueue(current.left)

        if current.right:
            new_queue.enqueue(current.right)

    return output_list
