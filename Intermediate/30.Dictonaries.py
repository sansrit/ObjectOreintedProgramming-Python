# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:34:00 2020

@author: Sansrit Paudel
                                Dictionaries
                                
        python calls them 'dicts' other language call them 'hashes'.
"""

#uses curly bracket . This makes it different from list.

stuff = {'name': 'sansrit', 'age': 22, 'height':6}


#uses keys name for accessing the particular value 

print(stuff['name'])

print(stuff['height'])


print(stuff)

del stuff['age']

print(stuff)