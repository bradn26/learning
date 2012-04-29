tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """ 
I'll do a list 
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
""" #Can also use three single quotes ('''), this is easier because you 
	#don't need to backspace and key around

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Combining an escape sequence and a format
print "Start the day on a \nnewline, %s sometime." % tabby_cat

print "1\r2"
print "12\b3"

#Ask Jack about the usability of escape sequences