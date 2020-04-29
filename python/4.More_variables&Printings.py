# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:42:17 2020

@author: Sansrit
28

MORE VARIABLES AND PRINTINGS
        FORMATTERS

        “format string".
        %s    for strings
        %d    for numbers
        %r    print no matter what
        
        

Every time you put " (double- quotes) around a piece of text,
you have been making a string.

In this exercise you will learn how to make strings that have variables
embedded in them.

MORE DETAILS ON PYTHON FORMAT CHARACTERS

"""

my_name = 'sansrit paudel'
my_age = 21
my_height = 6.0 #feet
my_weight = 76 #kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'grey'



print("let's talk about %s" % my_name)

print("He is %d feet tall." % my_height)

print("He is %d kg heavy."  % my_weight)

print("He has got %s eyes and %s hair" %(my_eyes, my_hair))


print("If I add %d,%d and %d I get %d" %(my_age , my_height , my_weight , my_age + my_height + my_weight ))


#to round off the number we simply can use round function

print(round(1.57))




