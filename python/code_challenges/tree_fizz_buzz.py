from data_structures.kary_tree import Node, KaryTree, Queue




def fizz_buzz_tree(original_tree):
    fizz_tree = original_tree.clone_self()
    breadth = Queue()
    breadth.enqueue(fizz_tree.root)
    while not breadth.is_empty():
        front = breadth.dequeue()

        if front.value % 3 == 0 and front.value % 5 == 0:
            front.value = 'FizzBuzz'
            print(front.value)
            continue

        if front.value % 3 == 0:
            front.value = 'Fizz'
            for child in front.children:
                breadth.enqueue(child)
            print(front.value)
            continue

        if front.value % 5 == 0:
            front.value = 'Buzz'
            for child in front.children:
                breadth.enqueue(child)
            print(front.value)
            continue

        else:
            front.value = str(front.value)
            for child in front.children:
                breadth.enqueue(child)
            print(front.value)

    return fizz_tree
