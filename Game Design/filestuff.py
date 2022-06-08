#Evelyn Berg
#program about using files, 'r' is read 'a' is append 'w' is write datetime
#when you open a file must make sure you close it (if you dont close it from the previous thing it wont work)
#file to save score for certian times instead of eevrything deleting after game is completed
import random
import os, datetime

os.system("cls")
#using library datetime, can vring date/time by themselves
date=datetime.datetime.now() #for current date and time
print(date)
print(type(date.strftime("%m /%d %Y")))
#Y for year must be uppercase

name ="Maria"
sce=344 #want to make string line to put into my fine (score is a number, letters in a string)
scrLine=str(sce)+"/t"+date.strftime("%m-%d-%y")+ "/t" 

#creating a file (must know the name of the file, call file something easy)
myFile = open("abc.txt") # must let it know what youre opening the file for
myFile.read(scrLine)
myFile.close()
#create new line ( as soon as you opne with write, deletes everything in file that was there before)
# use append to create keepable record

#create a file
myFile=open("abc", 'r')
myFile.read(scrLine)
myFile.close()


