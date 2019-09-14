#!/usr/bin/python3


#this program is for the guess number game

import random 
#importing the module 


hidden=random.randrange(1,10)

guess=int(input("enter the number=  "))

if guess==hidden:
	print ("you got it ")

elif guess<hidden:
	print ("too less")

else:
	print("too high")
