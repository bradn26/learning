i = 0
numbers = []

for i in range(0, 6): # I think something went a bit wrong with this for loop
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num