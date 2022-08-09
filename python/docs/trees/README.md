# Challenge Summary

1. Create a binary tree class with a methods for pre order, in order, and post order traversal

2. Create a binary search tree class with methods for adding in new values, as well as checking to see if the tree contains a given argument value

## Approach & Efficiency

For the binary tree functions the Big O for space would be O(0) as there is no output for the traversal functions. For time the Big O is O(N) due to the fact that the function iterates over every node in the tree, meaning that the time the function takes is linearly related to the number of nodes in the tree

For the binary search tree the Big O for space for the adding method is O(2/N) as it will only ever half to traverse half of the tree at mst, due to the split nature of the binary search tree. For space the Big O is O(1) as the add method only ever adds one node to the tree.

For the contains method in the binary search tree, the Big O for space is O(1) as it will only ever output either a True or False boolean. The BigO for time in the contains method is O(2/N) again for the same reasoning as the add method.

## Solution

Run the code for each file by running pytest on it's respective python test file. 

[Link to Binary Tree Code](python/data_structures/binary_tree.py)

[Link to Binary Search Tree](python/data_structures/binary_search_tree.py)
