# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:08:33 2020

@author: Sansrit Paudel
"""

def add(a,b):
    print("Adding %d + %d" %(a,b))
    return(a+b)
    



def subtraction(a,b):
    print("Subtracting %d - %d" %(a,b))
    return(a-b)
    
    

def multiply(p,k):
    print("Multiplying %d * %d" %(p,k))
    return(p*k)
    

def divide(a,b):
    print("Dividing %d / %d" %(a,b))
    return(a/b)
    



print("Lets do some maths with some functions")


age = add(30,5)
print(age)
height = subtraction(78,4)
print(height)
weight = multiply(90,2)
print(weight)
iq = divide(100,2)
print(iq)

print("Age: %d, Height: %d,   Weight: %d,  IQ: %d" %(age,height, weight, iq))


#operation would perform inside out.. i.e first divide , and mulitply and subtract and add


what = add(age, subtraction(height, multiply(weight, divide( iq,2) ) ))

print(what)

#PERFORMS DIVIDE AND ADD THEN SUBTRACT
random = 24+34/100-1023
print(random)


    