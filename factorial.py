#!/usr/bin/python3

#this is a program to find out the factorial of any number

num=int(input("enter the number for which you want the factorial"))

factorial=1 #this is fixed

if num<0:
	print("negative numbers are not having factorial")

elif num==0:
	print ("0 is not having any factorial")

else:

	while num>0:
		factorial=factorial*num
		num=num-1

	print ("factorial of the number would be = ",factorial)
