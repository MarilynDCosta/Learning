# W3Schools - Python
# Section 13: Tuples


# PYTHON TUPLES

# Tuples are another data collevtion used to store multiple items in a single variable.
# Tuples are ordered and unchangeable.
# Tuples are written with rounded brackets:
flowers = ("Lily", "Rose", "Peony")
print(flowers) # ("Lily", "Rose", "Peony")

# Tuple items...
#   1. Are Ordered      -> All items have a defined order that will not change
#   2. Unchangeable     -> Items cannot be changed, added or removed after a tuple has been created.
#   3. Allow Duplicates -> As tuples are indexed, they can have items with the same value.
flowers2 = ("Lily", "Rose", "Peony", "Lily")
print(flowers2)

# To determine how many items a tuple has, use the len() function:
print(len(flowers)) # 3

# To create a tuple with only one item, you have to add a comma after the item or Python will not recognise it as a tuple:
word = ("Hello")
print(type(word)) # String
word = ("Hello",)
print(type(word)) # Tuple

# Tuples can be of any data type:
integers = (1, 2, 3, 4, 5)
floats = (0.1, 0.2, 0.3, 0.4, 0.5)
booleans = (True, False, True, True, False)

# Tuples can also contain different data types:
mixedTypes = (1, "Marilyn", 0.25, True)

# Tuples are defined as objects with the data type 'tuple'.

# You can also use the tuple() constructor to create a tuple:
chocolates = tuple(("Lindt", "Celebrations", "Heroes", "Roses", "Ferrero Rocher"))
print(chocolates)


# ACCESSING TUPLE ITEMS

# You can access tuple items by referring to the index number, inside square brackets:
print(chocolates[1]) # "Celebrations"

# You can also use negative indexing to find items closer to the end of the tuple:
print(chocolates[-3]) # Heroes

# You can specify a range of indexes by specifying where to start and end the range:
print(chocolates[2:5]) # ("Heroes", "Roses", "Ferrero Rocher")

# By leaving out the start value, the range will start at the first item:
print(chocolates[:3]) # ("Lindt", "Celebrations", "Heroes")

# By leaving out the end value, the range will go on to the end of the tuple:
print(chocolates[3:]) # ("Roses", "Ferrero Rocher")

# If you want to start the search from the end of the tuple, specify negative indexes:
print(chocolates[-4:-2]) # ("Celebrations", "Heroes")

# To check if a specified item is present in a tuple, use the in keyword:
if "Lindt" in chocolates:
    print("I love Lindt!")


# UPDATING TUPLES

# Because tuples are unchangeable, you cannot change, add or remove items once a tuple is created.
# However, there are some workarounds.

# To change tuple values, you can convert a tuple into a list that you can change values in and then convert this list back into a tuple.
chocolatesList = list(chocolates)
chocolatesList[-2] = "Guylian"
chocolates = tuple(chocolatesList)
print(chocolates) # ("Lindt", "Celebrations", "Heroes", "Guylian", "Ferrero Rocher")

# To add tuple values, you can do the same thing:
chocolatesList = list(chocolates)
chocolatesList.append("Reese's Peanut Butter Cups")
chocolates = tuple(chocolatesList)
print(chocolates) # ("Lindt", "Celebrations", "Heroes", "Guylian", "Ferrero Rocher", "Reese's Peanut Butter Cups")

# Another way of adding values to tuples is adding tuples to tuples:
moreChocolates = ("Twix", "Snickers", "KitKat")
chocolates += moreChocolates
del moreChocolates
print(chocolates) # ("Lindt", "Celebrations", "Heroes", "Guylian", "Ferrero Rocher", "Reese's Peanut Butter Cups", "Twix", "Snickers", "KitKat")

# To remove items in a tuple, you can also use the same workaround for changing values in a tuple:
chocolatesList = list(chocolates)
chocolatesList.remove("Reese's Peanut Butter Cups")
chocolates = tuple(chocolatesList)
print(chocolates) # ("Lindt", "Celebrations", "Heroes", "Guylian", "Ferrero Rocher", "Twix", "Snickers", "KitKat")

# You can also delete the tuple completely.
del chocolates
# print(chocolates) -> Error because the tuple does not exist.


# UNPACKING TUPLES

# When creating tuples, we normally assign values to it.
# This is known as packing a tuple.
# In Python, you can also extract the values in a tuple back into variables.
# This is known as unpacking a tuple.
(white, red, pink) = flowers
print(white) # "Lily"
print(red)   # "Rose"
print(pink)  # "Peony"

# If the number of variables is less than the number of values, you can add an asterisk to the variable name and the values that will be assigned to variable as a list:
countries = ("Albania", "Kenya", "Brazil", "India", "China")
(europe, africa, southAmerica, *asia) = countries
print(europe)           # "Albania"
print(africa)           # "Kenya"
print(southAmerica)     # "Brazil"
print(asia)             # ["India", "China"]

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left:
fruits = ("Apple", "Mango", "Papaya", "Pineapple", "Cherry")
(green, *tropic, red) = fruits
print(green)    # "Apple"
print(tropic)   # ["Mango", "Papaya", "Pineapple"]
print(red)      # "Cherry"


# LOOPING TUPLES

# You can loop through a tuple using a for loop:
for x in countries:
    print(x)    # "Albania"
                # "Kenya"
                # "Brazil"
                # "India"
                # "China"

# You can also loop through tuple items by referring to their index number:
for i in range(len(countries)):
    print(countries[i]) # "Albania"
                        # "Kenya"
                        # "Brazil"
                        # "India"
                        # "China"

# You can also loop through tuple items by using a while loop:
i = 0
while i < len(countries):
    print(countries[i])
    i+=1    # "Albania"
            # "Kenya"
            # "Brazil"
            # "India"
            # "China"


# JOINING TUPLES

# To join more tuple, use the + operator:
countries2 = ("Pakistan", "Lebanon", "Finland", "Mexico", "Chile")
countries += countries2
print(countries) # ("Albania", "Kenya", "Brazil", "India", "China", "Pakistan", "Lebanon", "Finland", "Mexico", "Chile")

# If you want to multiply the content of a tuple, a give number of times, you can use the * operator:
countries *= 2
print(countries) # ("Albania", "Kenya", "Brazil", "India", "China", "Pakistan", "Lebanon", "Finland", "Mexico", "Chile", "Albania", "Kenya", "Brazil", "India", "China", "Pakistan", "Lebanon", "Finland", "Mexico", "Chile")