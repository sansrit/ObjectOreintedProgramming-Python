# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:04:08 2020

@author: Sansrit Paudel

more practise on functions and variables 
"""


def break_words(stuff):
#THIS split METHOD HELPS TO SPLIT THE WORDS
    words = stuff.split(' ')
    return words

#FUNCIONS DEFINATIONS
    
#SORTING THE WORDS
def sort_words(words):
    return(sorted(words))

def print_first_word(words):
    word = words.pop(0)
    print(word)
    
def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return(sort_words(words))
    
def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_word(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    

sentence = ("Sansrit Paudel is the game changer in programming world")


#PASSING THE FUNCTIONS

#METHOD TO SPLIT WITH SPACE
splitted =  break_words(sentence)
print(splitted)

#METHOD SORTED IS USED TO SORT FROM CAPITAL ABC TO a,b,c
sorted_word = sort_words(sentence)
print(sorted_word)


sort_senten = sort_sentence(sentence)
print(sort_senten)



first_last = print_first_and_last(sentence)
print(first_last)






