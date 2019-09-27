# Health meter
# Define characters
lives_chr = "♥"
energy_chr = "♦"
shield_chr = "♦"
# Input values
print("Please enter the number of lives.")
lives = int(input())
print("Please enter the energy level.")
energy = int(input())
print("Please enter the shield level.")
shield = int(input())
# Output results
print()
print("Health has been set.")
print()
print("Lives:  ", lives_chr * lives)
print("Energy: ", energy_chr * energy)
print("Shield: ", shield_chr * shield)