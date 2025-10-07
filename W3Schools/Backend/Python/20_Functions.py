# W3Schools - Python
# Section 20: Functions


# Functions are blocks of code that run only when they are called.
# You can pass data, known as parameters into a function.
# A function can return data as a result.
def greeting(name):
    print("Hello, I am", name + ".")

greeting("Marilyn")

# To call a function, you can use a function name followed by parenthesis.
def hello_world():
    print("Hello World!")

hello_world()

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want but make sure to separate them with a comma.
def shop(item, price):
    print("The", item, "is", price + ".")

shop("apple", "45p")
shop("lemon","30p")
shop("banana", "35p")

# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
# If you do not call the function with the right amount of arguments, you will get an error.

# If you do not know how many arguments to pass into a function, add a * before the parameter name in the function description.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def sisters(*girls):
    print(", ".join(girls[:-1]), "and", girls[-1], "are sisters.")

sisters("Veronica", "Fiona", "Marilyn")

# You can also send arguments with the key = value syntax.
def three_sisters(sister1, sister2, sister3):
    print(sister1 + ",", sister2, "and", sister3, "are sisters.")

three_sisters("Veronica", "Fiona", "Marilyn")

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def greeting(**name):
    print("My name is", name["first_name"], name["surname"] + ".")

greeting(first_name = "Marilyn", middle_name = "Raquel", surname = "D'Costa")

# If we call a function without an argument, you can use a default value:
def languages(language = "English"):
    print("I can speak", language + ".")

languages()
languages("French")
languages("German")
languages("Latin")

# You can send any data types of argument to a function and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def shopping(food):
    print("You need to buy:")
    for x in food: print(x)

shopping(["apples", "pears"])

# To let a function return a value, use the return statement:
def multiply_by_five(x):
    return [5*y for y in x]

print(multiply_by_five(range(11)))

# Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def nothing():
    pass

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
def triangle_area(base, height, /): # base and height are positional arguments.
    area = (base / 2) * height
    return f"The area of the triangle is {area}."

print(triangle_area(6,3))

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def rectangle_area(base, height):
    area = base * height
    return f"The area of the rectangle is {area}."

print(rectangle_area(base = 2, height = 4))
# Note that if you added the , / to the rectangle_area function, you will receive an error if you try to send a keyword argument.

# To specify that a function can have only keyword arguments, add *, before the arguments:
def cylinder_volume(radius, height, *, units='cm^3'): # units is a keyword argument.
    volume = 3.142 * radius**2 * height
    return f"The volume of the cylinder is {volume}{units}."

print(cylinder_volume(3, 6))
print(cylinder_volume(3, 6, units = 'mm^3'))

# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:
def triangular_prism_volume(base, height, length, units='cm^3'):
    volume = 1/2 * base * height * length
    return f"The volume of the traingular prism is {volume}{units}."

print(triangular_prism_volume(6, 3, 6))
print(triangular_prism_volume(6, 3, 6, 'mm^3'))
print(triangular_prism_volume(6, 3, 6, units = 'm^3'))
# However, note that, with the *, you will get an error if you try to send a positional argument instead of a keyword argument.

# You can combine both positional and keyword argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def add(a, b, /, *, c, d): # a and b are positional arguments; c and d are keyword arguments
  print(a + b + c + d)

add(5, 6, c = 7, d = 8)

# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion 
# as it can be quite easy to slip into writing a function which never terminates, 
# or one that uses excess amounts of memory or processor power. 
# However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# A notable example of recursion is the Fibonacci sequence:
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
print(fibonacci(6))

