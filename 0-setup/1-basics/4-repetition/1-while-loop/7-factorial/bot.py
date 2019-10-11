# While loop to calculate the factorial of a number

num = int(input("Please enter a number: "))
factorial = 1

while num > 0:
    factorial = factorial * num
    num = num -1

print ("\n The factorial is : " + str(factorial))
