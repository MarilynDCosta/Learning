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

# To insert new list items without replaving any existing values, use the insert() method:
shopping.insert(3, "Oranges")
print(shopping) # ["Cucumber", "Yoghurt", "Jam", "Oranges", "Salt", "Pepper"]


# ADDING LIST ITEMS

# To add only one item to the end of a list, use the append() method:
shopping.append("Apples")
print(shopping) # ["Cucumber", "Yoghurt", "Jam", "Oranges", "Salt", "Pepper", "Apples"]

# To insert a list item at a specified index, use the insert() method:
shopping.insert(4, "Flour")
print(shopping) # ["Cucumber", "Yoghurt", "Jam", "Oranges", "Flour", "Salt", "Pepper", "Apples"]

# To append elements from another list to a current list, use extend() method.
tea = ["Milk", "Tea Bags", "Sugar"]
shopping.extend(tea)
print(shopping) # ["Cucumber", "Yoghurt", "Jam", "Oranges", "Flour", "Salt", "Pepper", "Apples", "Milk", "Tea Bags", "Sugar"]

# Note: the extend() method does not have to append lists and can append any iterable object, such as tuples, sets and dictionaries:
breakfast = ("Sausages", "Eggs", "Bacon", "Hash Browns", "Mushrooms", "Tomatoes") # Note the brackets; breakfast is a tuple here
shopping.extend(breakfast)
print(shopping) # ["Cucumber", "Yoghurt", "Jam", "Oranges", "Flour", "Salt", "Pepper", "Apples", "Milk", "Tea Bags", "Sugar", "Sausages", "Eggs", "Bacon", "Hash Browns", "Mushrooms", "Tomatoes"]


# REMOVING LIST ITEMS

#  The remove() method removes the specified item
shopping.remove("Cucumber")
print(shopping) # ["Yoghurt", "Jam", "Oranges", "Flour", "Salt", "Pepper", "Apples", "Milk", "Tea Bags", "Sugar", "Sausages", "Eggs", "Bacon", "Hash Browns", "Mushrooms", "Tomatoes"]

# Note: if there are more than item with a specified value, the remove() method would only remove the first occurence:
shopping.append("Eggs")
shopping.remove("Eggs")
print(shopping) # ["Yoghurt", "Jam", "Oranges", "Flour", "Salt", "Pepper", "Apples", "Milk", "Tea Bags", "Sugar", "Sausages", "Bacon", "Hash Browns", "Mushrooms", "Tomatoes", "Eggs"]

# To remove a list item at a specified index, use the pop() method:
shopping.pop(2)
print(shopping) # ["Yoghurt", "Jam", "Flour", "Salt", "Pepper", "Apples", "Milk", "Tea Bags", "Sugar", "Sausages", "Bacon", "Hash Browns", "Mushrooms", "Tomatoes", "Eggs"]

# Note: if you do not specify the index, the pop() method will remove the last item in the list:
shopping.pop() 
print(shopping) # ["Yoghurt", "Jam", "Flour", "Salt", "Pepper", "Apples", "Milk", "Tea Bags", "Sugar", "Sausages", "Bacon", "Hash Browns", "Mushrooms", "Tomatoes"]

# You can also use the del keyword to remove an item at a specified index:
del shopping[2]
print(shopping) # ["Yoghurt", "Jam", "Salt", "Pepper", "Apples", "Milk", "Tea Bags", "Sugar", "Sausages", "Bacon", "Hash Browns", "Mushrooms", "Tomatoes"]

# The del keyword can also delete the list completely
del tea
# print(tea) -> tea as a list is not defined as it was deleted

# You can also empty a list by using the clear() method.
# Compared to using the del keyword, the list will still remain but will be empty:
shopping.clear()
if shopping == []:
    print("Shopping complete!") # Should print as the list is empty


# LOOP LISTS

# You can loop through a list by using a for loop:
for x in sisters:
    print(x) # Veronica
             # Fiona
             # Marilyn

# You can also loop through the list items by referring to their index number.
# By using the range() and len() functions, you can create a suitable iterable; in the example below the iterable is [0, 1, 2]:
for i in range(len(sisters)):
    print(sisters[i]) # Veronica
                      # Fiona
                      # Marilyn

# You can use a while loop to loop through list items.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration:

i = 0
while i < len(sisters):
    print(sisters[i])
    i += 1 # Veronica
           # Fiona
           # Marilyn

# You can also use list comprehension, which offers the shortest syntax for looping through lists.
[print(x) for x in sisters] # Veronica
                            # Fiona
                            # Marilyn


# LIST COMPREHENSION

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# For example, say you have a list of flowers and you want a new list of flowers containing the letter "e".
# Say that this is your list:
flowers = ["Lily", "Rose", "Peony", "Iris", "Dahlia", "Carnation", "Poppy", "Marigold", "Bluebell"]

# If you were to create this new list, you could go about it using a for loop
flowersWithE = []
for x in flowers:
    if "e" in x:
        flowersWithE.append(x)
print(flowersWithE) # ["Rose", "Peony", "Bluebell"]

# With list comprehension you can do this in one line of code
del flowersWithE
flowersWithE = [x for x in flowers if "e" in x]
print(flowersWithE) # ["Rose", "Peony", "Bluebell"]

# The syntax for list comprehension is newList = [expression for item in iterable if condition == True].

# The condition is like a filter that only accepts items that evaluate to True.
# In this case, our condition was "e" in x, which returned True for all elements apart from flowers in the list that did not contain "e".
# In list comprehension, the condition is optional and can be ommitted.
# If there is no condition, your new list would contain the same items as the list you had.

