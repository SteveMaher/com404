# Input and output program
# Define character
happy = "☺"
# Input values
print("Hello, what is your name?")
name = (input())
print("Hello", name, "Want to knoe how much wine is in that box?, Please enter the dimensions below:")
print()
print("What is the height of the box? (cm)")
height = float(input())
print("What is the width of the box? (cm)")
width = float(input())
print("What is the depth of the box? (cm)")
depth = float(input())
# Calculation
capacity = (height * width * depth) /1000
# Output the answer
print(name, "You have", capacity, "litres of wine to drink" )
print(happy)