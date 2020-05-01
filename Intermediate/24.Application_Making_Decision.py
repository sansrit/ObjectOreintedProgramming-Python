# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:00:09 2020

@author: Sansrit Paudel

Making decisions
31
"""

print("दुइ मद्धे कुनै द्वार प्रवेश गर। ")
print("१ वा २ रोज ")

door = input(">")



if door=="1":
    print("चिसो ठाउँ आइपुग्योउ , अब के गर्छौ ?")
    print("1.बरफ खान्छु ")
    print("2.फोटो लिन्छु ")
    print("१ वा २ रोज")
    
    baraf = input(">")
    
    if baraf == "1":
        print("Tasty")
    elif baraf =="2":
        print("Nice click ")
    else:
        print("well doing %s is better" %baraf)
        

elif door=="2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print( "Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

else:
 print( "You stumble around and fall on a knife and die. Good job!")

    
    


