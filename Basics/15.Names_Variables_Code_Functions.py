# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:40:35 2020

@author: Sansrit Paudel

FUNCTION IS DEFINED WITH def followed by function name and parameters and end the line with a colon : and start indenting



"""


#RECEIVES TWO ARGUMENTS AND STORE ON VARIABLES RESPECTIVELY]
'''
we want *args (asterisk args), which is a lot like your argv parameter but
for functions. This has to go inside () parentheses to work.
'''


#INDENT THE FUNCTION WITH A FOUR SPACE


def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))
    

#CATCHES THE TWO ARGUMENTS FORM THE FUNCTION CALL AND USE THEM ACOORDINGLY
    
def print_two_again(arg1, arg2):
    print("arg1: %r , arg2: %r" %(arg1, arg2))
    

def print_one(arg1):
    print("arg1: %r" %arg1)
    


def print_none():
    print("I got nothing.")
    


#SUPPLYING THE ARGUMENTS RESPSECTIVELY
    
#IT IS ALSO CALLED THE SUPPLYING THE PARAMENTS TO FUNCTIONS
    
print_two("sansrit", "Paudel")


#FUNCTION CALL
print_two_again("Zed", "Shaw")

print_one("First")

print("none")



'''
What does the * in *args do?
That tells Python to take all the arguments to the function and then put them in args as a list. It’s
like argv that you’ve been using, but for functions. It’s not normally used too often unless specifi -
cally needed.



'''