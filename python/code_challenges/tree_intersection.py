from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable




def tree_intersection(tree_a, tree_b):
    hash = Hashtable()
    return_nums = []
    a_values = tree_a.pre_order()
    b_values = tree_b.pre_order()
    for nums in a_values:
        key = str(nums)
        hash.set(key, nums)
    for nums in b_values:
        key = str(nums)
        if hash.contains(key) and not nums in return_nums:
            return_nums.append(nums)
    print(return_nums)
    return return_nums
