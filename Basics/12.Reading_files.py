# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:27:18 2020

@author: Sansrit Paudel
    
    READING FILES
    
"""

from sys import argv

script, filename = argv

#OPEN FUNCTOION IS USED FOR OPENING FLE
#OPEN STORE TO VARIABLE AND READ



txt = open(filename)

print("Here is your file: %r " %filename)


#VARIABLE WITH read() METHOD APPLIED


print(txt.read())

print("Type the filename again:")

file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())


#TO run from command line 
#C:\python>python 12.Reading_files.py Nepal.txt
