#!/usr/bin/env python3

#Creating Unlimited arguments e.g add any number of arguments
# add *args in the parameter
#args = tuple

def add(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add(2, 2, 2, 2 ,4, 5, 6, 7, 8, 9, 10))

# **kwargs limitless keyword arguments

def calculate(number,**kwargs):
    # kwargs = dictionary
    number+=kwargs['add']
    number+=kwargs['multiply']    
    return number

    
print(calculate(10, add =3, multiply = 5))

class Car:
    def __init__(self,**kw):
        self.wheel = 4
        self.make = kw.get("make")
        self.model = kw.get("model")

        # benefit of get in dict, will returns none if there is no arguments

my_car = Car(make = 'Nissan', model = 'GTR')
print(my_car.model)
my_car2 = Car() # if it wasnt specified, it may result in key error
print(my_car2.make)
