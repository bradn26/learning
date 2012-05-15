from sys import exit



def start():
	print "You wake up in the morning and it is sunny out"
	print "You can go surfing, rock climbing, biking, go to a baseball game, or watch movies all day."
	print "Which would you like to do?"
	
	next = raw_input("> ")
	
	if next == "surfing":
		surfing()
	elif next == "rock climbing":
		rock_climbing()
	elif next == "biking":
		biking()
	elif next == "baseball":
		baseball()
	elif next == "movies":
		movies()
	else:
		print "Come again?"


def surfing():
	print "It's very nice out so you don't need a wetsuit."
	print "There aren't many people at the beach."
	print "Would you like to try and do a trick?"
	trick = False

	while True:
		next = raw_input("> ")
		hurt = "Well, it didn't quite work. Looks like you'll be heading home with an ice pack."
				
		if next == "yes":
			print hurt
		elif next == "no":
			print "Good idea, maybe next week. Make sure to keep applying the sunscreen throughout the day"					
			print "There is still time in the day to do something else, how about another activity?"
			
			next = raw_input("> ")

			if next == "rock climbing":
				rock_climbing()
			elif next == "biking":
				biking()
			elif next == "baseball":
				baseball()
			elif next == "movies":
				movies()
			else:
				print "Come again?"
			
	
def rock_climbing():
	print "The rock gym looks like a good idea."
	print "Would you like to go bouldering or top-roping?"
		
	next = raw_input("> ")
	blister = '''Tried a little too much for one day, maybe you should stick to the 
	bouldering caves for a while longer? Your hands will be feeling it for the next week!'''

	if next == "bouldering":
		print "What a good time, you'll be sore tomorrow but... It's all good."
	elif next == "top-roping":
		print blister
	else:
		print "What? I don't understand you."

def biking():
	print "Great choice, would you like to go for a mountain or road ride?"
	
	next = raw_input("> ")
	sore = "You'll be sleeping well tonight after that ride"
	bloody = '''
	The mountain lion chases you down an mauls you, hopefully you have 'Find My Friends' enabled
	so your friends can tell the authorities where to look. Who'd have thought taunting would have worked?
	'''	
		
	if next == "road":
		print sore
	elif next == "mountain":
		print "There is a mountain lion in the middle of the trail... What to do?"
		print "You could taunt it, or run away... Decisions, decisions..."
	else:
		print "Get with it, let's try that again."
	while next != "taunt" and next != "run":
		next = raw_input("> ")
		
		if next == "taunt": # something goes wrong here
			print "Crazy enough to work, the mountain lion ran away!"
			print "You'll have a story to tell about that one!"
		elif next == "run": # something goes wrong here too
			print "Unfortunately, you've scared the mountain lion, and now he is chasing you"
			print "You can go 'left' or 'right'!"
			
			raw_input("> ")
			
			if next == "left":
				print bloody
			elif next == "right":
				print "You escaped. Congratulations!"
		while next != "left" and next != "right":		
			next = raw_input("> ")	
			print "You need to pay better attention!"
			print "Let's try that again."
		

def baseball():
	print "The Giants are playing the Dodgers and the A's are playing the Red Sox"
	print "Would you like to go to the game in Oakland or San Francisco?"
	
	next = raw_input("> ")
	oakland = '''Josh Reddick went 5/5 with 5 home runs. Too bad they were off Beckett, 
	they shouldn't even count!, that guy is terrible'''
	san_francisco = "Matt Cain pitched a perfect game! What an exciting night!"

	if next == "San Francisco":
		print san_francisco
	elif next == "Oakland":
		print oakland
	else:
		print "Green's has both games on, so if you can't make up your mind you might as well go there."
		
def movies():
	print "What a shame, you're spending the whole day inside."
	print "How about you reconsider your options?"
	
	print "How about something more active instead?"
	next = raw_input("> ")
	
	if next == "surfing":
		surfing()
	elif next == "rock climbing":
		rock_climbing()
	elif next == "biking":
		biking()
	elif next == "baseball":
		baseball()
	else:
		print "Come again?"
	
start()


