# Nesting 
# define health value
health = 100
count = 5

print ("Your health is 100%. Escape is in progress...")
print()

for count in range(count, 0, -1):
    response = input('...Oh dear, who is that?\n')

    if response == "Smilers Bot":
        print('Time to jam out of here!')
        health = health - 20  
        
    elif response == 'Hacker':
        print('Yay! Better follow this one!')
        health = health + 20   
    else:
        print('Phew, just another emoji!')

print('Escaped! Health is ' + str(health) + '%')