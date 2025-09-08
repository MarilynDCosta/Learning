# W3Schools - Python
# Section 7: Numbers


# There are 3 types of number in Python:
#   1. int
#   2. float
#   3. complex

# Variables of numeric types are created when you assign a value to them:
x = 1   # int
y = 2.5 # float
z = 1j  # complex

# To find the type of any numeric object in Python, use type():
print(type(x))
print(type(y))
print(type(z))

# Integer (Int) is a whole positive or negative number, without decimals, of unlimited length.

# Float is a positive or negative number, containing one or more decimals.
# Floats can also be scientific numbers with an "e" to indicate the power of 10:
scientific_float1 = 35e3
scientific_float2 = 12E4
scientific_float3 = -87.7e100

print(type(scientific_float1))
print(type(scientific_float2))
print(type(scientific_float3))

# Complex numbers are written with a "j" as the imaginary part.

# You can convert from one type to another with the int(), float() and complex() methods:

# Convert from int to float:
a = float(x)

# Convert from float to int:
b = int(y) # As y was a float before, it is simply truncated.

# Convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Python does not have a random() function to make a random number.
# However, Python does have a built-in module called random that can make random numbers:

import random
print(random.randrange(1,11)) # Displays a random number from 1 to 10