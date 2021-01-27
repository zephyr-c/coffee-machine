##################### Setup Information #####################
import time
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

##################### Helper Functions #####################

def sufficient_resources(drink):
    """Returns True if resources are sufficent for drink, False otherwise"""
    for item in drink.keys():
        if drink[item] > resources[item]:
            print(f"Sorry! Not enough {item}.")
            return False
    return True

def process_coins():
    """Returns a dollar amount total for given coin inputs"""

    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01

    return total

def make_coffee(recipe):
    """Deducts the necessary resources from the coffee machine to make a drink"""
    resources['coffee'] -= recipe.get('coffee', 0)
    resources['water'] -= recipe.get('water', 0)
    resources['milk'] -= recipe.get('milk', 0)


##################### Machine Actions #####################

while True:
    print("Welcome to the Coffee Machine")
    print("What would you like to order?")
    print("Menu: espresso, latte, cappuccino")
    order = input()
    if order == 'report':
        for resource, amount in resources.items():
            print(f"{resource.capitalize()}: {amount}")
        print("\n")
        continue

    if order == 'off':
        break

    recipe = MENU[order]['ingredients']
    cost = MENU[order]['cost']

    if not sufficient_resources(recipe):
        print("\n")
        continue

    print(f"Your drink costs ${cost:.2f}")
    print("Please insert your coins")

    total = process_coins()

    change = total - cost

    if change < 0:
        print(f"Sorry that's only ${total:.2f}. Returning coins.\n")
        continue

    else:
        print(f"Thank you! Your change is ${change:.2f}")
        resources['money'] += cost

    print("\n🧑‍🍳 Making your coffee! 🧑‍🍳\n")

    make_coffee(recipe)

    print(f"Here is your {order.capitalize()} ☕. Enjoy!\n")


