#!/usr/bin/python3

def add(n1, n2):
    return (n1 + n2)

def substract(n1, n2):
    return (n1 - n2)

def multiply(n1, n2):
    return (n1 * n2)

def divide(n1, n2):
    return (n1 / n2)

operations = {
   "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = float(input("What's the first number?: ")) 

    for i in operations:
        print(i)

    calc_continuation = True

    while calc_continuation:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calc_continuation = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type 'exit' to switch the calculator off : ")
        if calc_continuation == "y":
            num1 = answer
        elif calc_continuation == "exit":
            print("Calculator Off")
            break
        else:
            calc_continuation = False
            calculator()


calculator()






