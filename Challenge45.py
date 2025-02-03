class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print("The name of the hippo is " + str(self.name) + ".")
        print("The age of the hippo is " + str(self.age) + ".")


John = Animal("John", 15)

John.description()
    
    
        






