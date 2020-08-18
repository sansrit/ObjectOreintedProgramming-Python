class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    K=3



''' Everything inside class name and pass to variable like to create an object'''

happy_bday = Song(["Happy Birthday to you ", 
                    "I don't want to get sued",
                        "So I'll stop right there"])
                

'''Object has been created'''


bulls_on_prade = Song(["They rally around the family ",
                      "With pockets full of shells"])

print(type(happy_bday))


happy_bday.sing_me_a_song()

bulls_on_prade.sing_me_a_song()

'''Change the variable on object '''

happy_bday.K = 7
print(happy_bday.K)


'''"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts.
 This method called when an object is created from the class and it allow the class to initialize the attributes of a class.'''


'''
 self in Python class. self represents the instance of the class.
  By using the “self” keyword we can access the attributes and methods of the class in python. 
  It binds the attributes with the given arguments. The reason you need to use self.
'''

