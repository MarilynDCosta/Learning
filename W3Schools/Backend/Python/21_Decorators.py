# W3Schools - Python
# Section 21: Decorators

import functools


# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.
def changecase(function):
    def myinner():
        return function().upper()
    return myinner

@changecase
def myfunction(): # This function gets decorated by changecase.
    return "Hello, Marilyn!"

print(myfunction())


# A decorator can be called multiple times.
# You just need to place the decorator above the function you want to decorate.
@changecase
def rickroll():
    return "Never Gonna Give You Up"

print(rickroll())


# Functions that require arguments can also be decorated.
# Just make sure you pass the arguments to the wrapper function.
def uppercase(function):
    def innerfunction(name):
        return function(name).upper()
    return innerfunction

@uppercase
def greeting(name):
    return "Hello " + name + "!"

print(greeting("Marilyn"))


# Sometimes the decorator function has no control over the arguments passed from the decorated function.
# To solve this problem add *args and **kwargs to the wrapper function.
# This would allow the wrapper function to accept any number and any type of arguments, and pass them to the decorated function.
def new_uppercase(function):
    def innerfunction(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return innerfunction

@uppercase
def new_greeting(name):
    return "Hello " + name + "!"

print(greeting("Marilyn"))


# Decorators can accept their own arguments by adding another wrapper level.
def change_multiple_cases(n):
    def changecase(function):
        def myinner():
            if n == 1:
                a = function().lower()
            elif n == 2:
                a = function().upper()
            else:
                a = function.capitalize()
            return a
        return myinner
    return changecase

@change_multiple_cases(1)
def name():
    return "Marilyn"

print(name())


# You can use multiple decorators on one function.
# This is done by placing decorator calls on top of each other.
# The decorators are called in the order they are specified.
def changecase(function):
  def myinner():
    return function().upper()
  return myinner

def addgreeting(function):
  def myinner():
    return "Hello, " + function() + ". Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Marilyn"

print(myfunction())


# Functions in Python have metadata that can be accessed using the __name__ and ___doc___ attributes.
def greeting(name):
    return f"Hello, my name is {name}."

print(greeting.__name__) # greeting


# However, if a function is decorated, the metadata of the original function is lost.
def changecase(function):
  def myinner():
    return function().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__) # myinner


# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
def changecase(function):
  @functools.wraps(function)
  def myinner():
    return function().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__) # myfunction