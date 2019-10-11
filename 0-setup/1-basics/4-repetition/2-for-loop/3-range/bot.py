# Range
num = int(input("What level of brightness is required?"))
print("\n Adjusting brightness...")
bright = "**"


for count in range(0, num, 2):
    print("\nBeep's brightness level: " + bright)
    print("Bop's brightness level: " + bright)
    bright = bright + bright
