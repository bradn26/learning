from sys import exit
from random import randint

class Bike_Ride(object):
	
	def __init__(self, start):
			self.quips = [
			"What a ride, you'll be tired tomorrow.",
			"Make sure to ice, you'll want to keep DOMS to a minimum.",
			"Remember to stretch, don't want to get injured.",
			]
			self.thoughts = [
			"Looks like you'll have to wait another week, the bike needs to see a mechanic.",
			"Maybe you should have gone mountain biking instead, you've broken your road bike.",
			"Ouch, that'll cost you. Maybe mountain biking wasn't such a bad idea after all."
			]
			self.start = start
		
	def play(self):
		next = self.start
		
		while True:
			print "\n----------------"
			scene = getattr(self, next)
			next = scene
			
	def finished(self):
		print self.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
	def broken(self):
		print self.thoughts[randint(0, len(self.thoughts)-1)]	
		
	def getting_ready(self):
		print "What a beautiful day in NorCal."
		print "It's so nice out, it would be a crime not to make it out on the bike"
		print "to get some exercise."
		print "\n"
		print "You could go 'road' biking or 'mountain' biking."
		print "Which would you like to do?"
		
		action = raw_input("> ")
		
		if action.lower() == "road":
			print "Great choice, it looks like you have some maintenance to do"
			print "on your bike before you can get on the road."
			print "You need to re-pack your bearings in a certain combination"
			print "to keep your pedals functioning properly."
			print "You can't mess around with this too long or else you might break it."
			combination = "%d%d%d" % (randint(1,5), randint(1,5), randint(1,5))
			guess = int(raw_input("[Combination]> "))
			guesses = 1
			cheat_code = 267
						
			while (guess != combination and guess != cheat_code) and guesses < 10:
				if guess > code:
					print "Crunch! That's not quite right, try a higher combination."
				if guess < code:
					print "Crunch! That's not quite right, try a lower combination."
				guesses += 1
				guess = int(raw_input("[Combination]> "))
				
				if guess == combination or guess == cheat_code:
					print "Click!"
					print "-------------------------------------"
					print "Perfect, now you can get on the road."
					return 'the_road_ride'
				else:
					return 'broken'
					
		if action.lower() == "mountain":
			print "Sounds good. Your bike is in great shape."
			print "Would you like to go riding in 'Golden Gate Park' or 'Marin'?"
			