# W3Schools - Python
# Section 18: While Loops


# Python has two primitive loop commands: while loops and for loops.

# The while loop can execute a set of statements as long as a condition is true.

def countdown(startNumber):
    while startNumber > 0:
        print(startNumber)
        startNumber -= 1

countdown(10) # Should count down from 10 to 1.

# While loops require relevant variables to be ready.
# For the example above, startNumber needed to be defined and it was set to 10 as a parameter within a function.

# With a break statement, you can stop a while loop even if the condition is still true

def countdownToFive(startNumber):
    while startNumber >= 0:
        print(startNumber)
        if startNumber <= 5:
            break
        startNumber -= 1

countdownToFive(10) # Should count down from 10 to 5.

# You can use a continue statement to stop a current iteration of a while loop and continue with the next iteration.

def evenCountdown(startNumber):
    while startNumber >= 0:
        if startNumber % 2 == 0:
            print(startNumber)
        else:
            startNumber -= 1
            continue
        startNumber -= 1

evenCountdown(10) # Should count down from 10 to 0 in decrements of 2.

# You can use an else statement to run a block of code when a condition is no longer true.

def bomb(startNumber):
    while startNumber >= 1:
        print(startNumber)
        startNumber -= 1
    else:
        print("Bang!")
# However, note that the else block would not be execute if the loop is stopped by a break statement.

bomb(10) # Should count down to 1 and then print "Bang!"