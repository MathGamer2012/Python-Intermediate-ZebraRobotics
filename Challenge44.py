class Animal:

    def __init__(self, name, legs, hungry):
        self.name = name
        self.legs = legs
        self.hungry = False

    def printInfo(self):
        print("I have " + str(self.legs) + " legs")
        print(str(self.hungry) + " I am not hungry")



Jeff = Animal("Jeff", 4, True)
Bob = Animal("Bob", 6, False)
Logan = Animal("Logan", 8, False)

Jeff.printInfo()
Bob.printInfo()
Logan.printInfo()


