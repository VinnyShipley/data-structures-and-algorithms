# Singly Linked List

A Singly linked list is a node list where each node contains two pieces of information: a value, and a next.

## Challenge

Today's challenge was, when given a singly linked list, to create a function that inserts a node at the head of the list, a function that checks if the list contains a certain value, and a function that turns the list into a specific string structure.

## Approach & Efficiency

In both time and space, the insert algorithm is a O(1) function, as it is only ever adding one value to the node list, and the function will never be longer.

The Big O quotient for the includes function when thinking about space is O(1) because it will only ever return a boolean value. For time however Big O is O(N) due to the fact that at worst case it will have to iterate over every value of the given list, and that list length will vary based on the list, thus taking up more time.

The Big O quotient for space in the string function is O(N) because the longer the list being fed into the function, the longer the output will be, by a linear measure. Time will also be O(N) due to the fact that the function has to list loop through the entire list every time.

## API

The approach I took for the insert was to identify the head of the list and then change the value of the head node to the value of the input of the function, with the next value being the old head of the list.

The includes function loops through the list and checks if the current value is the value input into the function. If the current value does not equal the input, the current value is then set to the next value of the current node. If the value of the current is the input value, the function returns a true boolean. If the current value is ever None, meaning that it has gotten to the end of the list, the function returns a false boolean.

The to string function is essentially another looping function, where as long as the current value of the node is true, meaning it is not none, that value is put into a string structure and placed in a format easily viewable to humans. When current is false, meaning that it has encountered the end of the list, it stops looping and outputs the statement.

[Link to code](python/data_structures/linked_list.py)
