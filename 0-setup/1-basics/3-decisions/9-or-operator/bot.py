# Logical OR Operator
# Retrieve story type from the user
adventure = str(input("Please enter the type of adventure should I have? (scary, short, safe, or long)"))

# Type of Adventure is scary or short
if ((adventure == "scary") or (adventure == "short")):
    print ("Entering the dark forest!")


# Type of Adventure is safe or long
elif ((adventure == "safe") or (adventure == "long")):
    print ("Taking the safe route!")

# All other responses
else:
    print ("Not sure which route to take.")