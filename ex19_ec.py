def beer_and_chicken(beer_count, boxes_of_chicken):
	print "You have %d beers!" % beer_count
	print "You have %d boxes of chicken!" % boxes_of_chicken
	print "That's enough for the Red Sox Starting Rotation!"
	print "Forget the playoffs.\n"
	
	
print "Direct input of the numbers:"
beer_and_chicken(15, 6)

print "Using the variables from the script:"
amount_of_beer = 20
amount_of_chicken = 10

beer_and_chicken(amount_of_beer, amount_of_chicken)

print "Doing some math inside!:"
beer_and_chicken(12 + 3 * 2 / 3.0, 3 + 7 * 3 / 2.0)

print "Combining variables and mathemtics:"
beer_and_chicken(amount_of_beer + 2, amount_of_chicken + 5)

print "variables on left, math on the right:"
beer_and_chicken(amount_of_beer, 12 + 6)

print "math on the left, variables on the right"
beer_and_chicken(4 + 3 * 2, amount_of_chicken)

print "math and variables combined on the left, direct on the right"
beer_and_chicken(amount_of_beer + 5, 226)

print "Direct on the left, math and variables on the right"
beer_and_chicken(313, amount_of_chicken + 12)

print "using script variables and math"
amount_of_beer = 777

beer_and_chicken(amount_of_beer, 13)

print "using script variables and math take #2"
amount_of_chicken

beer_and_chicken(11223, amount_of_chicken)