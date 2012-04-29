x = "There are %d types of people." % 10 #This incorporates a string that has an integer in it
binary = "binary" #This line creates a text string with the word binary in it
do_not = "don't"#This creates a text string with the word don't in it
y = "Those who know %s and those who %s" % (binary, do_not) #This creates a formatted string that calls upon previous strings of 'binary' and 'don't'

print x #prints the x string
print y #prints the y string

print "I said: %r." % x #This line prints out a formatted string that calls upon 'x'
print "I also said: '%s'." % y #This line prints out a formatted string that calls upon 'y'

#creates a text string that is a boolean value
hilarious = False #'false' is a boolean value
joke_evaluation = "Isn't that joke so funny?! %r" #this creates a formatted string that calls up a boolean value

print joke_evaluation % hilarious #creates a string that calls upon a boolean value

w = "This is the left side of..." #creates a text string
e = "a string with a right side." #creates a text string

print w + e # This combines two variables that have text string that appears 2 sided
 