i = 0
numbers = []

while i < 6:
	print "at the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers # why doesn't this need a format character?
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num