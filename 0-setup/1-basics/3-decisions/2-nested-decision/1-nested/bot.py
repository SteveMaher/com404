# ask for the type of book cover
covertype = str(input('What is the cover type of the book (hard / soft?'))

# Is the input a hard or soft cover
if (covertype == "soft"):

    # the input was soft so ask if the cover is perfect bound
    binding = str(input('Is the book perfect bound?'))

    if (binding =="yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stiches are great for short books")

# Print message for hard cover
else:
    print("Books with hard covers can be more expensive!")
    


