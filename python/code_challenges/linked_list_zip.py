from data_structures.linked_list import LinkedList, Node

def zip_lists(a, b):
    new_list = LinkedList()
    # counter for list a
    n = 0
    # counter for list b
    k = 0
    current_a_node = a.head
    current_b_node = b.head

    # Testing to make sure that the values were being accessed correctly
    print(f'this is a.value {a.head.value} ')
    print(f'this is a head {a.head.value}')
    print(b)
    print(f'this is current a next {current_a_node.next.value}')

    while (current_a_node.next.value != None) or (current_b_node.next.value != None):


        #if the next value in the current node in list b is None
        if current_b_node.next.value == None:
            while current_a_node.next.value != None:
                new_list.append(current_a_node.value)
                current_a_node.value = current_a_node.next.value
                return new_list

        # if the next value of the current node in list a is None
        if current_a_node.next.value == None:
            while current_b_node.next.value != None:
                new_list.append(current_b_node.value)
                current_b_node.value = current_b_node.next.value
                return new_list



        if n == k:
            new_list.append(current_a_node.value)
            n += 1
            current_a_node.value = current_a_node.next.value
            if current_a_node.next.value == None:
                return new_list


        if n > k:
            new_list.append(current_b_node.value)
            k += 1
            current_b_node.value = current_b_node.next.value
            if current_b_node.next.value == None:
                return new_list

    return new_list

