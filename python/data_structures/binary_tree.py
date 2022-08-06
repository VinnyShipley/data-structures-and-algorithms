class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root


    def pre_order(self):
        values = []
        def walk(root):
            if root is None:
                return None
            # root
            values.append(root.value)
            # left
            walk(root.left)
            # right
            walk(root.right)
        walk(self.root)
        return values


    def in_order(self):
        """
        left
        root
        right
        """
        values = []
        def walk(root):
            if root is None:
                return None
            # left
            walk(root.left)
            # root
            values.append(root.value)
            #right
            walk(root.right)
        walk(self.root)
        return values

    def post_order(self):
        """
        right
        root
        left
        """
        values = []
        def walk(root):
            if root is None:
                return None
            #left
            walk(root.left)
            # right
            walk(root.right)
            #root
            values.append(root.value)
        walk(self.root)
        return values





class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
