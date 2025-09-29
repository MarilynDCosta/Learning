# W3Schools - Python
# Section 15: Dictionaries


# PYTHON DICTIONARIES

# Dictionaries store data values in key:value pairs.
# They are collections that are ordered, changeable and do not allow duplicates.

fruit = {"Type": "Apple", "Colour": "Red", "Expiry in Days": 5, "Expired?": False, "Price": 0.45}
print(fruit)

# Dictionary items can be referred to by using the key name.
print(fruit["Type"])

# Dictionaries have a defined order and that order will not change.
# Therefore, you can refer to dictionary items by index.

# Dictionaries are changeable so items can be changed, added or removed after a dictionary has been created.

# Dictionaries cannot have two items with the same key.
# Duplicate values in this case would overwrite existing values.
fruit = {"Type": "Apple", "Colour": "Red", "Expiry in Days":5, "Expiry in Days":10, "Expired?": False, "Price": 0.45}
print(fruit)

# To determine the length of a dictionary, use the len() funcion.
print(len(fruit)) # 5

# Values in a dictionary can be any data type (as seen above).
# Dictionaries are defined as objets with the data type 'dict'.
print(type(fruit))

# You can also use the dict() constructor to make a dictionary.
person = dict(name = "Marilyn", age = 22, university = "Bath")
print(person)


# ACCESSING DICTIONARY ITEMS

# You can access items of a dictionary by referring to its key name inside square brackets.
my_name = person["name"]
print("Hello, I am", my_name + ".")

# You can also use the get() method which would give you the same result.
my_age  = person.get("age")
print("I am", my_age, "years old.")

# To return all the keys in a dictionary, you can use the keys() method.
print(person.keys())

# The list of keys is a view of the dictionary, which means that any changes done to the dictionary woll be reflected in the keys list.
person["number of siblings"] = 2
print(person.keys())

# The values() method returns a list of all values in the dictionary.
print(person.values())

# The list of values is a view of the dictionary, which means that any changes done to the dictionary will be reflected in the values list.
person["university"] = "University of Bath" # Changes university from Bath to University of Bath
print(person.values())

person["gender"] = "Female" # Adds a new item to the dictionary
print(person.values())

# To return each item in a dictionary, use the items() method.
# This will return each item as tuples in a list.
print(person.items())

# The list returned from using the items() method is a view of the items of the dictionary, which means that any changes done to the dictionary will be reflected in the items list.
person["university subject"] = "Computing"
print(person.items())

# To check if a key is present in a dictionary, use the in keyword.
if "university subject" in person:
    print("\"university subject\" is in the person dictionary.")


# CHANGING DICTIONARY ITEMS

# You can change dictionary items by referring to a key name.
person["university subject"] = "Computer Science"
print(person["university subject"])

# You can also use the update() method to update the dictionary with items from the given argument.
# The argument must be a dictionary or an iterable object with key:value pairs.
person.update({"year of study": 4})
print(person)


# ADDING DICTIONARY ITEMS

# You can add items to a dictionary by using a new index and assigning a value to it.
person["country of birth"] = "England"
print(person)

# You can also use the update() method update the dictionary with items from a dictionary or an iterable object with key:value pairs.
person.update({"nationality": "British"})
print(person)


# REMOVING DICTIONARY ITEMS

# There are several ways to remove items from a dictionary.

# The first way is using the pop() method.
# The pop() method removes the item with the specified key name.
person.pop("number of siblings")
print(person)

# You can also use the popitem() method to remove the last inserted item.
person.popitem() # Removes "nationality"
print(person)

# You can also use the del keyword to remove an item with a specified key name.
del fruit["Expired?"]
print(fruit)

# The del keyword can also delete a dictionary completely.
del fruit

# You can also use the clear() method to empty the dictionary but not delete it completely.
person.clear()
print(person) # returns an empty dictionary: {}


# LOOPING THROUGH DICTIONARIES

# You can loop through a dictionary with a for loop.
# When looping through a dictionary, the return value are keys of the dictioanry but there are methods to returning the values as well.
student = {'Name': 'Marilyn', 'Age': 22, 'University': 'University of Bath', 'Gender': 'Female', 'University Subject': 'Computer Science', 'Year of Study': 4, 'Country of Birth': 'England'}

# To print all keys in a dictionary:
for x in student:
    print(x)

# You can also use the keys() method to return keys of a dictionary.
for x in student.keys():
    print(x)

# To print all values in a dictionary:
for x in student:
    print(student[x])

# You can also use the values() method to return values of a dictionary.
for x in student.values():
    print(x)

# You can loop through both keys and values by using the items() method.
for x, y in student.items(): # x corresponds with keys and y corresponds with values -> otherwise, each item will be returned as a tuples containing the item's key and value.
    print(x, y)


# COPYING DICTIONARIES

# You cannot copy a dictionary by typing dict2  = dict1 because dict2 is only a reference to dict1 and changes in dict1 will be automaticall made to dict2.
student2 = student
student["Graduation Year"] = 2026
print(student2) # student2 should also have a graduation year
del student2

# One way to make a copy is the copy() method.
me = student.copy()
print(me)
del me

# Another way of copying a dictionary is by using the built-in function dict()
me = dict(student)
print(me)


# NESTED DICTIONARIES

# Nested dictionaries are dictionaries that can contain dictionaries.
siblings = {"eldest": {"name": "Veronica", "year": 1995}, "middle": {"name": "Fiona", "year": 1998}, "youngest": {"name": "Marilyn", "year": 2003}}
print(siblings)
del siblings

# You can also add dictionaries into a new dictionary
eldest = {"name": "Veronica", "year": 1995}
middle = {"name": "Fiona", "year": 1998}
youngest = {"name": "Marilyn", "year": 2003}
siblings = {"eldest": eldest, "middle": middle, "youngest": youngest}
print(siblings)

# To access items in nested dictionaries, you can use the name of the dictionaries starting with the outer dictionary.
print(siblings["middle"]["year"]) # 1998

# You can loop through a dictionary by using the items() method.
for x, obj in siblings.items(): # x is the outer dictionary.
    print(x)
    for y in obj: # y are the keys within the inner dictionaries.
        print(y + ':', obj[y]) # obj[y] are the values in the inner dictionary corresponding to the key y.