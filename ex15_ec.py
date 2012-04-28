# adding features for python has to the script so I can use them
from sys import argv

# adds filename as a variable
script, filename = argv

# opens a specified text file
txt = open(filename)

# presents the file name
print "Here's your file %r:" % filename
# prints the file
print txt.read()

# requests the file name for a raw input
print "Type the filename again:"

# allows the raw input of a filename
file_again = raw_input("> ") # extra credit 4 requires getting rid of this confusing

# opens the file that is requested
txt_again = open(file_again)

# prints the file that is requested
print txt_again.read()