# Decision using ther if elif to specify alternative mutually exclusive paths
# input
forky = str(input('Where is Forky?\n'))

# if statement
if forky == 'With Bonnie':
    print ('Phew! Bonnie will be happy')

# elif statement
elif forky == 'Running Away':
    print ('Oh no! Bonnie will be upset!')

# else for message if variable not found
else:
    print ('Ah! I better look for him.')