# if elif else to specify alternative mutually exclusive paths
# you use as many elif as you like
# input
direction = str(input('Towards which direction should I paint (up, down, left or right??'))

# 1st if statement
if direction == 'up':
    print ('I am painting in the upward direction!')

# multiple elif statements
elif direction == 'down':
    print ('I am painting in the downward direction!')

elif direction == 'left':
    print ('I am painting in the left direction!')

elif direction == 'right':
    print ('I am painting in the right direction!')

# final else for message if variable not found
else:
    print ('I dont know what direction that is')
