# W3Schools - Python
# Section 5: Variables


# PYTHON VARIABLES

# To create a variable you must assign a value to it:
n = 5
print(n)
name1 = "Marilyn"
print("Hello", name1)

# In Python, one can change between data types:
n = True # changes x from an integer into a boolean
print(n)

# If you want to specifiy the data type of a variable, you can use casting:
x=int(5)
y=float(3)
z=str(3)
print(x + x) # results in an integer
print(x + y) # results in a float because y was assigned as a float
# print(x+z) would not work because z is assigned as a string and is '3'

# Use type() to get the data type of a variable:
print(type(x)) # integer

# For declaring string variables, you can use either single or double quotes:
name2 = "John"
name2 = 'John'

# Variables as case sensitive:
x = 2
X = 4
print(x + X) # 6


# VARIABLE NAMES

# Variable naming rules for Python:
#   1. A variable name must start with a letter or the underscore character.
#   2. A variable name cannot start with a number.
#   3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
#   4. Variable names are case-sensitive (age, Age and AGE are three different variables).
#   5. A variable name cannot be any of the Python keywords.

# Naming conventions:
#   1. Camel Case  -> each word except the first starts with a capital letter
#   2. Pascal Case -> each word starts with a capital letter
#   3. Snake Case  -> each word is separated with an underscore
camelCase = "My name"
PascalCase = " is "
snake_case = "Marilyn."


# ASSIGNING MULTIPLE VALUES

# You can assign values to multiple variables in one line:
a, b, c = "Biscuits", "Fruits", "Chocolate"

# Likewise, you can also assign the same value to multiple variables:
a = b = c = 1

# If you have a collection of values, e.g.: lists or tuples, Pythin can extract the values into variables, known as unpacking:
shopping_list = ["Biscuits", "Fruits", "Chocolate"]
a1, b1, c1 = shopping_list
print(a1)
print(b1)
print(c1)


# OUTPUT VARIABLES

# You can use print() to output variables
greeting = "My name is Marilyn."
print(greeting)

# You can also output multiple variables by separating the variables with commas:
print(a1, b1, c1) # Biscuits, Fruits, Chocolate

# For numbers, you can use + as a mathematical operator
print(a + b) # 2

# In the print() function, if you combine a string and a number with a + operator, there will be an error.
# The best way to avoid this error is comma separation.
number = 5
name = "Marilyn"
print(number, name) # 5 Marilyn


# GLOBAL VARIABLES

# Global variables are variables created outside of a function.
# These variables can be used inside functions and outside them too.

compliment1 = "awesome"

def pythonComplimenter():
    print("Python is", compliment1)

pythonComplimenter()

# If you create a variable with the same name inside a function, this variable will be local and can only be use inside the function.
# The global variable with the same name will remane as it was.

def peopleComplimenter():
    compliment1 = "fantastic"
    print("You are", compliment1)

peopleComplimenter()

print("Python is", compliment1)

# To create a global variable inside a function, use the global keyword:
def bathComplimenter():
    global compliment1 
    compliment1 = "cool"

bathComplimenter()

print("Python is", compliment1) # Python is cool