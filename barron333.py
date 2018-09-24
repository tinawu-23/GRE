#!/usr/bin/env python3 

# scrapes words (Barron333) from vocabulary.com and makes a game/pratice tool in terminal

import requests
from bs4 import BeautifulSoup
import random
import time

## Get vocabs from source ##

url = "https://www.vocabulary.com/lists/176985"
source = requests.get(url)
data = source.text
soup = BeautifulSoup(data,"html.parser")

wordlist = []
deflist = []
wrongwords = []

for word in soup.find_all('a', attrs={'class':'word dynamictext'}):
	wordlist.append(str(word).split('>')[1][:-3])
for defs in soup.find_all('div', attrs={'class':'definition'}):
	deflist.append(str(defs).split('>')[1][:-5])

barron333 = dict(zip(wordlist, deflist))


## Display word list function ##
def displaylist():
	for word,definition in barron333.items():
		print("{:>14}:  {:<}".format(word, definition))	


## Generate quiz function ## 
def generatequiz(words):
	keys = list(barron333.keys())
	random.shuffle(keys)
	shuffledlist = [(key, barron333[key]) for key in keys]

	for wordpair in shuffledlist:
		answers = {}
		answerchoice = 1
		for i in range(5):
			answers[answerchoice]=random.choice(shuffledlist)[1]
			answerchoice += 1
		answers[random.randint(1,5)] = wordpair[1]
		print(wordpair[0]+'\n')
		for answer in answers:
			print(str(answer)+': '+answers[answer])
		userchoice = input('Please enter your choice: ')
		while userchoice != '1' and userchoice != '2' and userchoice != '3' and userchoice != '4' and userchoice != '5' and userchoice != 'q':
			userchoice = input('Enter a valid choice: ')
		if userchoice == "q":
			return

		if answers[int(userchoice)]==wordpair[1]:
			print('CORRECT!')
		else:
			print('Incorrect. The definition of '+wordpair[0]+ ' is: '+wordpair[1])
			wrongwords.append(wordpair)
		print('')
		words -= 1
		if words == 0:
			return 
		time.sleep(0.5)

## Main ## 
print('\n=============== GRE Barron 333 Essential Words  ===============\n')
print('   1. Review Word List')
print('   2. Take Quiz\n')

option = int(input('Enter an option: '))
while option != 1 and option != 2:
	option = int(input('Enter valid option: '))
print('')

if option == 1:
	displaylist()
elif option == 2:
	words = int(input('How many questions would you like: '))
	print('')
	generatequiz(words)
	if len(wrongwords) == 0:
		print('You got all words correct! :)')
	else:
		print('Words you missed... ')
		for wordpair in wrongwords:
			print(wordpair[0]+': '+wordpair[1])
print('')
