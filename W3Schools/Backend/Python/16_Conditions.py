# W3Schools - Python
# Section 16: Conditions and If Statements


# Python supports the usual logical conditions from mathematics.
# -> Equals                     ==
# -> Not Equals                 !=
# -> Less Than                  <
# -> Less Than or Equal To      <=
# -> Greater Than               >
# -> Greater Than or Equal To   >=

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# If statements are written by using using the if keyword.
a = 3
b = 4
if b > a:
    print("b is greater than a.")

# Python relies on indentation to define the scope in the code.
# Other programming languages often use curly brackets for this purpose.

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
if b < a:
    print("b is less than a.")
elif b > a:
    print("b is greater than a.")

# The else keyword catches anything which is not caught by preceding conditions.
if b < a:
    print("b is less than a.")
elif b == a:
    print("b is equal to a.")
else:
    print("b is greater than a.")

# If you only have one statement to execute, you can put it on the same line as the if statement
if b > a: print(True)

# You can also do this if you have one statement to execute 
print(True) if b < a else print(False)

# You can also have multiple else statements on the same line:
print("<") if b < a else print("=") if b == a else print(">")

# The and keyword is a logical operator that can be used to combine conditional statements.
c = 200
if b > a and c > a: print("a has the smallest number.")

# The Or keyword is a logical operator that can also combine conditional statements:
if b > c or c > a: print("At least one of these conditions is True.")

# The note keyword is a logical operator that can be used to reverse the result of the conditional statement.
if not a > c: print("a is not greater than c.")

# You can also have nested if statements, which are if statements inside if statements.
if c > a:
    print("c is greater than a.")
    if c > b:
        print("c is the highest number as it is also greater than b.")

# If statements cannot be empty byt if you have an if statement with no content, put in the pass statement to avoid getting errors.
if c > b: pass