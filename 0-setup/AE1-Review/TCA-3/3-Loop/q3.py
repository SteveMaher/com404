# While Loop with count
# User input

heroes = int(input("How many heroes must we gather?\n"))

# Set the variable to 1
count = 1

print("Gathering heroes...")

while heroes >= count:
    print("...found hero", count)
    count = count + 1

print("...all the heroes have been gathered")
