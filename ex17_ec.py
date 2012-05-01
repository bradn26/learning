from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
input = open(from_file); indata = input.read(); print "The file is %d bytes long. \nDoes the output file exist? %r \nReady, hit RETURN to continue, CTRL-C to abort." % (len(indata), exists(to_file)); raw_input(); open(to_file, 'w').write(indata); print "Alright, all done."


# need to make this script shorter somehow / general tips on shortening scripts
# figure out what 'cat' does
