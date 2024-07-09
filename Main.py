import random
'''
1 for snake
-1 for water
0 for gun

'''

computer = random.choice([0, -1, 1])

youstr = input("Enter Your Choice, Snake(s), Water(w), Gun(g) :")

youDict = {
    "w": -1,
    "s": 1,
    "g": 0
}

reverseDict = {
    -1: "Water",
     1: "Snake",
     0: "Gun"
}

you = youDict[youstr]

print(f"You Chose {reverseDict[you]} \n Computer Chose {reverseDict[computer]}")

if(computer == you):
    print("Its A Draw")

else:
        if(computer == -1 and you == 1):
             print("You Win!")
        elif(computer == -1 and you == 0 ):
              print("You Lose!")
        elif(computer == 1 and you == -1):
              print("You Lose!")
        elif(computer == 1 and you == 0):
              print("You Lose!")  
        elif(computer == 0 and you == -1):
              print("You Win!")
        elif(computer == 0 and you == 1):
              print("You Lose!")
        else:
              print("Something Went Wrong")