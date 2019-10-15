# Code to demonstrate the use of a user-defined function with a loop

def cross_bridge(in_steps):
    if in_steps > 5:
        print("The brigde is collapsing!")
        for count in range (in_steps, 0, -1):
            print("Crossed Step")

    if in_steps <= 5:
        for count in range (in_steps, 0, -1):
            print("Crossed Step")
    else:
        print("We must keep going!")



cross_bridge(3)
cross_bridge(6)






