from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        super().__init__()

    def add(self,value):
        if not self.root:
            self.root = Node(value)
        if value < self.root.value:
            if not self.root.left:
                self.root.left = Node(value)
            else:
                walk(self.root.left, value)



            if not self.root.right:
                self.root.right = Node(value)

    def walk(root, target):
        if root is None:
                return
        if root









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
