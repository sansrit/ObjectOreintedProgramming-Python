# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:31:28 2020

@author: Sansrit Paudel
"""

print("Let's practice everythings")

print(" you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = (""" 
     \t The lovely bird
     with logic so firmly planted
     cannot discern \n     the needs of love 
     nor comprehend passion from intuition and
     requires an explanation
     \n\t\t where there is none.     
""")

print("-----------------------------------")

print(poem)

print("-----------------------------------")


five = 10-2+3-6
print("This should be five: %s" %five)

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/100
    return(jelly_beans, jars, crates)
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With the starting point of: %d" %start_point)
print("We have %d jars, %d beans and %d crates"%(beans, jars, crates))




