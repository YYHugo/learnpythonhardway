class Parent(object):

    def implicitInheritance(self):
        print("Parent implicit")


class Child (Parent):
    pass

# Instantiating new objects
dad = Parent()
son = Child()

dad.implicitInheritance()
# son should print Parent function
son.implicitInheritance()
