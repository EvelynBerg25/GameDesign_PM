#Evelyn Berg

import os
os.system('cls')

number= int(input("any number")) #inpt of what number I want

if number % 2 == 0:
    print("the number is even")
else: print("the number is odd")

if number % 3 == 0:
    print("the number is a multiple of 3")

if number % 3 == 0:
    print("this number is a multiple of 5")

if number % 3 == 0 and number % 5 == 0: #making sure it doesnt glitch
    print("this number is a multiple of 5 and 3")

#if I run it with 15, it says
#any number 15
#the number is odd
#the number is a multiple of 3        
#this number is a multiple of 5       
#this number is a multiple of 5 and 3 