# The iterable can be any iterable object, such as a list, tuple, set, etc.
# With our example, the iterable was flowers.

# The expression is the current item in the iteration but is also the outcome, which you can manipulate before it ends up like a list item in the new list.
# In our example, our expression was simply x.
# However, in our example, the condition is case sensitive so no flowers with an uppercase E and no lowercase e would have been detected.
del flowersWithE
flowers.append("Erica")
flowersWithE = [x for x in flowers if "e" in x]
print(flowersWithE) # Erica would not be detected

# One way you could fix this issue is by replacing flowers with a list with the same items in lowercase...
del flowersWithE
flowers = [x.lower() for x in flowers]
print(flowers)
flowersWithE = [x.capitalize() for x in flowers if "e" in x]
print(flowersWithE)
# In this case when you have two expressions here x.lower() when creating a new flowers list and x.capitalize() when creating the list for flowers containing e.

# You could also manipulate the case of the items in flowers in a simpler way by manipulating the condition:
flowers = [x.capitalize() for x in flowers] # We are restoring the flowers list to its original capitalised state as it was in the beginning.
del flowersWithE
flowersWithE = [x for x in flowers if "e" in x.lower()]
print(flowersWithE)
# This is only three lines of code (excluding restoring the flowers list to its original state).
# The expression can be set to any outcome you want and can also contain conditions.
# Conditions in this case are not like a filter but are a way of manipulating the outcome.

# For example, let's say that for any flower that does not contain a letter e, we replace it with the word "blossom".
# Our code would look like this...
flowersWithEOrBlossom = [x if "e" in x.lower() else "Blossom" for x in flowers]
print(flowersWithEOrBlossom) # ["Blossom", "Rose", "Peony", "Blossom", "Blossom", "Blossom", "Blossom", "Blossom", "Bluebell", "Erica"]
# This expression says that the list item should be returned if it contains e and if it isn't return "Blossom".


# SORTING LISTS

# List objects have a sort() method that sorts a list alphanumerically, ascending by default:
flowers.sort()
print(flowers) # ["Bluebell", "Carnation", "Dahlia", "Erica", "Iris", "Lily", "Marigold", "Peony", "Poppy", "Rose"]

numbers = [25, 45, 12, 19, 71, 103, 54, 3]
numbers.sort()
print(numbers) # [3, 12, 19, 25, 45, 54, 71, 103]

# If you want to sort the numbers in descending order, use the keyword argument reverse = True:
flowers.sort(reverse = True)
print(flowers) # ["Rose", "Poppy", "Peony", "Marigold", "Lily", "Iris", "Erica", "Dahlia", "Carnation", "Bluebell"]

numbers.sort(reverse = True)
print(numbers) # [103, 71, 54, 45, 25, 19, 12, 3]

# You can also customise your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (lowest number first):
def myfunc(n):
    return abs(n-50)
numbers.sort(key = myfunc)
print(numbers) # [54, 45, 71, 25, 19, 12, 3, 103]

# By default, the sort() method is case-sensitive, which results in all capital letters being sorted before lower case letters:
differentCases = ["apple", "Croissant", "Bible", "love", "Victory", "mouse"]
differentCases.sort()
print(differentCases) # ["Bible", "Croissant", "Victory", "apple", "love", "mouse"]

# However, this issue can be fixed by using str.lower, str.upper or str.capitalise as a key function to treat all list entities as if they all have the same case:
differentCases.sort(key = str.capitalize)
print(differentCases)

# If you want the reverse order of a list, regardless of the alphabet you can use the reverse method to reverse the current sorting order of the elements:
flowers.reverse() # This should results in flowers being in alphabetical order.
print(flowers) # ["Bluebell", "Carnation", "Dahlia", "Erica", "Iris", "Lily", "Marigold", "Peony", "Poppy", "Rose"]


# COPYING LISTS

# You cannot copy a list by just typing list2 = list1 because list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
flowers2 = flowers
flowers.append("Daisy")
flowers.sort()
print(flowers2) # flowers2 also contains "Daisy"

# Instead, you can use the method copy().
del flowers2
flowersCopy = flowers.copy()
print(flowersCopy) # ["Bluebell", "Carnation", "Dahlia", "Daisy, "Erica", "Iris", "Lily", "Marigold", "Peony", "Poppy", "Rose"]

# You can also use list() to make a copy.
del flowersCopy
flowersCopy = list(flowers)
print(flowersCopy) # ["Bluebell", "Carnation", "Dahlia", "Daisy, "Erica", "Iris", "Lily", "Marigold", "Peony", "Poppy", "Rose"]

# Another method to copy the list is by using the slice operator:
del flowersCopy
flowersCopy = flowers[:]
print(flowersCopy) # ["Bluebell", "Carnation", "Dahlia", "Daisy, "Erica", "Iris", "Lily", "Marigold", "Peony", "Poppy", "Rose"]


# JOINING LISTS

# There are several ways to join or concaternate lists in Python.

# One way is using the + operator:
alphabet = ["a", "b", "c"]
count = [1, 2, 3]
alphabetCount = alphabet + count
print(alphabetCount) # ["a", "b", "c", 1, 2, 3]

# Another way is to append all items from one list to another:
del alphabetCount
for x in count:
    alphabet.append(x)
print(alphabet) # ["a", "b", "c", 1, 2, 3]

alphabet = ["a", "b", "c"]

# You can also use the extend() method, where you can add one list to another.
alphabet.extend(count)
print(alphabet) # ["a", "b", "c", 1, 2, 3]