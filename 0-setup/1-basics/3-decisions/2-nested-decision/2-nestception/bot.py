# Multiple nested decisions
# Ask user what room to look in
room = str(input("Where should I look?"))

# If the user inputs bedroom ask where in the bedroom to look
if (room == "in the bedroom"):
    bedroom_location = str(input('Where in the bedroom should I look?'))
# if the answer is under the bed
    if (bedroom_location =="under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")

# If the user inputs bathroom ask where in the bathroom to look
if (room == "in the bathroom"):
    bathroom_location = str(input('Where in the bathroom should I look?'))
#if the answer is in the bathtub
    if (bathroom_location =="in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")

# If the user inputs lab ask where in the lab to look
if (room == "in the lab"):
    lab_location = str(input('Where in the lab should I look?'))
#if the answer is on the table
    if (lab_location =="on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

# Print message when any other room input
else:
    print("I do not know where that is but I will keep looking.")