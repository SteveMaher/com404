# Sum of a number of user input variables
# Input and set the var

howmany = int(input("How many numbers should I sum up?"))
counting = 1
total = 0

# While Loop

while counting <= howmany:
    num = int(input("Please enter number " + str(counting) + "of " + str(howmany) + ":"))
    counting = counting + 1
    total = total + num
print ("The answer is" + str(total))