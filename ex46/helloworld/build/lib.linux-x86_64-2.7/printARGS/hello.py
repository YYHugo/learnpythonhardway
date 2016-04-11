import sys

def func(self):
    arguments = sys.argv

    for args in xrange(0, len(arguments)):
        print("The {}th argument is: {}".format(args, arguments[args]))

    print("THE END")
