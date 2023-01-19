#!/usr/bin/python3
"""coffee_machine module"""


# Avaliable resources in the coffee machine

resources = {
        'Water': 1000,
        'Milk': 600,
        'Coffee': 500,
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

def prices(drinks):
    """Prints the price for each drink"""
    for drink in drinks:
        print(f"{drink}: ${drinks[drink]}")


def serving(drinks):
    """Prompts customer to enter his/her request and returns the request"""
    user = False
    while not user:
        customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        for drink in drinks:
            if customer_input == drink:
                user = True
                return "customer_input"
            elif customer_input == "report":
                return "report"
            elif customer_input == "off":
                return "off"

def resource_report(resources):
    """Prints the current resources and it's available values"""
    resource_water = resources["Water"]
    resource_milk = resources["Milk"]
    resource_coffee = resources["Coffee"]
    resource_money = resources["Money"]
    return(f"{resource_water}ml\n{resource_milk}ml\n{resource_coffee}g\n${resource_money}")


def process_coin(prices, customer_input):
    """Process user currency"""
    print("Please insert coins.")
    total_money = int(input("how many quarters?: ")) * 0.25
    total_money += int(input("how many dimes?: ")) * 0.1
    total_money += int(input("how many nickles?: ")) * 0.05
    total_money += int(input("how many pennies?: ")) * 0.01
    return total_money


continue_serving = True
while continue_serving:
    print("Hi, Welcome to my coffee shop!")
    print()
    prices(drinks)  
    print()

    customer_input = serving(drinks)
    if customer_input == "off":
        print("Goodbye")
        continue_serving = False
    elif customer_input == "report":
        print()
        print(f"Resources Avaliable:\n{resource_report(resources)}")
        print()
    else:
        sufficient_resource= check_resources(drinks, resources, customer_input, recipes)
        total_money = process_coin(customer_input, prices) 
        print(f"Total money entered: ${total_money}\n") 
        transaction = check_transaction(customer_input, total_money, drinks, resources)
        print(f"{transaction}\n")

