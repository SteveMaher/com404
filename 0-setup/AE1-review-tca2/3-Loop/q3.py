# While loop with count
# User input number
zone = int(input("How many zones must I cross?\n"))

# set the variable to 1
count = 1

print("Crossing zones...\n")

while zone > 0:
    print("...crossed zone", zone)
    zone = zone - count

print('Crossed all zones. Jumani')
