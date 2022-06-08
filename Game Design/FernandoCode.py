#Evelyn Berg
#sunctions and saving files

import random 
import os

os.system('cls')
from time import sleep 
seconds=.5

list1= ["123"]
list2= ["123"]
list3= ["123"]
count= 0
Game= True
theword= ""
high= 0
name= input("What is your name?")

def hint(): #allows us to reuse code in multiple spots
    global count
    if count == 0: 
        print("------------------------------------------------")
        print("              here is a new hint                ")
        print(" these _ have _")
        print("------------------------------------------------")

    elif count == 1:
        print("------------------------------------------------")
        print("            here is your final hint             ")
        print(" these _ have _")
        print("------------------------------------------------")

else:
    print("you're horrible at guessing! no more hints. good luck!")

def selectWord(choice):
    global theword
    if choice == 1:
        theword = random.choice(list1)
    if choice == 2:
        theword = random.choice(list2)
    if choice == 3:
        theword = random.choice(list3)
    return theword

while Game:
    os.system('cls')
    print("------------------------------------------------")
    print("                guess the color                 ")
    print()




