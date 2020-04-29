# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 07:49:12 2020

@author:Sansrit Paudel
TAKING INPUT



"""

'''
while True:
    for i in ["/","- ","|","\\","|"]:
        print ("%s" % i,)
'''


#USE OF INPUT  FUNCTION input() AND STORE IN VARIABLE TO TAKE INPUT FROM USER


print("What is your Age? ")


#THE SCANNED INPUTS ARE SAVED AS STRING NEED TO CONVERT TO INT OR NUMBER TYPE FOR MATHEMATICAL CALCULATIONS




age = int(input())


print("How tall are you?")
height = input()

print("What is your weight?")
weight = input()


print("So you are %r years old %r feet tall %r kg weight" %(age, height, weight))
