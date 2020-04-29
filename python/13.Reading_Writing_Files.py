# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:28:23 2020

@author: Sansrit Paudel

                READING AND WRITING FILES



        • close—Closes the fi le. Like File- >Save.. in your editor.
        • read—Reads the contents of the fi le. You can assign the result to a variable.
        • readline—Reads just one line of a text fi le.
        • truncate—Empties the fi le. Watch out if you care about the fi le.
        • write(stuff)—Writes stuff to the fi le



"""




from sys import argv

script, filename = argv

print("We're going to erase %r."%filename)
print("If you dont want that , hit CTRL + C ")

print("If you don't want that hit return")

input("?")

print("Opening the file......")

#IMPORTANT OPENING THE FILE FOR WRITE MODE CREATE FILE OBJECT ON WRITE VARIBALE.

target = open(filename, 'w')

#w indicates the write mode


print("Truncating the file. Goodbye!")

target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file")

#WRITE ONTO THE NOTEPAD FILE CONTAINED ON A VARIABLE

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print("And finally, we close it.")

target.close()










