#Evelyn Berg
#learning to manipulate strings and using methods

import os
os.system('cls')

print('Hi') 
message = "you are awesome" #a string is an array of characters
# 0 1 2 3 4 5 6 7 ... arrays begin at zero
# you are ...

print(message)
print(message[5]) #print index (going to be r)
print(len(message)) #print length of message
print(message[len(message)-1])


#or 

wordLength = len(message)
print(wordLength)
print(message[wordLength - 1]) #length - 1 to get the last character of word

if message.isdigit()   
#when using methods add dot on end
    sum - message + 3
    print(sum)
else: #will always run else statement if if statement is wromg
    print(message + " I say so") #concatination
#if adding something only applicable to else, intent

print(message.upper()) #temporarily uppercase

message = message.upper()
print(message)

if message.upper():
    print(message)
else:
    message = message.upper()
    print(message)

num1 = 2.5
print(type(num1)) #results in ,class 'float'
print(int(num1)) #takes of decimal at end

middle = int(wordLength/2)
print(middle)
print(message[middle])

print(message[0:7]) #printing "you are awesome but letters 0 to 7"
print(message[7:10])

print(help(message.index)) #for help figuring out what index is