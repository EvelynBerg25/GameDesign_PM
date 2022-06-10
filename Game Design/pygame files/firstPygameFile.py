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
pygame.time.delay(3000)
blueClr= (0,0,225)
redClr= (255,0,0)
screen.fill(blueClr)
pygame.display.update() #must do everytine you change the background or image (anything the user needs to see changing)
pygame.time.delay(3000)

yb= 300
hb=50
wb= 50 #creating location for drawn shape
xb=100
square= (xb,yb,wb,hb)#create object  to draw
color= {"white":(255,255,255),"pink":(),"blue":(0,0,255), "orange":(255,218,0),"purple":(104,0,204),"yellow":(255,255,51),"black":(0,0,0),"teal":(0,153,153),"lavender":(229,204,225),"brown":(102,51,0)}
clr=color.get("white")
background= blueClr
run = True
while run:
    screen.fill(background)
    for event in pygame.event.get(): 
        if event.type:
            run = False
            print('you quit')
    #rect(surface, color, center, radius)
    pygame.draw.rect(screen,redClr, square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, blueClr, (200,200),25)
    pygame.display.update()




