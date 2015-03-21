import sys, re

global userInput

def printInput():
	global userInput
	print 'Enter a string: '
 	userInput = raw_input()
	return userInput

def validateInput(inputStr):
	if len(inputStr.split()) != 1 or not re.match(r'^[a-zA-Z\']+$', inputStr):
		return False
	else:
		return True

#Driver

#reading dictionary into trie

def createTrie():
	root = dict()
	with open('aspell-en-dict.txt') as readFile:
	    for line in readFile:
	    	word_dict = root
	    	line = line.strip()
	    	for character in line:
	    		word_dict = word_dict.setdefault(character, {})
	    	word_dict = word_dict.setdefault('null', 'null')
	return root

print createTrie()



    		
    	

#while not validateInput(printInput()):
#	print 'Improper input, try again...'

#print 'Valid Input: ' + userInput


