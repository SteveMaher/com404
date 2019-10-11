# While loop
# Input number of bars
bars = int(input("How many bars should be charged?"))
cel = "█"
# Set cables variable to 0
charged = 0

#while loop
while bars > charged:
    charged = charged + 1
    print("\n Charging:", cel * charged )

print ("The battery is fully charged.")
