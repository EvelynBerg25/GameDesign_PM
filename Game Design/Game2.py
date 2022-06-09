#Evelyn Berg
#guessing numbers game (to make instructions in file, exit from menu)

#write pseudocode for Guessing Number program
#Instructions in a file, printed when number one is selected
#choice for printing scoreboard (limited to top 5 scores, sorted high to low) 
#user can leave game only from menu

#random.randint(1, 25)

import random 
import os

os.system('cls')

name= input("WHAT IS YOUR NAME? ")
instr= open("Game Design/scoregame2.txt",'r')

menu= input(""">>>>>>>>>>>>>>>>>>>>   GUESS THE NUMBER   <<<<<<<<<<<<<<<<<<<
<  <      <    TYPE A NUMBER AND PRESS ENTER     >      >   >
<  <      <         INSTRUCTIONS - PRESS 1       >      >   >
<  <      <           LEVEL ONE - PRESS 2        >      >   >
<  <      <           LEVEL TWO - PRESS 3        >      >   >
<  <      <          LEVEL THREE - PRESS 4       >      >   >
<  <      <            TO EXIT - PRESS 5         >      >   >
<><><><><><><><><><><>>>>>>>>>><<<<<<<<<<><><><><><><><><><><""")



if menu== 1:
    print("1")

while True:
    choice= menu
    choice=int(choice)
    if choice > 0 and choice < 6: #so that i can specify
        if choice ==1:
            myFile = instr
            content = myFile.readlines()
            print(content)
            myFile.close()
        
        if choice ==2:
            answer= random.randint(1,25)

            guess1 = input("enter your guess: ")
            if guess1 == answer:
                print("you're correct!")
                break #restart game here
            else:
                print("sorry, try again!") #if you get it wrong you can try again
                

#lev1=
#lev2=
#lev3=
#exit=

#answer = random.randint(1, 25)

#answer= random.randint(1,25)

