'''
First I will show you the implicit actions that happen when you defi ne a function in the parent,
but not in the child.

Very handy for repetitive code you need in many classes.
'''

class Parent(object):

    def implicit(self):
        print("Parent Implicct()")

    
'''passing parent on child class means inheritate properties form parents'''

class Child(Parent):
    pass



dad = Parent()
son = Child()


dad.implicit()


'''Access thorough object son from child class'''
son.implicit()


'''
The use of pass under the class Child: is how you tell Python that you want an empty block.
This creates a class named Child but says that there’s nothing new to defi ne in it. Instead, it will
inherit all its behavior from Parent.
'''