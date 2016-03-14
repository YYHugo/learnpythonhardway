def inches2centimerters(inch):
    return (inch * 2.54)

def pounds2Kilogram(lbs):
    return (lbs * 0.453592)

name = 'Zed A. Shawn'
age = 35 # not a lie
height = 74  # inches
weight = 180 # lbs


cm_height = inches2centimerters(height)
kg_weight = pounds2Kilogram(weight)

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall or %d centimeters tall." % (height, float(cm_height))
print "He's %d pounds heavy or %d kilograms heavy." % (weight, kg_weight)
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
