# Decision using the if else statementto specify alternative mutually exclusive paths
# input
response = str(input('Have you fear in your heart?\n'))

# if statement
if response == 'yes':
    print ('Fear is the path to the dark side. You cannot be a Jedi apprentice.')

# else for message if input not yes
else:
    print ('The force is strong in you. You may be a Jedi apprentice.')
