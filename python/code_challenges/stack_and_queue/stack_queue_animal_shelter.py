from nis import cat
from stack import Stack

class Cat:
    def __init__(self, name=None):
        self.name = name
        self.type = "cat"
    
class Dog:
    def __init__(self, name=None):
        self.name = name
        self.type = "dog"

class AnimalShelter:
    def __init__(self):
        self.pets = Stack()
        self.holding = Stack()
        self.adopting = None

    def enqueue(self, animal):
        while self.pets.top != None:
            self.holding.push(self.pets.pop())
        self.pets.push(animal)
        while self.holding.top != None:
            self.pets.push(self.holding.pop())

    def dequeue(self, pref):
        if self.pets != None:
            while self.pets.top != None:
                if pref == "cat" or pref == "dog":
                    if self.pets.top.value.type == pref:
                        self.adopting = self.pets.pop()
                        break
                    else:
                        self.holding.push(self.pets.pop())
                else:
                    self.adopting = self.pets.pop()
                    break
            while self.holding.top != None:
                self.pets.push(self.holding.pop())
            return self.adopting
        else:
            return "Everyone got adopted!"
