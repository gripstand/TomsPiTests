
import random

# set all my variables

encourage=["Nice try","No cigar","Sorry","Where is the force when you need it","Good guess","Dang","Good effort","Not this time","Nada","Hmmmm no...","Buzzzz no"]
count=int(1)
gi=int(1)
message=str() 
correct=random.randrange(100)

######################
# evaluates guess
#####################

def checkguess(guess, correct):
	if guess > 100:
		message="please guess a number less than 100"
	elif guess > correct:
		message="you are too high!"
	elif guess < correct:
		message="you are too low!"
	else:
		message="you got it!"
	return message

############
# Generates error message for bad input
###########

def get_qualified_input(prompt,test_function,error_msg):
    while True:
        try:
            result = test_function(input(prompt))
        except:
            pass
        else:
    		return result
    	print(error_msg)


################
# checks for positve int input
################

def test_positive_int(x):
    try:
        if int(x) > 0:
           return int(x)
    except:
        pass
    raise Exception("Invalid")


def divline():
	print ("--------------------------------------------------------------------------------")

def increment():
	global count 
	count+=1

########
# Main Program here
########



# welcome the user

print ("Lets play guess the number!!")
print ("You will try and guess and I will tell you if it's too high, or too low")
divline()

# Ask user to set guess limit

guesslimit=get_qualified_input("How many guesses should I give you? ",test_positive_int, "Please only use whole numbers (idiot)")


print ("ok - here we go with guess number one of %s!" % guesslimit)
#while count != guesslimit:
while True:
	divline()
	guess=get_qualified_input("Make your guess number %s: " % count,test_positive_int, "That is a stupid guess but it still counts!")
	message=checkguess(guess,correct)
	if guess==correct:
		print("You da man and you did it in only %s tries!" % count)
		break
	elif count==guesslimit:
		print("FAIL!!!! The number I picked was %s" % correct)
		break
	else:
		enc=random.randrange(len(encourage))
		print("%s, but %s. That was try number %s" % (encourage[enc], message, count))
		print ("You have %d left" % (guesslimit-count))
		increment()
		divline()

print("Good Game!!!!")
