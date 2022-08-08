from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    new_queue = Queue()
    output_list = []
    i = 1
    root = tree.root

    new_queue.enqueue(root)

    if root is None:
        return output_list

    while not new_queue.is_empty():
        print(new_queue)

        print(i)
        current = new_queue.dequeue()
        output_list.append(current.value)
        print(output_list)
        if current.left:
            new_queue.enqueue(current.left)
            print(new_queue)

        if current.right:
            print(current.right.value)
            new_queue.enqueue(current.right)
            print(new_queue)
        i += 1
    return output_list
