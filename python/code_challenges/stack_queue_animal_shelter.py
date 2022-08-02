from data_structures.queue import Queue





class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()



    def enqueue(self, animal):

        if animal.pet_type == 'dog':
            self.dog_queue.enqueue(animal)

        if animal.pet_type == 'cat':
            self.cat_queue.enqueue(animal)


    def dequeue(self, animal):
        if animal == 'dog':
            new_pet = self.dog_queue.dequeue()
            return new_pet

        if animal == 'cat':
            new_pet = self.cat_queue.dequeue()
            return new_pet

        else:
            return None


class Dog:
    def __init__(self):
        self.pet_type = 'dog'



class Cat:
    def __init__(self):
        self.pet_type = 'cat'
