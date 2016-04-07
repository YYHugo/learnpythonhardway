def looping(repeat, inc):
    i = 0
    numbers = []

    while i < repeat :
        print "At the top i is %d" % i
        numbers.append(i)

        i += inc
        print "Number now: ", numbers
        print "At the bottom i is %d\n" % i

    print "The numbers: "

    for num in numbers :
        print num

n = int(raw_input("How many loops? \n >"))
inc = int(raw_input("In steps of \n >"))
looping(n, inc)