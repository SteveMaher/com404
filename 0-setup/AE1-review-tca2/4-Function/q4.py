# Function
#Define visit function
def visit(ghost):
    if ghost == 'Christmas Past':
        print('Humbug! I care not for these days of past celebration.')
    elif ghost == 'Christmas Present':
        print('Humbug! I care not for their suffering.')
    elif ghost == 'Christmas Future':
        print('Please no more. I will change my ways')
    else:
        print('\n')


# calls to the function for testing

visit('Ghost of Christmas Past')
visit('Ghost of Christmas Present')
visit('Ghost of Christmas Future')