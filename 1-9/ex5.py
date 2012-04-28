name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 #Lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
x = height * .0254 #Converts inches to meters
q = weight * .45359237 #Converts pounds to kilograms
number = "fifteen"

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "%s is %f " % (name, x)
print "%s is %d" % (name, q)

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)