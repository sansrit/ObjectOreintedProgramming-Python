# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:40:43 2020

@author: Sansrit Paudel 

LIST IN PYTHON
enclosed on square brackets

"""
'''
num_string_list = ['one', 'two', 'three']

numbers = [1,2,3,4,5]

print(num_string_list)
'''

the_count = [2,4,6,4,5]

fruits = ['apples', 'orange', 'pears', 'apricots' ]

change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

#APPLING THE FOR LOOP THOROUGH THE LIST
# , for loop executes on loop with visiting elements on list
#for variable name in List


for number in the_count:
    print("This is a count %d " %number)



for fruit in fruits:
    print("A fruit of type %s" %fruit)
    

#we can go through mixed list too
for i in change:
    print("I got %r" %i)
    

#WE CAN BUILD UP OUR OWN LIST FIRST EMPTY AND FILL LATER

#CREATED EMPTY LIST
    
elements = []

#range method is used to create range from starting to less than ending
for i in range(0,6):
    print("Adding %d to list" %i)
    #append method is used with empty list to fill list
    elements.append(i)
   # print(elements)

print(elements)

for i in elements:
    print("Elements was: %d" %i)