# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:23:29 2020

@author: Sansrit Paudel
" VARIABLES AND NAMES"""


cars = 100

space_in_car = 4.0

drivers = 30

passengers = 90

cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capacity = cars_driven * space_in_car

average_passengers_per_car = passengers/cars_driven


print("There are ", cars, "available.")

print("There are only", drivers, "available.")

print("There will be ", cars_not_driven, "Empty cars today.")

print("We can transport", carpool_capacity, "people today" )



#DIFFERENCE BETWEEN SINGLE = AND == IS
#SINGLE EQUALS ASSIGNS VALUE TO THE VARIABLE
# DOUBLE EQUALS CHECKS THE EQUALITY. COMPARS IF TWO VALUE ARE EXACTLY SAME 



