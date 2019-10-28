# Q2. Decision
#Display message to user
print("Learn the steps of the 5 sequence tango.\n")
# Read in the user response as an integer
steps = int(input("What step do you wish to learn?\n"))

# if statement
if steps ==1:
    print("Leader takes a step back.")
# elif statements
elif steps == 2:
    print("Side step towards centre of floor.")
elif steps == 3:
    print("Leader steps outside of follower.")
elif steps == 4:
    print("Preparation of the cross with the forward step.")
elif steps == 5:
    print("Leader closes his feet, follower completes cross step.")
# else for message if variable not found
else:
    print("Terminate the sequence.")
