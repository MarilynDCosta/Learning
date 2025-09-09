# W3Schools - Python
# Section 9: Strings


# PYTHON STRINGS

# Strings can be written with either single or double quotation marks.
# It does not matter which type you use but it is good to stick to one for consistency and code quality.

# You can quote inside strings, as long as the quotation marks inside the string are not the same as the quotation marks used for the quote:
print('You can call me "Marilyn".')

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
name = "Marilyn"
print(name)

# You can create multiline strings to a variable by using three quotes (double or single):
song = """Never gonna give you up.
Never gonna let you down.
Never gonna run around and desert you.
Never gonna make you cry.
Never gonna say goodbye.
Never gonna tell a lie and hurt you.
"""
print(song)

# Like many popular programming languages, strings are arrays of unicode characters.
# However, Python does not have a character data type: a character is simply a string with a length of 1.
# You can use [] to access elements of a string.
print(song[1]) # e

# When looping through a string, you can use a for loop.
for x in "Marilyn":
    print(x)

# Use len() to get the length of a string:
print(len("Marilyn")) # 7

# To check if a phrase or character is present in a string, use the keyword in:
greeting = "Hello, I am Marilyn."
print("Marilyn" in greeting) # True

# You can also use this in an if statement:
if "Marilyn" in greeting:
    print("Hello, Marilyn")

# To check if a certain phrase or character is not in a string, you could use the keyword not in:
print("Wally" not in greeting) # True

if "Wally" not in greeting:
    print("Where's Wally?")


# SLICING STRINGS

# You can return the range of characters by using the slice syntax.
# Remember that strings and lists in Python are zero-indexed.
print(song[2:5]) # Gets the characters from position 2 to position 5 (not included) -> Returns ver

# To slice from the start, you can leave out the start index:
print(song[:5]) # Never

# To slice until the end, you can leave out the end index:
print(song[6:]) # Should print out the whole song but "Never"

# To slice from the end of a string, use negative indexing:
print(song[-10:-6]) # hurt


# STRING MODIFICATION

# Python has a set of built in methods you can use on strings.

# Firstly you can change the whole case of a string to upper or lower case by using the upper() and lower() methods respectively:
print(name.upper()) # MARILYN
print(name.lower()) # marilyn

# You can also remove whitespace in strings by using the strip() method.
# This would remove space before and after the text.
text = " I love Python. "
print(text.strip()) # Returns "I love Python."

# You can also replace strings in a string of text with another string by using the replace() function:
print(song.replace("Never gonna", "I will"))

# Use the split() method to return a list where the text between the specified seprator becomes the list items.
print(song.split("Never gonna")) # Gives you all the things Rick says he will never do... Also note the first index of this list is blank because "Never gonna" is at the start of the song.


# STRING CONCATERNATION

# To concaternate strings you can use the + operator.
a = "Hello"
b = "Marilyn"
c = a + b
print(c)

# Note that this does not add a space; to fix this add a " "
c = a + " " + b
print(c)

# Another way you could do this, without needing to add a space is to not use the + operator but to simply print out both variables and separate them with a comma.
print(a, b)


# FORMAT STRINGS

# From the variables, chapter, we know that we cannot use concaternate a string with a non-string data type.
# However, you can combine strings and non-strings using f-strings or the format() method.

# F-strings are specified by simply putting an f in front of a string literal and adding curly brackets as placeholders for variable and other operations.
age = 21
fString1 = f"My name is {name} and I am {age} years old."
print(fString1)

# Placeholders in f-Strings can container modifiers to format the value.
# A modifier is included by adding a colon and followed by a legal formatting type.
# One legal formatting type is .2f, which means a fix point number with 2 decimals:
price = 59
fString2 = f"The price is £{price:.2f}."
print(fString2)

# A placeholder can also contain Python code such as math operations.
ageDifference = 8
fString3 = f"My sister is {age + ageDifference} years old."
print(fString3)


# ESCAPE CHARACTERS

# To insert illegal characters in a string, you can use escape characters.
# An escape characters is a backslash followed by the character you want to insert.

# An example of an illegal character is double quote inside a string surrounded by double quotes.
text = "You can call me \"Al\"."
print(text)

# These are some escape characters used in Python:
#   1. \'       -> Single quote
#   2. \\       -> Backslash
#   3. \n       -> New Line
#   4. \r       -> Carriage Return
#   5. \t       -> Tab
#   6. \b       -> Backspace
#   7. \f       -> Form Feed
#   8. \ooo     -> Octal Value
#   9. \xhh     -> Hex Value