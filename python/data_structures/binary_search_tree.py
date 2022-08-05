from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        super().__init__()

    def add(self,value):
        self.root = Node(value)


    def add_left(self,value):


        if not self.root:
            self.root = Node(value)

        def walk(root, node_to_add):
            if root is None:
                return

            if node_to_add.value < root.value:
                if not root.left:
                    root.left = node_to_add

                else:
                    walk(root.left, node_to_add)

            else:
                if root.right is None:
                    root.right = node_to_add

        walk(self, value)


    def contains(self, target):

        def walk(root):
            if root is None:
                return False

            if root.value == target:
                return True

            if root.value > target:
                walk(root.left)
            else:
                walk(root.right)

        return walk(self.root)
