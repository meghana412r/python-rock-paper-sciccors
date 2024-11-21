import random
a = input("Enter 0 for rock , 1 for paper , 2 for scisssors\n")
b = random.randint(0 , 2)
c = int(a)
set = ["rock","paper","scissors"]
if c >=3 or c < 0:
    print("Input is invalid")
else:
    print(f"you chose {set[c]} and computer chose {set[b]}")
if c == b:
    print("It is a Tie")
if b == 0 and c == 2:
    print("Computer win")
if b == 1 and c == 0:
    print("Computer win")
if b == 2 and c == 1:
    print("Computer win")  
if c == 0 and b == 2:
    print("You win")
if c == 1 and b == 0:
    print("You win")
if c == 2 and b == 1:
    print("You win")
