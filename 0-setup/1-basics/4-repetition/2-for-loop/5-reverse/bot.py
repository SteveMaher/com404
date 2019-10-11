# Reverse

phrase = str(input("What phrase do you see"))

print("\n Reversing...")
print("\n")

for char in range(len(phrase) - 1, -1, -1):
    print(phrase[char], end="")
