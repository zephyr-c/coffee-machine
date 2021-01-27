##################### Setup Information #####################
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

def sufficient_resources(drink): #come back and refactor for specific deficiencies

    return (drink.get("water", 0) < resources["water"] and
            drink.get("milk", 0) < resources["milk"] and
            drink.get("coffee", 0) < resources["coffee"])

def process_coins(p=0, n=0, d=0, q=0):
    return (p * 0.01) + (n * 0.05) + (d * 0.10) + (q * 0.25)

def make_coffee(recipe):
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
        print("Sorry, not enough something for that drink")

    print(f"Your drink costs ${cost:.2f}")
    print("Please insert your coins")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = process_coins(pennies, nickels, dimes, quarters)

    change = total - cost

    if change < 0:
        print("Sorry that's not enough. Returning coins.\n")
        continue

    else:
        print(f"Thank you! Your change is ${change:.2f}")
        resources['money'] += cost

    print("\nMaking your coffee!\n")

    make_coffee(recipe)

    print(f"Here is your {order.capitalize()}. Enjoy!\n")


