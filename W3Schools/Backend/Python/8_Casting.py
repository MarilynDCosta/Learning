# W3Schools - Python
# Section 8: Casting


# Casting can be used to specify data types on a variable.
# Because Python is an object-oriented language, it uses classes to define data types.
# Casting in Python is therefore done using constuctor functions such as...
#   1. int()
#   2. float()
#   3. str()

# Note: Strings can only be converted into integers or floats if the string represents a number:
w = int("3")
x = float("8")
y = int(3.8) # When converting a float into an integer, truncation is used.
# z = int("3.8") -> You cannot convert a string decimal number into an integer.

# Note: You can convert scientific numbers written as strings into floats.
a = float("-87.7e100")

print(w, x, y, a)