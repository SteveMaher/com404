# if elif else to specify alternative mutually exclusive paths
# use as many elif as you like
direction = str(input('Towards which direction should I paint (up, down, left or right??'))
if direction == 'up':
    print ('I am painting in the upward direction!')

elif direction == 'down':
    print ('I am painting in the downward direction!')

elif direction == 'left':
    print ('I am painting in the left direction!')

elif direction == 'right':
    print ('I am painting in the right direction!')

else:
    print ('I dont know what direction that is')
