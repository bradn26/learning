import random

# Operate the quiz script by typing 1 for true and 0 for false, type quit or press ctrl+c to quit.
# Written By Ninja@Quakenet

# Check answer function:
def check_answer(answer, task_id):
	# Set correct message, wrong message and error message
	correctmsg	=	"Correct!"
	wrongmsg	=	"Wrong answer, the correct answer was __%s__" % answers[task_id]
	error1		= 	"Error in function, first if."
	error2		= 	"Error in function, second if."
	
	if answers[task_id] == True:
		if answer == "1":
			print (correctmsg)
		elif answer == "0":
			print (wrongmsg)
	elif answers[task_id] == False:
		if answer == "0":
			print (correctmsg)
		elif answer == "1":
			print (wrongmsg)
		else:
			print (error2)
	else:
		print (error1)


# Tasks and answers:
tasks 	=		["not False","not True", "True or False", "True or True", "False or True", "False or False", "True and False", "True and True", "False and True", "False and False", "not(True or False)", "not(True or True)", "not(False or True)", "not(False or False)", "not(True and False)", "not(True and True)", "not(False and True)", "not(False and False)", "1!=0", "1!=1", "0!=1", "0!=0", "1==0", "1==1", "0==1", "0==0" ]
answers	=		[True, False, True, True, True, False, False, True, False, False, False, False, False, True, True, False, True, True, True, False, True, False, False, True, False, True]

# The highest index in tasks[]
max_task_id = 26

################################################################################################
print("\n"* 5)
print (">>> Operate the quiz script by typing 1 for true and 0 for false, type quit or press CTRL-C to exit\n")
answer = raw_input("press ENTER to continue \n")
print("\n"*20)

# Starting quiz loop
while answer != "quit":
	task_id = random.randrange(0,max_task_id)
	task = tasks[task_id]
	print (task), "\n"
	answer = raw_input('Answer: ')
	check_answer(answer, task_id)
	print ("\n")


print "Thanks for playing!"
