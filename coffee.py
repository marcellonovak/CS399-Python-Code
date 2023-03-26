# Example coffee shop code

small = 2
regular = 5
large = 6

budget = input("How much money do you have? ")

try:
    budget = int(budget)
except ValueError:
    print("Please enter a number")
    exit()  # exit vs quit?

if budget > 0:
    if budget >= large:
        print("You can afford a large coffee")
        if budget == large:
            print("You have no change")
        else:
            print("Your change is", budget - large)

    elif budget >= regular:
        print("You can afford a regular coffee")
        if budget == regular:
            print("You have no change")
        else:
            print("Your change is", budget - regular)

    elif budget >= small:
        print("You can afford a small coffee")
        if budget == small:
            print("You have no change")
        else:
            print("Your change is", budget - small)
