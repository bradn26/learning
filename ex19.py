# this line defines the cheese and crackers function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# takes the cheese and crackers function and puts the 
	#direct numbers into the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# uses straight variables from the scrip
print "OR, we can use variabes from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# executes the script
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# allows math inside the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# combines math and variables to give the output
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)