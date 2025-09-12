# W3Schools - Python
# Section 14: Sets


# PYTHON SETS

# Sets are used to store multiple items in a single variable.
# A set is a collection, which is unordered, unchangeable and unindexed.
# Sets are written with curly brackets:
flowers = {"Rose", "Lily", "Peony", "Lavender"}
print(flowers)

# Set items...
#   1. Are Unordered            -> Items in a set do not have a defined order and can not be referred to by index or key.
#   2. Are Unchangeable         -> Items cannot be changed after a set has been created.
#   3. Do Not Allow Duplicates  -> Sets cannot have two items with the same value.

# Note: Duplicate items in a set would be ignored.
chocolates = {"Ferrero Rocher", "Cadbury's", "Lindt", "Cadbury's"}
print(chocolates)

# Set items can be of any data type:
integers = {1, 2, 3}
floats = {0.1, 0.2, 0.3}
booleans = {True, False, True}

# You can have multiple data types within a set.
# Note: True and 1 are considered the same value in sets and are treated as duplicates; the same can also be said for False and 0.
mixedTypes1 = {1, True, "Marilyn", 2.3}
mixedTypes2 = {0, False, "Hello", 2.8}
print(mixedTypes1)
print(mixedTypes2)

# Use the len() function to find out how many items a set has:
print(len(flowers)) # 3

# Sets are defined as objects with the data type 'set'.

# You can also use the set constructor to make sets:
sisters = set(("Veronica", "Fiona", "Marilyn"))
print(sisters)


# ACCESSING SET ITEMS

# You cannot access items in a set by referring to an index or key.
# However, you can loop through set items using a for loop:
for x in sisters:
    print(x)

# You can also use the in keyword to ask if a specified value is in a set:
print("Marilyn" in sisters)     # True
print("Rachel" not in sisters)  # True


# ADDING SET ITEMS

# Once a set is created, you cannot change its items but you can add new items.
# To add one item to a set, use the add() method:
chocolates.add("Guylian")
print(chocolates)

# To add another set into the current set, use the update() method:
moreChocolates = {"Twix", "Snickers", "KitKat"}
chocolates.update(moreChocolates)
print(chocolates)

# You can also use the update() method to add any iterable object to a set, such as a tuple, list or dictionary:
chocolatesList = ["Celebrations", "Quality Street"]
chocolates.update(chocolatesList)
print(chocolates)


# REMOVING SET ITEMS

# To remove an item in a set, use the remove() or discard() methods:

# Note: If the item to remove does not exist, Python will raise an error:
chocolates.remove("Guylian")
print(chocolates)

# Note: If the item to discard does not exist, Python will not raise an error:
chocolates.discard("Twix")
print(chocolates)

# You can also use the pop() fucntion to remove an item but this method will remove a random item so you are not sure what item will be removed.
# This is due to sets being unordered:
x = chocolates.pop()
print(x)
print(chocolates)

# The clear() method empties a set:
mixedTypes1.clear()
print(mixedTypes1) # set()

# The del keyword deletes a set completely:
del mixedTypes2


# LOOPING SETS

# You can loop through sets using a for loop:
for x in chocolates:
    print(x)


# JOINING SETS

# There are several ways to join two or more sets in Python:

# The union() method returns a new set with all items from both sets:
names = {"Rose", "Lily", "Marilyn", "Sadie", "Lavender"}
jointSet = flowers.union(names)
print(jointSet)

del jointSet

# You can also use the | operator for the same result:
jointSet = flowers | names
print(jointSet)

del jointSet

# You can also use the union() method or the | operator to join multiple sets:
herbs = {"Lavender", "Thyme", "Oregano"}

jointSet = flowers.union(names, herbs)
print(jointSet)

del jointSet

jointSet = flowers | names | herbs
print(jointSet)

del jointSet

# You can also use the union() to join a set or tuple:
herbsTuple = ("Rosemary", "Thyme", "Oregano")

plants = flowers.union(herbs)
print(plants)

# The update() method inserts all items from one set into another.
# The update() method changes the original set and does not return a new set:

alphabet1 = {"a", "b", "c"}
alphabet2 = {"d", "e", "f"}
alphabet1.update(alphabet2)
print(alphabet1)

# The intersection() method keeps only duplicates.
# This method returns a new set, containing items present in both sets.
flowerNames = names.intersection(flowers)
print(flowerNames)

del flowerNames

# You can also use the & operator for the same result:
flowerNames = names & flowers
print(flowerNames)

# The intersection_update() method keeps only duplicayes but will change the original set instead of returning a new set:
fruits = {"Apple", "Banana", "Cherry"}
techCompanies = {"Google", "Microsoft", "Apple"}
fruits.intersection_update(techCompanies)
print(fruits) # {"Apple"}

# The values True and 1 are considered the same value and the same applies for False and 0:
mixedTypes1 = {1, False, "Marilyn", 2.3}
mixedTypes2 = {0, True, "Hello", 2.8}
intersection = mixedTypes1.intersection(mixedTypes2)
print(intersection)

# The difference() methof returns a new set, containing only items from the first set that are not present in the other set:
nonFlowerNames = names.difference(flowers)
print(nonFlowerNames)

# You can also use the - operator for the same result:
nonHerbNames = names.difference(herbs)
print(nonHerbNames)

# The difference_update() method keeps items from the first set that are not in the other set, but will change the original set instead of returning a new set:
fruits = {"Apple", "Banana", "Cherry"}
techCompanies = {"Google", "Microsoft", "Apple"}
fruits.difference_update(techCompanies)
print(fruits)

# The symmetric_difference() method will keep only elements that are not present in both sets:
flowerXorName = flowers.symmetric_difference(names)
print(flowerXorName)

# You can also use the ^ operator for the same result:
herbXorName = herbs.symmetric_difference(names)
print(herbXorName)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set:
fruitsXorTech = {"Apple", "Banana", "Cherry"}
techCompanies = {"Google", "Microsoft", "Apple"}
fruitsXorTech.symmetric_difference_update(techCompanies)
print(fruitsXorTech)