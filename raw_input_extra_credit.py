print "What is your name?",
name = raw_input()
print "How tall are you?",
height = raw_input()
print "How old are you?",
age = raw_input()
print "What is your favorite sport?",
favorite_sport = raw_input()
print "What city do you live in?",
city = raw_input()

print '''
So your name is %s, you're %r tall, you're %r years old, your
favorite sport is %s, and you live in %s
''' % (name, height, age, favorite_sport, city)