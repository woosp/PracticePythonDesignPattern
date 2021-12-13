class Animal:
    def walk(self):
        pass

class Cat(Animal):
    def walk(self):
        print("cat walking")

class Dog(Animal):
    def walk(self):
        print("dog walking")


def makeWalk(animal : Animal):
    animal.walk()



class Fish:
    def swim(self):
        print("fish swimming")

kitty = Cat()
bingo = Dog()
nemo = Fish()
makeWalk(kitty)
makeWalk(bingo)
# makeWalk(nemo)


class AnimalFishAdapter(Animal): 
    def __init__(self, fish: Fish): 
        self.fish = fish
    def walk(self):
        self.fish.swim()

makeWalk(AnimalFishAdapter(nemo))
