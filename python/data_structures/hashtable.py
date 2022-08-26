from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self.list = [None] * self.size

    def set(self, key, value):
        key_value_tuple = (key, value)
        index = self.hash(key)
        if self.list[index] == None:
            bucket_list = LinkedList()
            self.list[index] = bucket_list
            bucket_list.head = key_value_tuple
        else:
            while self.list[index]:
                if


    def hash(self, key):

        char_num_list = []

        for char in key:

            num = ord(char)
            primed = num * 599
            char_num_list.append(primed)

        char_sum = sum(char_num_list)
        return self.size % char_sum





