# Membership Operators

phrase = str(input("What phrase do you see?"))
print()
print("Reversing...")

for char in range(len(phrase) - 1, -1, -1):
    print("\n The phrase is: " + phrase[char], end="")
