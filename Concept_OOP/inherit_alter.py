'''

The third way to use inheritance is a special case of overriding where you want to alter the behavior
before or after the Parent class’s version runs

'''

class Parent(object):

    def altered(self):
        print("parent altered()")




class Child(Parent):

    def altered(self):
        print("Child before parent altered()")
'''Switches to alter method on parents'''
'''use of super with argument class name of child with self argument and method of parent'''
        super(Child, self).altered()
        print("Child after parent altered()")


dad = Parent()

son = Child()


dad.altered()
son.altered()



