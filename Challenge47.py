class Customer:

    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("I'm a string that stands in for the contents of your cart")

class ReturningCustomer(Customer):
    
    def display_order_history(self):
        print("I'm a string that stands in for your order history!")

RandomDude = Customer("ID: 18290")
RandomDude.display_cart()
RandomDude.display_order_history()

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart() 
monty_python.display_order_history()
