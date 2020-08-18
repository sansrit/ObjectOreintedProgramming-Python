# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:02:24 2020

@author: Sansrit Paudel

    FUNCTIONS AND VARIABLES
    
"""

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("you have %d cheeses!" % cheese_count)
    print("you have %d boxes of crackers!" %boxes_of_crackers)
    
    print("Man that's not enough for a party")
    print("Get a blanket. \n")
    
    

print("We can just give function numbers directly:")

cheese_and_crackers(20,30)

print(" OR, we can use variable from our script:")

amount_of_cheese = 10
amount_of_crackers = 15

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")

cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variable and math:")

cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

    

