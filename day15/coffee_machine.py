#!/usr/bin/python3
"""coffee_machine module"""


MENU = {   
    "espresso": {       
        "ingredients": {    
            "water": 50,  
            "coffee": 18,
            "milk": 10,
        },         
        "cost": 1.5,       
    },         
    "latte": {    
        "ingredients": {   
            "water": 200,   
            "coffee": 150, 
            "milk": 35,    
        },       
        "cost": 2.5,  
    },      
    "cappuccino": {     
        "ingredients": {    
            "water": 250,  
            "coffee": 130,   
            "milk": 50,     
        },      
        "cost": 3.0,    
    },         
}

profit = 0.0

resources = {        
    'water': 1000,      
    'milk': 600,     
    'coffee':500    
}


# Names of drinks and their prices
drinks = {
    'espresso': 1.50,
    'latte': 2.50,
    'cappuccino': 3.00
}


def prices(drinks):
    """Prints the price for each drink"""
    for drink in drinks:
        print(f"{drink}: ${drinks[drink]}")

def resource_report(resources):
    """Prints the current resources and it's available values"""
    resource_water = resources["water"]
    resource_milk = resources["milk"]
    resource_coffee = resources["coffee"]
    return(f"{resource_water}ml\n{resource_milk}ml\n{resource_coffee}g\n${profit}")


def process_coin():
    """Process user currency"""
    print("Please insert coins.")
    total_money = int(input("how many quarters?: ")) * 0.25
    total_money += int(input("how many dimes?: ")) * 0.1
    total_money += int(input("how many nickles?: ")) * 0.05
    total_money += int(input("how many pennies?: ")) * 0.01
    return total_money

def check_resources(inputs):
    for item in inputs:
        if inputs[item] >= resources[item]:
            print(f"Sorry, there's not enough [item]")
    return True

def check_transaction(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is {change} change refunded")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money, Money refunded")
        return False

def make_coffee(name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here's your {name}. Enjoy!")


continue_serving = True
while continue_serving:
    print("Hi, Welcome to my coffee shop!")
    print()
    prices(drinks)  
    print()
  
    customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    try:
        if customer_input == "off":
            print("Goodbye")
            continue_serving = False
        elif customer_input == "report":
            print()
            print(f"Resources Avaliable:\n{resource_report(resources)}")
            print()
        elif customer_input is  "espresso" or "latte" or "cappuccino":
            drink = MENU[customer_input]
            if check_resources(drink['ingredients']):
                payment = process_coin()
                print(f"Total money entered: ${payment}\n") 
                if check_transaction(payment, drink['cost']):
                    make_coffee(customer_input, drink['ingredients'])
                    print()
    except KeyError:
        print(f"{customer_input} not listed in the coffee names")
        print()
        break
