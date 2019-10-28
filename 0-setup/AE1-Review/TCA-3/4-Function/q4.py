# Function

def spideySense(enemy, direction):
    if enemy == "Green Goblin" and direction == "front":
        print("Goblin bombs incoming from", direction)
    elif enemy == "Venom" and direction == "behind":
        print("Venomous webbing incoming from", direction)
    elif enemy == "Electro" and direction == "left side":
        print("Electro striking from", direction)
    elif enemy == "Unknown" and direction == "right side":
        print("New enemy attacking from", direction)
    else:
        print()
    
# The following are calls to the function for testing purposes

spideySense("Green Goblin", "front")
spideySense ("Venom", "behind")
spideySense ("Electro", "left side")
spideySense ("Unknown", "right side")
