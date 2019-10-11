# Sum of a number of user input variables
# Input and set the var

howmany = int(input("How many numbers should I sum up?"))
counting = 1
total = 0

# While Loop

while counting <= howmany:
    num = int(input("\n Please enter number " + str(counting) + " of " + str(howmany) + ": "))
    counting = counting + 1
    total = total + num
print ("\n The answer is " + str(total))