

class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("Child override")



dad = Parent()

son = Child()



dad.override()

son.override()


'''OVER RIDE MEANS
IF PARENT CLASS SAYS 2+2 = 4

IF YOU CLAIM 2+2 = 8

YOUR CLAIM WOULD BE EXECUTED PROVIDED THAT BOTH HAVE SAME FUNCTION NAME'''

