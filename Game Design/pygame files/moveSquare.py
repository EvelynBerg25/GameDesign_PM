#Evelyn Berg
#we are learning basic pygame functions

import pygame, os, time
pygame.init()

import os
os.system('cls')

WIDTH= 700  #these are pixels #dont change these!
HEIGHT= 700

#creating a dispay
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #double parethesis, like a coordinate (inputing one value instead of 2)
pygame.display.set_caption("My First Game") #title of the window
pygame.time.delay(100000)
blueClr= (0,0,225)
redClr= (255,0,0)
screen.fill(redClr)
pygame.display.update() #must do everytine you change the background or image (anything the user needs to see changing)
pygame.time.delay(100000)

#variables of the square
yb= 700
hb=50
wb= 50 #creating location for drawn shape
xb=700
speed=2
square= pygame.Rect(xb,yb,wb,hb)#create object  to draw
color= {"white":(255,255,255),"pink":(),"blue":(0,0,255), "orange":(255,218,0),"purple":(104,0,204),"yellow":(255,255,51),"black":(0,0,0),"teal":(0,153,153),"lavender":(229,204,225),"brown":(102,51,0)}
clr=color.get("white")
background= clr
run = True


keys= pygame.key.get_pressed() #provide a list of 11 keys
if keys[pygame.K_a]: # to go from side to side, copy and paste with square.y to go up and down
    square.x += speed #remember that y variable gets less as it goes UP NOT DOWN
if keys[pygame.K_d]:
    square.x += speed


    #rect(surface, color, center, radius)
    pygame.draw.rect(screen,redClr, square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, blueClr, (200,200),25)
    pygame.display.update()
    
