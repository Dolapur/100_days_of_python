#!/usr/bin/python3
"""coffee_machine module"""


# Avaliable resources in the coffee machine
amount = [0.25, 0.10, 0.05, 0.01]

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

def avaliable_drinks(drinks):
    """Prints the price for each drink"""
    for drink in drinks:
        print(f"{drink}: ${drinks[drink]}")

def serving(drinks):
    """Prompts customer to enter request and returns the request"""
    customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    for drink in drinks:
        if customer_input == drink:
            return customer_input
        elif customer_input != drink:
            return "Enter the listed drinks"

def check_resources(drinks, resources, customer_input, recipes):
    """Checks the availability of resources for the customer's
    request and returns True if enough resources
    """
    if customer_input in drinks:
        for drink in recipeis.keys():
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


def check_transaction(customer_input, total, drinks, resources):
    """Checks if customer has inserted enough money for drink requested"""
    if customer_input == "espresso" and total == drinks["espresso"]:
        resources["Money"] += total
        print(f"Here is your {customer_input}. Enjoy!")

    elif customer_input == "espresso" and total > drinks["espresso"]:
        customer_bal = total - drinks["espresso"]
        resources["Money"] += drinks["espresso"]
        print(f"${round(customer_bal, 2)} balance refunded, Thanks!")
        print(f"Here is your {customer_input}. Enjoy!") 

    elif customer_input == "latte" and total == drinks["latte"]:       
        resources["Money"] += total                           
        print(f"Here is your {customer_input}. Enjoy!") 

    elif customer_input == "latte" and total > drinks["latte"]:   
        customer_bal = total - drinks["latte"]  
        resources["Money"] += drinks["latte"]   
        print(f"${round(customer_bal, 2)} balance refunded, Thanks!")  
        print(f"Here is your {customer_input}. Enjoy!")                                                                                     
    elif customer_input == "cappuccino" and total == drinks["cappuccino"]:   
        resources["Money"] += total        
        print(f"Here is your {customer_input}. Enjoy!") 

    elif customer_input == "cappuccino" and total > drinks["cappuccino"]:  
        customer_bal = total - drinks["cappuccino"]    
        resources["Money"] += drinks["cappuccino"]         
        print(f"${round(customer_bal, 2)} balance refunded, Thanks!")             
        print(f"Here is your {customer_input}. Enjoy!") 
    else:
        print("Sorry that's not enough money. Money refunded.")


continue_serving = True

while continue_serving:
    print("Hi, Welcome to my coffee shop!")
    print()
    print(f"Resources Avaliable:\n{resource_report(resources)}")
    print()
    avaliable_drinks(drinks)
    print()

    customer_input = serving(drinks)
    print()

    check_resources(drinks, resources, customer_input, recipes)
    amount = input("Enter a representation of amount separated with space (quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01): ")

    total = process_coin(amount) 
    print(f"Total money entered: ${total}\n") 
    
    transaction = check_transaction(customer_input, total, drinks, resources)
    print(f"{transaction}\n")

    print(f"Current Resources Avaliable:\n{resource_report(resources)}")
    coffee_machine = input("For maintenance of the coffee machine, Enter 'off' to turnoff or 'ignore' to proceed: ").lower()
    if coffee_machine == "off":
        continue_serving = False
        print("Coffee machine down, Try again later")


