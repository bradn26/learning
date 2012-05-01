# Calls in argv from the command line
from sys import argv

# establishes a list where you use the script, then an input file is established
script, input_file = argv

# prints the file
def print_all(f):
	print f.read()

# recalls the first line of the file
def rewind(f):
	f.seek(0)

# prints a recalled line
def print_a_line(line_count, f):
	print line_count, f.readline()

# opens the given file
current_file = open(input_file)

print "First, let's print the whole file:\n"

# prints the file
print_all(current_file)


print "Now let's rewind, kind of like a tape."

# goes back to the top of the file
rewind(current_file)

print "Let's print three lines:"

# prints the first line of the current file
current_line = 1
print_a_line(current_line, current_file)

# prints the next line of the current file
current_line = current_line + 1
print_a_line(current_line, current_file)

# prints the next line of the current file
current_line = current_line + 1
print_a_line(current_line, current_file)