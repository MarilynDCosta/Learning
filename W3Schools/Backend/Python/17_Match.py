# W3Schools - Python
# Section 17: Match


# The match statement is used to before different actions based on different conditions.
# The match statement can be used to replace writing many if statements.
# The match statement selects one of many code blocks to execute.

# Match statements have the following format:
# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block

# The match expression is evaluated once.
# The value of the expression is compared with the values of each case.
# If there is a match, the associated block of code is executed.

day = 3
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

# You can use the underscore character as the last case value if you want a code block to execute when there are no other matches:
match day:
  case 6:
    print("Today is Saturday.")
  case 7:
    print("Today is Sunday.")
  case _:
    print("Looking forward to the weekend.")

# You can use the pipe character as an operator in the case evaluation to check for more than one value match in one case:
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Weekday")
  case _ :
    print("Weekend")

# You can add if statements in the case evaluation as an extra condition check:
month = 5
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _ :
    pass