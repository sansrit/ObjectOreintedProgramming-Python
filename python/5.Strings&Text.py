# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:23:39 2020

@author: Sansrit Paudel

        STRINGS AND TEXT
        
        We use %r for debugging, since it displays the “raw” data of the variable, but we use %s and
others for displaying to users.

        
"""

x = "There are %d types of people." %10

# variable can hold strings . so easy


binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary , do_not)

print(x)
print(y)


print("I said : %r." %x)

print("I also said: '%s'." %y)

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"


#note this method is super cool.

print(joke_evaluation % hilarious)


w = "you and I"
e = " We are together"


#this is also called con catenation

print(w+e)



