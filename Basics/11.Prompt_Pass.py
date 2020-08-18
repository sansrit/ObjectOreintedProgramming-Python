# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:23:17 2020

@author: Sansrit Paudel

"""

#11.Prompt&Pass

from sys import argv

script, user_name = argv

prompt = '>'

print("HI %s, I'm the %s script." %(user_name, script))

print("I'd like  to ask you a few questions.")

print("Do you like me %s?" % user_name)

likes = input(prompt)

print("Where do you live %s?" % user_name)

lives = input(prompt)


print("What kind of computer do you have?")
computer = input(prompt)


print(
      """
        Alright, so you said %r about liking me.
        19 You live in %r. Not sure where that is.
        20 And you have a %r computer. Nice.
        
        """
        %(likes, lives, computer)
     )

