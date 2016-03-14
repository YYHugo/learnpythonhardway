from sys import argv

script, filename = argv

print "We're going to read %r." % filename
print "If you don't want that, hit Ctrl-C (^C)."
print "If you DO want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'r')

print "Reading the file."
print target.read()

print "And finally, we close it."
target.close()
