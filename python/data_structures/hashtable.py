from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.buckets = [None] * size
        self.size = size

    def set(self, key, value):
        key_value_tuple = (key, value)
        index = self.hash(key)
        bucket = self.buckets[index]

        if bucket == None:

            bucket = LinkedList()
            self.buckets[index] = bucket
            bucket.head = key_value_tuple

        bucket.insert(key_value_tuple)


    def hash(self, key):
        char_num_list = []

        for char in key:
            num = ord(char)
            char_num_list.append(num)

        char_sum = sum(char_num_list)
        hashed_index = char_sum * 599
        return hashed_index % self.size


    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            return False
        if bucket:
            current = bucket.head
            while current:
                key_value_pair = current.value
                if key_value_pair[0] == key:
                    return True
                current = current.next
        return False

    def get(self, key):
        pass


    def keys(self):
        keys_list = []
        for bucket in self.buckets:
            if bucket:
                current = bucket.head
                while current:
                    keys_list.append(current.value[0])
                    current = current.next
        return keys_list








