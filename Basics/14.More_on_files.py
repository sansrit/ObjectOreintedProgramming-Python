# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:03:05 2020

@author: Sansrit Paudel

"""

from sys import argv

#TO CHECK THE FILE IF EXISTS OR NOT


from os.path import exists

script, file1, file2 = argv

print("Copying form %s to %s " %(file1,file2 ))

#OPEN THE FILE AND STORING ON VARIABLE


in_file = open(file1)

#READ FORM FILE 1 VARIABLE TO NEXT VARIABLE


indata = in_file.read()

#RETURNS THE TOTAL LENGTH ON THE FILES


print("The input file is %d bytes long" %len(indata))


#RETURNS THE BOOLEAN VALUE IF FILE 2 EXISTS OR NOT..
print("Does the output file exists? %r" %exists(file2))

print("Ready, hit RETURN  to continue , CTRL-C to abort.")


input()

#FIRST OPEN THEN  SPECIFY THE MODE WRITE, AND STORE IN VARIBALE AND . 


file2 = open(file2, 'w')

#USING THE METHOD WRITE TO NEXT FILE NAME.

file2.write(file1)


print("Alright , all done ")

file2.close()
in_file.close()


