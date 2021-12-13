# Youtube: https://www.youtube.com/watch?v=bUULgkwaicQ&list=PLDV-cCQnUlIaGcUNSYWeDpHy_3RlMgFkU&index=5
# Wiki: https://en.wikipedia.org/wiki/Command_pattern

# base interface
class Command:
    def execute(self):
        pass

class PrintCommand(Command):
    def __init__(self, print_str:str):
        self.print_str = print_str

    def execute(self):
        print(f"from print command: {self.print_str}")


# test code
first_command = PrintCommand("first command")
second_command = PrintCommand("second command")
first_command.execute()
second_command.execute()

# receiver 
class Dog:
    def sit(self):
        print("dog sat down")
    def stay(self):
        print("dog is staying")
    def speak(self):
        print("dog is barking")

class DogCommand(Command):
    def __init__(self, dog:Dog, commands):
        self.dog = dog
        self.commands = commands

    def execute(self):
        for command in self.commands:
            if command == "sit":
                self.dog.sit()
            elif command == "stay":
                self.dog.stay()
            elif command == "speak":
                self.dog.speak()

# test code
baduk = Dog()
dogCommand = DogCommand(baduk, ["sit", "speak", "stay", "stay"])
dogCommand.execute()


# Invoker Class
class Invoker:
    def __init__(self):
        self.command_list = []

    def addCommand(self, command: Command):
        self.command_list.append(command)

    def runCommands(self):
        for each_cmd in self.command_list:
            each_cmd.execute()

# test code
print("------")
invoker = Invoker()
invoker.addCommand(first_command)
invoker.addCommand(dogCommand)
invoker.addCommand(second_command)
invoker.runCommands()


