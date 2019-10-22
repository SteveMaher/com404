# Function
#Define visit function
def visit(ghost):
    if ghost == 'Ghost of Christmas Past':
        print('Humbug! I care not for these days of past celebration.')
    elif ghost == 'Ghost Christmas Present':
        print('Humbug! I care not for their suffering.')
    elif ghost == 'Ghost Christmas Future':
        print('Please no more. I will change my ways')
    else:
        print()
# calls to the function for testing
visit('Ghost of Christmas Past')
visit('Ghost of Christmas Present')
visit('Ghost of Christmas Future')
