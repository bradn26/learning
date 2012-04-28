from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, "w+") # "w" means open it in 'write' mode
# using the w+ allows you to truncate without worrying about the
# extra lines of code related to truncation below

#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

target.close() # closes the file that I just wrote / does the writing

txt = open(filename) # reopens the file

print "Here's your file %r:" % filename
print txt.read()

txt.close()