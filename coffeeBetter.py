# Example coffee shop code with OOP

class Coffee:
    # Constructor
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def check_budget(self, budget):
        # Clean user budget input
        if not isinstance(budget, (int, float)):
            print("Enter float or int for budget")
            exit()
        if budget <= 0:
            print("Sorry, you're flat fucking broke pal")
            exit()

    def get_change(self, budget):
        return budget - self.price

    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
            print(f'You can afford a {self.name} coffee')

            if budget == self.price:
                print("You have no change")
            else:
                print(f'Here is your change, ${self.get_change(budget)}')

            exit('Have a nice day!')


small = Coffee('Small', 2)
regular = Coffee('Regular', 5)
large = Coffee('Large', 6)

try:
    user_budget = float(input('What is your budget? '))
except ValueError:
    exit('Please enter a number')

for coffee in [large, regular, small]:
    coffee.sell(user_budget)
