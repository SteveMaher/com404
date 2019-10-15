# Code to demonstrate the use of a user-defined function with multiple parameters

def climb_ladder(remaining, crossed):
    if remaining < crossed:
        print("Still some way to go!")
    else:
        print("We made it!")

climb_ladder(2, 5)
climb_ladder(5, 5)







