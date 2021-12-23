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


# from youtube
class AnimalFishAdapter(Animal): 
    def __init__(self, fish: Fish):    
        self.fish = fish
    def walk(self):
        self.fish.swim()

# Me trying differnet way
# class AnimalFishAdapter(Animal): 
#     def __init__(self, animal: Animal):
#         self.animal = animal
#     def walk(self):
#         if isinstance(self.animal , Fish):
#             self.animal.swim()
#         elif isinstance(self.animal, Dog):
#             self.animal.walk()
#         else:
            # print("invalid instance!!")
            
print("----")
makeWalk(AnimalFishAdapter(nemo))
# makeWalk(AnimalFishAdapter(bingo))
# makeWalk(AnimalFishAdapter(kitty))
