# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:25:29 2020

@author: Sansrit Paudel

Mapping with Dictonaries using key value 

"""

states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }

cities = {
        
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }




#add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'


print(cities)


#print out some cities

print('-'*50)

print("NY State has:", cities['NY'])
print("OR state has:", cities['OR'])

#print some states
print('-'*50)

print( "Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-'*50)

print("Michigan has:", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])


#print every state abbreviation
print('-'*50)

for state, abbrev in states.items():
    print("%s is abbreviated %s" %(state, abbrev))
    
#print every cities abbreviation
print('-'*50)

for cities,abbrev in cities.items():
    print("%s has the city %s" %(cities, abbrev))
    
    
print('-'*50)


state = states.get('TX', 'Does Not Exist')
print(state)


'''
What the difference between a list and a dictionary?
A list is for an ordered list of items. A dictionary (or dict) is for matching some items (called “keys”)
to other items (called “values”).
'''