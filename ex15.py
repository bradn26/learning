# bringing in another library to import stuff
from sys import argv

# adds filename as a variable that is assigned from the command line argument
script, filename = argv

# opens a specified text file
txt = open(filename)

# presents the file name
print "Here's your file %r:" % filename
# prints the file
print txt.read()

txt.close() #closes the file

# requests the file name for a raw input
print "Type the filename again:"

# allows the raw input of a filename
file_again = raw_input("> ")

# opens the file that is requested
txt_again = open(file_again)

# prints the file that is requested
print txt_again.read()

txt_again.close() #closes the file