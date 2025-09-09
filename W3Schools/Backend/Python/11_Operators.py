# W3Schools - Python
# Section 11: Operators


# Operators perform operations on variables and values.
# Python divides the operators in the following groups.
#   1. Arithmetic
#   2. Assignment
#   3. Comparison
#   4. Logical
#   5. Identity
#   6. Membership
#   7. Bitwise

# Arithmetic operators are used with numeric values to perform common mathemical operations:
#   1. Addition         +
#   2. Subtraction      -
#   3. Multiplication   *
#   4. Division         /
#   5. Modulus          %
#   6. Exponentation    **
#   7. Floor Division   //

# Assigment operators are used to assign values to variables.
# The most notable example is =.
# However, you also have assignment operators that consist of a arithemetic or bitwise operator followed by an equals sign...
# These operators mean that you should perform that arithmetic or bitwise operation on the variable and assign the result of this operation as the variable.
# E.g.: x += 5 means x = x + 5

# Note: you could use the := operator to assign a variable that you can print out.
# For example
'''
x = 3
print(x)
could be written as 
print(x:=3)
'''

# Compariosn operators are used to compare two values:
#   1. ==   -> Equal
#   2. !=   -> Not Equal
#   3. >    -> Greater Than
#   4. <    -> Less Than
#   5. >=   -> Greater Than or Equal To
#   6. <=   -> Less Than or Equal To

# Logical operators are used to combine conditional statements.
# There are three operators:
#   1. and  -> returns True if both statements are True
#   2. or   -> returns True if at least one statement is True
#   3. not  -> reverses the result, if the result is True then False is returned

# Identity operators compare objects to see, not if they are equal, but if they are the same object, with the same memory location.
# There are two identity operators:
#   1. is       -> returns True if both variables are the same object
#   2. is not   -> returns True if both variables are not the same object

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # True
print(x is y) # False

# Membership operators are used to test if a sequence is presented in an object.
# There are two membership operators:
#   1. in       -> returns True if a sequence with the specified value is present in the object
#   2. not in   -> returns True if a sequence with the specified value is not present in the object

# Bitwise operators are used to compare binary numbers
#   1.  &    -> AND : sets each bit to 1 if both bits are 1
#   2.  |    -> OR  : sets each bit to 1 if one of two bits is 1
#   3.  ^    -> XOR : sets each bit to 1 if only one of two bits is 1
#   4.  ~    -> NOT : inverts all bits
#   5.  <<   -> Zero Fill Left Shift : shifts left by pushing zeros in from the right and let the leftmost bits fall off
#   6.  >>   -> Signed Right Shift : shifts right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off