# Nested Loop

rows = int(input("How many rows shoud I have?"))
columns = int(input("How many columns should I have?"))
emoji = ":-) "

print("Here I go:")
print()

for count in range(0, rows, 1):
    for count in range(0, columns, 1):
        print(emoji, end="")
    print()

print("\n Done !")
