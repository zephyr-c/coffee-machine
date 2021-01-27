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


def sufficient_resources(drink): #come back and refactor for specific deficiencies

    return (drink.get("water", 0) < resources["water"] and
            drink.get("milk", 0) < resources["milk"] and
            drink.get("coffee", 0) < resources["coffee"])

def process_coins(p=0, n=0, d=0, q=0):
    return (p * 0.01) + (n * 0.05) + (d * 0.10) + (q * 0.25)

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
        print("Sorry, not enough something for that drink")  # come back and refactor for specific deficiencies

    print(f"Your drink costs ${cost}")
    print("Please insert your coins")
    pennies = int(input("How many pennies? "))
    nickels = int(input("How many nickels? "))
    dimes = int(input("How many dimes? "))
    quarters = int(input("How many quarters?"))
    total = process_coins(pennies, nickels, dimes, quarters)

    change = total - cost

    if change < 0:
        print("Sorry that's not enough. Returning coins.")

    else:
        print(f"Thank you! Your change is ${change}")

    resources['money'] += cost

    resources['coffee'] -= recipe.get('coffee', 0)
    resources['water'] -= recipe.get('water', 0)
    resources['milk'] -= recipe.get('milk', 0)

    print(f"Here is your {order.capitalize()}. Enjoy!")



# TODO: 1. Check if resources are sufficient for ordered drink
# TODO: 2. Deduct required resources
# TODO: 3. Process coins


