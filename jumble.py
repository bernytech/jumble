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
	print 'Enter a word that contains only alphabetical characters and/or apostrophe: '
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

def all_perms(pList):
    if len(pList) == 0:
    	yield []
    elif len(pList) == 1:
    	yield pList
    else:
    	iList = []
    	for i in range(len(pList)):
    		element = pList[i]
    		rElements = pList[:i] + pList[i+1:]
    		for p in all_perms(rElements):
    			yield [element] + p

#Driver

trie = createTrie()

while not validateInput(printInput()):
	print 'Improper input, try again...'

validWords = set()
for p in all_perms(list(userInput)):
	word = "".join(p)
	if isValidWord(trie, word):
		validWords.add(word)
print validWords

