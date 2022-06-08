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

instr= input(""">>>>>>>>>>>>>>>>>>>>   GUESS THE NUMBER   <<<<<<<<<<<<<<<<<<<
<  <      <    TYPE A NUMBER AND PRESS ENTER     >      >   >
<  <      <         INSTRUCTIONS - PRESS 1       >      >   >
<  <      <           LEVEL ONE - PRESS 2        >      >   >
<  <      <           LEVEL TWO - PRESS 3        >      >   >
<  <      <          LEVEL THREE - PRESS 4       >      >   >
<  <      <            TO EXIT - PRESS 5         >      >   >
<><><><><><><><><><><>>>>>>>>>><<<<<<<<<<><><><><><><><><><><""")

if instr== 1:
    print("1")

#lev1=
#lev2=
#lev3=
#exit=



#myFile = open("Game Design/scoregame2.txt", 'r')
#content = myFile.readlines()
#print(content)
#myFile.close()

