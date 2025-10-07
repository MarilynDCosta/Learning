# W3Schools - Python
# Section 19: For Loops


# For loops are used for iterating over a sequence, i.e.: list, tuples, dictionaries and sets.
# This is less like the for keyword in other programming languages and works more like an iterator method as found in other OOP languages.

# With for loops, we can execute a set of statemenrs once for each item in a list, tuple, set. etc.

shoppingList = ["Milk", "Rice", "Sugar", "Yoghurt", "Peanuts", "Cheese"]
inTrolley = ["Cheese", "Rice", "Sugar"]

for x in shoppingList:
    if x in inTrolley: print("Already have in trolley.")
    else: print("You need to find", x + ".")

# For loops do not need an indexing variable to be set beforehand.

# You can also loop through strings.
name =  "Marilyn"
for x in name: print(x) # Should print Marilyn downwards.

# With the break statement, you can stop a loop before it has looped through all items.
for x in name:
    if x == "l": break
    print(x) # Should print Mari downwards.

# You can use the continue statement to stop a current iteration of a loop and continue with the next.
vowels = ["a", "e", "i", "o", "u"]
for x in name:
    if x.lower() in vowels: continue
    else: print(x) # Should print only consonants of Marilyn downwards.

# To loop through a set of code for a specified number of times, you can use the range() function.
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
    if x == 0: continue
    print(x) # Should count up from 1 to 5.

# The range() function defaults to 0 as a starting value by default but you can also specify the starting value by adding a parameter.
# You could recreate the last example done by simply using range(1,6) and getting rid of the continue statement when x==0.
for x in range(1,6): print(x) # Should count up from 1 to 5.

# The range() function defaults to increment a sequence by 1.
# However you can specify the increment value by adding a third parameter.

for x in range(2, 12, 2): print(x) # Prints even numbers from 2 to 10.

# You can use the else keyword in a for loop to specift a block of code to be executed when a loop is finished.
for x in range(1, 11): print(x)
else: print("We have counted to 10.")

# However, note that the else block would not be execute if the loop is stopped by a break statement.
for x in range(1, 11): 
    if x==6: break
    print(x) # This should only count to 5
else: print("We have counted to 10.") # This line would not be run.

# A nested loop is a loop inside a loop.
# The inner loop would be executed one time for each iteration of the outer loop.
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adjectives:
  for y in fruits:
    print(x, y)

# For loops cannot be empty, but if you do have a for loop with no content, you can use a pass statement to avoid getting an error.
for x in fruits:
   pass # Nothing is printed from this loop.