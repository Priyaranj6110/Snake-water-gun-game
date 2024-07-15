'''
1 for snake
0 for water
2 for gun
'''
import random
computer=random.choice([0,1,2])
meStr=input("enter the choice:")
youDict={
    "s":1,
    "w":0,
    "g":2
}
reverseDict={
    1:"s",
    0:"w",
    2:"g"
}
my=youDict[meStr]


print(f"you chose {reverseDict[my]}\n computer chose{reverseDict[computer]}")
if(computer==my):
    print("draw")
else:    
    if (computer==0 and my==1):
        print("you win")
    elif (computer==0 and my==2):
        print("you lose")    
    elif (computer==1 and my==0):
        print("you lose")       
    elif (computer==1 and my==2):
        print("you win")  
    elif (computer==2 and my==1):
        print("you lose")
    elif (computer==2 and my==0):
        print("you win")
    else:
        print("something is going wrong")            