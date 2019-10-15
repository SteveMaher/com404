# Code to demonstrate the implementation of multiple user defined functions

def display_box(name):
  print("*" * (len(name) + 10))
  print("* Hello", name, "*")
  print("*" * (len(name) + 10))
  
def greet_user():
  print("Please enter your name")
  name = input()
  display_box(name)
  
greet_user()