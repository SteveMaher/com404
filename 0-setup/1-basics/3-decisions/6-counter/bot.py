# counter
# input the variables
first = int(input('Please enter the first whole number '))
second = int(input('Please enter the second whole number '))
third = int(input('Please enter the third whole number '))
# add fields to count and store the odd and even numbers
odd = 0
even = 0

# calculate
if (first % 2 > 0):
    odd = odd + 1
else:
    even = even + 1

if (second % 2 > 0):
    odd = odd + 1
else:
    even = even + 1

if (third % 2 > 0):
    odd = odd + 1
else:
    even = even + 1

print('There were', even, 'even and', odd, 'odd numbers.')








