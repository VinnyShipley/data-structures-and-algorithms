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

    def find_maximum_value(self):
        max = 0
        def walk(root):
            nonlocal max
            if root.value:
                print('this is None')
                if root.value > max:
                    max = root.value
                    if root.left:
                        walk(root.left)
                    if root.right:
                        walk(root.right)
                    return max
                if root.value <= max:
                    if root.left:
                        walk(root.left)
                    if root.right:
                        walk(root.right)
                    return max
            else:
                return max
        max = walk(self.root)
        return max



class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left
