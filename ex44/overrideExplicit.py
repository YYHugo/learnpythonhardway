class Parent(object):

    def override(self):
        print("Parent function")


class Child (Parent):

    def override(self):
        print("CHILD: I know what I'm doing. Overriding father's function...")

# Instantiating new objects
dad = Parent()
son = Child()

dad.override()
# son should print Parent function
son.override()
