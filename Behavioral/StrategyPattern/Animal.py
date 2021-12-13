# https://www.youtube.com/watch?v=gJZPZRqEv6E&list=PLDV-cCQnUlIaGcUNSYWeDpHy_3RlMgFkU&index=2

class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Lion(Animal):
    def speak(self):
        print("roar")

# this function doen't need to have any if-statement
def makeSpeak(animal: Animal):
    animal.speak()

def createAnimal(input_str: str) -> Animal:
    if input_str == "cat":
        return Cat()
    elif input_str == 'lion':
        return Lion()


# test code (dumb)
cat = Cat()
lion = Lion()
makeSpeak(cat)
makeSpeak(lion)

# test code (smarter)
input_str = input('choose animal: ')
animal = createAnimal(input_str)
makeSpeak(animal)

