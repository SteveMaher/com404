# Code to demonstrate the use of a user-defined function with a parameter

def escape_by(plan):

    if plan == "jumping over":
        print("\nWe cannot escape that way! The boulder is moving too fast!")
    elif plan == "running around":
        print("\nWe cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("\nThat might just work! Lets go deeper!")
    else:
        print("\nWe cannot escape that way! The boulder is in the way!")

escape_by ("jumping over")
escape_by ("running around")
escape_by ("going deeper")


