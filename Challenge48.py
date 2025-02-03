class Employee:
    
    def __init__(self, name):
        self.name = name
    
    def wage(self):
        money = 20
        time = int(input("Type the amount of hours you work: "))
        total = money * time
        print("Your total wage is", total, "dollars")


class partTime:

    def __init__(self, name):
        self.name = name

    def wage(self):
        money2 = 12
        time2 = int(input("Type the amount of hours you work: "))
        total2 = money2 * time2
        print("Your total wage is", total2, "dollars")
                
def checkTo():
    check = input("Are you a part time employee:(Y for Yes)(N for No): ")
    nom = input("Type your name here: ")

    if check == "Y" or check == "y":
        nom = partTime(nom)
        nom.wage()

    elif check == "N" or check == "n":
        nom = Employee(nom)
        nom.wage()


checkTo()

    








