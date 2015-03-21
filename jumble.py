import sys, re

global userInput

def printInput():
	global userInput
	print 'Enter a string: '
 	userInput = raw_input()
	return userInput

def validateInput(inputStr):
	if len(inputStr.split()) != 1 or not re.match(r'^[a-zA-Z]+$', inputStr):
		return False
	else:
		return True


#Driver

while not validateInput(printInput()):
	print 'Improper input, try again...'

print 'Valid Input: ' + userInput
