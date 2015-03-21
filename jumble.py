import sys

def printInput():
	print 'Enter a string: '
	return raw_input()

def validateInput(inputStr):
	if len(inputStr.split()) != 1:
		return False
	else:
		return True


#Driver

while not validateInput(userInput = printInput()):
	print 'Improper input, try again...'


