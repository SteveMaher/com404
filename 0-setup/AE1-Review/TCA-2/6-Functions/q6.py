# Multiple functions and function calls

def is_league_united(hero1, hero2):
    if hero1 == 'Superman' and hero2 == 'Wonder Woman':
        return True
    else:
        return False

def  decide_plan(hero1, hero2):
    united = is_league_united(hero1, hero2)
    if united == True:
        return 'Time to save the world!'
    else:
        return 'We must unite the league!'

def run():
    hero1 = input('Please enter the name of your 1st Superhero\n')
    hero2 = input('Please enter the name of you 2nd Superhero\n')
    question = input('Please choose league or plan\n')
    if question == 'league':
        is_league_united()
    elif question == 'plan':
        answer = decide_plan()
    else:
        print('Invalid command. Pleas try again')

# Run the program
run()





