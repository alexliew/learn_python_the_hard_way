class Parent(object):
    def altered(self):
        print("Parent altered()")

class Child(Parent):
    def altered(self):
        print("Child, before parent altered()")
        # the two argument form can work OUTSIDE methods, i.e. super(<class name>, <object of that class/subclass>)
        # super(Child, self).altered()
        # without arguments, works only within a method
        super().altered()
        print("Child, after parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
