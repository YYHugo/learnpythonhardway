qtt = 10
x = "There are %r types of people." % qtt
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)
print x
print y

# the expression %r will print quotation marks along the string, whereas %s won't
# %r displays the "raw" data of the variable
print "I said: %r." % x
print "I also said: '%s." % y

hilarious = False
joke_evaluations = "Isn't that joke so funny?! %r"

print joke_evaluations % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
