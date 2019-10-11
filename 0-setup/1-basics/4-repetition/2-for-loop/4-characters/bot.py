# Character string

characters = str(input("What strange markings do you see?"))
num = 0

for position in range(0, len(characters), 1):
    print("index " + str(num) + ":" + str(characters[position]))
    num = num + 1




("Done !")