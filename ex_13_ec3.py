from sys import argv

script, name = argv

#name = raw_input("What is your name? ")
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")

print "The script is called:", script
print "Your name is %s." % name
print "You are %r years old." % age
print "You are %r tall." % height

#Have Jack look at this code to see what the hell is going on here.