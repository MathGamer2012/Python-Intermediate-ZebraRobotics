myAcc = None 

class BankAccount:

    def __init__(self, name, dollar):
        self.name = name
        self.dollar = dollar
        
    def deposit(self, dollar):
        self.dollar += dollar

    def withdraw(self, dollar):
        self.dollar -= dollar

    def balance(self):
        print(self.dollar) 

while(choice != 5):   
    while(True):
        login = str(input("Type the name of your account here (to add a account type a): "))
        
        if login == "a":
            acc1 = str(input("Type the name of your bank account here: "))
            dollar = 0
            myAcc = BankAccount(acc, dollar)

        else:
            login2 = int(input("Type the pin of your account here: "))
        
        print("Select one of the options: \n 1. Deposit Money \n 2. Withdraw Money \n 3. See Balance \n 4. Log out \n 5. Quit")
        choice = int(input("Your Choice: "))


        if choice == 1:
            question2 = int(input("How much money would you like to deposit: "))
            myAcc.deposit(question2)
            print(myAcc.dollar)

        if choice == 2:
            question4 = int(input("How much money would you like to deposit: ")) 
            myAcc.withdraw(question4)
            print(myAcc.dollar) 

        if choice == 3:
            myAcc.balance()


        if choice == 4:
            break
        



