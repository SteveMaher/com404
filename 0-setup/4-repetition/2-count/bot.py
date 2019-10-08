# While loop with count
# Input number of live cables
cables = int(input("How many live cables must I avoid?"))

# Set cables variable to 0
livecables = 0

while cables > livecables:
    livecables = livecables + 1
    print("\n Avoiding...Done!", livecables, "live cables avoided.")


print ("All live cables have been avoided.")
