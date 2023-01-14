#!/usr/bin/python3
"""coffee_machine module"""


# Avaliable resources in the coffee machine
resources = {
        'Water': 80000,
        'Milk': 50000,
        'Coffee': 20000,
        'Money': 0.0
}

# Names of drinks and their prices
drinks = {
        'espresso': 1.25,
        'latte': 2.50,
        'cappuccino': 2.13
}

# Recipe detail for coffee
recipes = {
        'espresso': {
            'water': 150,
            'milk':  50,
            'coffee': 70,
        },
        'latte':  {
            'water': 200,
            'milk': 90,
            'coffee': 100,
        },
        'cappuccino': {
            'water':250,
            'milk': 70,
            'coffee': 90,
        }
}

def serving(drinks):
    """Prompts customer to enter his/her request and returns the request"""
    customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    for drink in drinks:
        if customer_input == drink:
            return customer_input

def check_resources(drinks, resources, request_, recipes):
    """Checks the availability of resources for the customer's
    request and returns True if enough resources
    """
    if customer_input in drinks:
        for drink in recipes.keys():
            if customer_input == drink:
                for recipe, quantity in recipes[drink].items():
                    if recipe == "water" and resources["Water"] > quantity:
                        resources["Water"] -= quantity
                    elif recipe == "milk" and resources["Milk"] > quantity:
                        resources["Milk"] -= quantity
                    elif recipe == "coffee" and resources["Coffee"] > quantity:
                        resources["Coffee"] -= quantity
                    else:
                        print(f"Sorry there is not enough {recipe}.")
                break

def resource_report(resources):
    """Prints the current resources and it's available values"""
    resource_water = resources["Water"]
    resource_milk = resources["Milk"]
    resource_coffee = resources["Coffee"]
    resource_money = resources["Money"]
    return(f"{resource_water}ml\n{resource_milk}ml\n{resource_coffee}g\n${resource_money}")

def process_coin(amount):
    """Process user currency"""
    total = 0.0
    coins = amount.split(" ")
    for coin in range(0, len(coins)):
        total += float(coins[coin])
    return total

continue_serving = True

while continue_serving:
    print("Hi, Welcome!")
    print(f"Resources Avaliable:\n{resource_report(resources)}")
    customer_input = serving(drinks)
    check_resources(drinks, resources, customer_input, recipes)
    amount = input("Enter a list of amount separated with space (quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01): ")
    total = process_coin(amount)
    print(total)
    print(f"Current Resources Avaliable:\n{resource_report(resources)}")
    coffee_machine = input("For maintenance of the coffee machine, Enter 'off' to turnoff or 'ignore' to proceed: ").lower()
    if coffee_machine == "off":
        continue_serving = False
        print("Coffee machine down, Try again later")


