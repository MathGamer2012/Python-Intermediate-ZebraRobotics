
inventory = { "001": ["Apple", 2],
             "002": ["Mago", 5],
             "003": ["Chocolate", 10],
             "004": ["Toy", 15],
             "005": ["Grapes", 6],
             "006": ["Soccer ball", 20],
             "007": ["Basket ball", 20],
             "008": ["Tennis ball", 3],
             "009": ["PS4", 399],
             "010": ["Nintendo Switch", 399],
             "011": ["Xbox", 399],
             "012": ["Console games", 79],
            }


class ShoppingCart:

    def __init__(self):
        self.cart = [] 
        self.price = 0

    
    def add(self):
        print("This is what we have at our store",inventory)
        question = input("What item do you want to add to your cart (Type item id): ")
        self.cart.append(inventory[question])
        print("This is your cart", self.cart)


    def remove(self):
        print(self.cart)
        question2 = str(input("What item do you want to delete from your cart (Type the name of the item, case-sensetive): "))

        for i in range(len(self.cart)):
            if question2 == self.cart[i][0]:
                self.cart.remove(self.cart[i])

        print("This is your cart after removing the item", self.cart)

    def view(self):
        print("This is your cart", self.cart)

    def cash(self):
        finalSum = 0
        for s in range(0,len(self.cart)):
            finalSum = finalSum + self.cart[s][1]
               
        print("The total amount of money you need to pay is(not including tax)", finalSum)


myCartObj = ShoppingCart()
        
while(True):
    print("Select one of the options: \n 1. Add to your cart \n 2. Remove from Cart \n 3. View Cart \n 4. Check out")
    choice = int(input("Your Choice: "))
    if choice == 1:
        myCartObj.add()

    if choice == 2:
        myCartObj.remove()

    if choice == 3:
        myCartObj.view()

    if choice == 4:
        myCartObj.cash()
        break
        



        



