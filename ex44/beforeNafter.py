class Parent(object):

    def altered(self):
        print "This is parent function."


class Child(Parent):

    def altered(self):
        # CHILD, BEFORE PARENT function alter
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
