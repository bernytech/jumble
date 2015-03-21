import sys, re

global userInput

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

def printInput():
	global userInput
	print 'Enter a word that contains only alphabetical characters and hyphen (e.g. don\'t): '
 	userInput = raw_input()
	return userInput

def validateInput(inputStr):
	if len(inputStr.split()) != 1 or not re.match(r'^[a-zA-Z\']+$', inputStr):
		return False
	else:
		return True

def isValidWord(trie, userInput):
	word_dict = trie
	for character in userInput:
		if character in word_dict:
			word_dict = word_dict[character]
		else:
			return False
	else:
		if 'null' in word_dict:
			return True
		else:
			return False


#Driver

trie = createTrie()

while not validateInput(printInput()):
	print 'Improper input, try again...'

if isValidWord(trie, userInput):
	print 'This is indeed a valid dictionary word: ' + userInput
else:
	print 'Word not found in the dictionary: ' + userInput



