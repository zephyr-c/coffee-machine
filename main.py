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

def check_resources(drink):
    """Checks that there are sufficient resources to make a drink"""
    w, m, c = [True] * 3
    if drink.get("water", 0) > resources["water"]:
        print("Sorry, not enough water!")
        w = False
    if drink.get("milk", 0) > resources["milk"]:
        print("Sorry, not enough milk!")
        m = False
    if drink.get("coffee", 0) > resources["coffee"]:
        print("Sorry, not enough coffee!")
        c = False
    return w and m and c

def process_coins(p=0, n=0, d=0, q=0):
    """Returns a dollar amount total for given coin inputs"""
    return (p * 0.01) + (n * 0.05) + (d * 0.10) + (q * 0.25)

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

    if not check_resources(recipe):
        print("\n")
        continue

    print(f"Your drink costs ${cost:.2f}")
    print("Please insert your coins")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = process_coins(pennies, nickels, dimes, quarters)

    change = total - cost

    if change < 0:
        print(f"Sorry that's only ${total:.2f}. Returning coins.\n")
        continue

    else:
        print(f"Thank you! Your change is ${change:.2f}")
        resources['money'] += cost

    print("\nMaking your coffee!\n")

    make_coffee(recipe)

    print(f"Here is your {order.capitalize()}. Enjoy!\n")


