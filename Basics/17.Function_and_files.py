# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:56 2020

@author: Sansrit Paudel
"""

from sys import argv

script, input_file = argv


def print_all(jpt ):
    print(jpt.read())
    


def rewind(f):
    f.seek(0)
    

def print_a_line(line_count, f):
    print(line_count, f.readline())
    


#the filename that gets passed which gets opened and stored on varibale current_file
    

current_file = open(input_file)


print("Lets print the whole file")



#CALL FUNCTION TO READ FILE 

print_all(current_file)

#ALTER WITHOUT CALLING FUNCTION #print(*current_file)


#C:\python>python 17.Function_and_files.py input_file.txt

print("Lets rewind , kind of like a tape.")

rewind(current_file)


print("Let's print three lines:")


#PASSING TO A FUNCTION FOR LINE COUNT AND FILE TO READ LINE

current_line = 1
print_a_line(current_line, current_file)


current_line = current_line+1
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)






