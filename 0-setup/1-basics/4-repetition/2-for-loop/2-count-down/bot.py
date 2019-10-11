# Reverse the range in a loop
num = int(input("How far are we from the cave?"))

for count in range(num, 0, -1):
    print(str(num) + " Steps remaining")
    num = num -1
print("\n We have reached the cave !")
