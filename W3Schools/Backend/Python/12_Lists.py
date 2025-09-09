# W3Schools - Python
# Section 12: Lists


# PYTHON LISTS

# Lists are a data collection used to store multiple items in a single variable.
# Lists are created using square brackets.

sisters = ["Veronica", "Fiona", "Marilyn"]
print(sisters)

# List items are...
#   1. Ordered                ->    The order of the list would not change; if new items are added, they are added to the end of the list.
#   2. Changeable             ->    Items in a list can be changed, added and removed after a list has been created.
#   3. Allow Duplicate Values ->    As lists are indexed, lists can have items with the same value.

# To determine how many items a list has, use the len() function:
print(len(sisters))

# List items can be of any data type:
numbersToFive = [1, 2, 3, 4, 5]
booleans = [True, False, True, True, False]

# A list can also contain different data types:
list1 = [1, "Happy", 3.4, False]

# Lists are defined as objects with the data type 'list'.
print(type(sisters))

# You can use the list() constructor when creating a new list.
upToFive = list((1, 2, 3, 4, 5))

# There are 4 collection data types in Python:
#   1. Lists
#   2. Tuples
#   3. Sets
#   4. Dictionaries


# ACCESSING LIST ITEMS

# List items are indexed and can be accessed by referring to their index number:
print(sisters[1]) # Fiona

# Negative indexing means starting from the end of the list, where -n refers to the nth last item in the list:
print(sisters[-1]) # Marilyn

# You can specify a range of indexes by specifying where to start and end the range.
# When specifying a range, the return value will be a new list with the specified items.
shopping = ["Pasta", "Rice", "Cherries", "Chocolate", "Bread", "Tomatoes"]
print(shopping[2:5]) # ["Cherries", "Chocolate", "Bread"]

# If you leave out the start value, the range will start at the first item:
print(shopping[:4]) # ["Pasta", "Rice", "Cherries", "Chocolate"]

# If you leave out the end value, the range will go on to the end of the list:
print(shopping[3:]) # ["Chocolate", "Bread", "Tomatoes"]

# If you want to start the search from the end of the list, you can use negative indexes:
print(shopping[-4:-1]) # ["Cherries", "Chocolate", "Bread"]

# To determine if a specified item is present, you can use the in keyword:
if "Bread" in shopping:
    print("Bread is on the shopping list.")


# CHANGING LIST ITEMS

# To change the value of a specific item, refer to the index number:
shopping[1] = "Wine"
print(shopping) # ["Pasta", "Wine", "Cherries", "Chocolate", "Bread", "Tomatoes"]

# To change items in a specific range, you can define a list with the new values and refer to the range of index values where you want to insert the new values:
shopping[2:5] = ["Peaches", "Biscuits", "Cake"]
print(shopping) # ["Pasta", "Wine", "Peaches", "Biscuits", "Cake", "Tomatoes"]

# If you want to insert more itmes than you replace, the new items will be inserted where you specified and the remaining items will move accordingly:
shopping[:2] = ["Cucumber", "Yoghurt", "Jam"]
print(shopping) # ["Cucumber", "Yoghurt", "Jam", "Peaches", "Biscuits", "Cake", "Tomatoes"]

# If you insert less items than you replace, the new items will be inserted where you specified and the remaining items in the specified range that do not have a corresponding value will be removed:
shopping[3:] = ["Salt", "Pepper"]
print(shopping) # ["Cucumber", "Yoghurt", "Jam", "Salt", "Pepper"]