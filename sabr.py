prompt = '>'

print "Hi, I would like to ask you a few questions about your season."
print "What is your name?"
name = raw_input(prompt)

print "How many at-bats did you have %s?" % name
atbats = float(raw_input(prompt))

print "How many hits did you have %s?" % name
hits = float(raw_input(prompt))

average = hits / atbats

print "So %s, your batting average is %.3f." % (name, average)