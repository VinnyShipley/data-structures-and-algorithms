from data_structures.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection

    def clone_self(self):
        if not self.root:
            return KaryTree()

        breadth = Queue()
        cloned_queue = Queue()

        clone_root = self.root

        breadth.enqueue(self.root)

        cloned_queue.enqueue(clone_root)

        while not breadth.is_empty():
            front = breadth.dequeue()

            clone_front = Node(front)
            if not clone_root:
                clone_root = clone_front
            for child in front.children:
                breadth.enqueue(child)
                cloned_child = Node(child.value)
                cloned_queue.enqueue(cloned_child)
                cloned_child.children.append(cloned_child)

        return KaryTree(root=clone_root)


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []
