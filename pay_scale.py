#!/usr/bin/python3

hrs = input("Enter Hours:")# enter the hours
h = float(hrs)#after converting it to float
rate = input("Enter rate:")
r = float(rate)
def computepay(h,r):
    if h <= 40:
        pay = h * r
    elif h > 40:
        pay = 40 * r + (h-40) * r * 1.5
    return pay
print(computepay(h,r)) 
