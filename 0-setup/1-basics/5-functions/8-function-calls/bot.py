# Code to demonstrate the use of multiple function calls

# Function to print display box
def display_box(word):
  print("*" * (len(word) + 4))
  print("*", word, "*")
  print("*" * (len(word) + 4))
  

# Function to print lower case
def lower_case(word):
    print(word.lower())

# Function to print upper case
def upper_case(word):
    print()


# Function to display mirrored 
def disply_mirrored(word):
    print()


# Function to repeat word
def display_repeat(word):
    print()


# Input Options and Loop
def run():
    word = input("Please enter a word\n")
    print("Please select an option number from the list below\n")
    print("1) Display in a Box – display the word in an ascii art box")
    print("2) Display Lower-case – display the word in lower-case e.g. hello")
    print("3) Display Upper-case – display the word in upper-case e.g. HELLO")
    print("4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH")
    print("5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")
    option = int(input())
    print()

    if option == 1:
        print(display_box(word))
    elif option == 2:
        print(lower_case(word))
    elif option == 3:
        print(upper_case(word))
    elif option == 4:
        print(display_mirrored(word))
    elif option == 5:
        print(display_repeat(word))
    else:
        print("Invalid option, please try again")


# Run the programme
run()





