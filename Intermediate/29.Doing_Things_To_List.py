# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:23:02 2020

@author: Sansrit Paudel

Doing Things to Lists


"""

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are 10 things in that list , let's fix that.")

stuff = ten_things.split(' ')

print(stuff)
print(len(stuff))

more_stuff = ['day', 'night', 'Song', 'Frisbee', 'Corn', 'babana', 'girl', 'boy']


while len(stuff)!=12:
    next_one = more_stuff.pop()
    print("Adding", next_one)
    stuff.append(next_one)
    print("There is %d items now." %len(stuff))
    

print(stuff)

print("Lets do some thing with stuff")

print(stuff[1])

#-1 prints the last elements on list
print(stuff[-1])

print(stuff.pop())
print(stuff.pop())

#it joins thr different elements to one 
print(' '.join(stuff))

print('#'.join(stuff[3:5]))
      
      
'''What does stuff[3:5] do?
That’s getting a “slice” from the stuff list that is from element 3 to element 4, meaning it does
not include element 5. It’s similar to how range(3,5) would work.
www.it-
'''


