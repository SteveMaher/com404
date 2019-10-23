miles = int(input("How many miles must I travel before I reach the secret base?\n"))
print("I will count the miles...\n")

for count in range (miles, 0, -1):
    print("I have", miles, "miles to go before I reach the base.")
    miles = miles - 1

print()
print("I have arrived at the secret headquarters of the MIB!")
print("It is time to sneak in.")
