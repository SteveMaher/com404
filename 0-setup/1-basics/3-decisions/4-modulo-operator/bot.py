# use the modulo operator to calculat a odd or even whole number
number = int(input('Please enter a whole number.'))

# calculate the modulo of the input number, if greater than 0 the even number
if (number % 2 > 0):
    print ('The number', number, 'is an odd number')

else:
    print ('The number', number, 'is an even number')
