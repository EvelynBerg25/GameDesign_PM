#Evelyn Berg
#guessing numbers game (to make instructions in file, exit from menu)

#write pseudocode for Guessing Number program
#Instructions in a file, printed when number one is selected
#choice for printing scoreboard (limited to top 5 scores, sorted high to low) 
#user can leave game only from menu

#random.randint(1, 25)

import datetime
import random 
import os

os.system('cls')

name= input("WHAT IS YOUR NAME? ")
instr= open("Game Design/scoregame2.txt",'r')
cnt= 0
high=0
Game= True
score= 200-40*cnt

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
            content = myFile.readlines() #operation on closed file error?
            print(content)
            myFile.close()
        
        if choice ==2:
            answer= random.randint(1,25)
            print(answer)
            guess = input("enter your guess: ")
            if guess == answer:
                print("you're correct!")
                break #restart game here
            else:
                print("sorry, try again!")
                 #if you get it wrong you can try again
            #cnt+=1  
            #if cnt ==5:
               # print("Sorry! Better luck next time")
            #break 
        if choice ==3:
            answer= random.randint(1,50)
            print(answer)
            guess = input("enter your guess: ")
            if guess == answer:
                print("you're correct!")
                break 
            else:
                print("sorry, try again!")
            cnt+=1  
            if cnt ==5:
                print("Sorry! Better luck next time")
            break
        if choice ==4:
            answer= random.randint(1,100)
            print(answer)
            guess = input("enter your guess: ")
            if guess == answer:
                print("you're correct!")
                break 
            else:
                print("sorry, try again!")
            cnt+=1  
            if cnt ==5:
                print("Sorry! Better luck next time")
            break
        if choice ==5:
            Game= True
            score= 200-40*cnt

            if score > high:   # find highest sce
                high=score
                print(name+", your score is "+str(score))
                input("Press enter ")
                os.system('cls')
                print("<><><><><><><><><><><><>")
                answer=input("Do yo want to play again? ")
                if ('n' or 'N') in answer:
                        Game=False
                        print("Thank you for playing my game" )
            if ('y' or 'Y') in answer:
                #break
                abc= 0
        print("your highest score is " + str(high))
        abc=+1
        date=datetime.datetime.now() #for current date and time
        if abc ==2:
            print(date and name and score)

                        

