# W3Schools - Python
# Section 9: Strings


# Booleans represent one of two values: True or False.
# In programming, you often neeed to kow if an expression is True or False.
# You can evaluate any expression in Python and get either True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer.
print(10>9)  # True
print(10==9) # False
print(10<9)  # False

# When you run a condition in an if statement, Python returns True or False:
a = 150
b = 30

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# The bool() function allows you to evaluate any value and give you True or False in return:
print(bool("Marilyn"))
print(bool(5))

# You can also use the bool() function on variables:
name = "Marilyn"
number = 5
print(bool(name))
print(bool(number))

# Most values are true unless...
#   1. A string is empty.
#   2. A number (decimal or not) is 0.
#   3. A list, tuple or dictionary is empty.
#   4. You use the boolean value False.
#   5. You use the value None

print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(False))  # False
print(bool(None))   # False

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myClass():
    def __len__(self):
        return 0

myObj = myClass()
print(bool(myObj))

# Functions can also return booleans:

def isAGreaterThanB(a, b):
    if a>b:
        return True
    
print(isAGreaterThanB(60,30)) # True

# You can also execute code based on the Boolean answer of a function:
if isAGreaterThanB(60,30):
    print("A is greater than B.")
else:
    print("A is not greater than B.")

# Python also has many in-built functions that return boolean values.
# For instance, the isinstance() function determines if an object is of a certain data type:
x = 20.5
print(isinstance(x, int)) # False