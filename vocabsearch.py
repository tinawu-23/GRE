#!/usr/bin/env python3 

# quick search of a vocab
# usage: ./vocabsearch

import sys
import requests
from bs4 import BeautifulSoup


def usage(exit_code=0):
	print('''\nUsage: {} word
	-e: example sentences
	-s: synonyms
	-a: antonyms \n'''.format(sys.argv[0]))
	sys.exit(exit_code)

def definition(word):
	url = "https://www.vocabulary.com/dictionary/"+word
	source = requests.get(url)
	data = source.text
	soup = BeautifulSoup(data,"html.parser")

	definition = str(soup.find('meta', attrs={'name':'description'})).split('=')[1][1:-6]
	if 'Try the world\'s fastest, smartest dictionary' in definition:
		definition = "cant find this word :|"
	print("\n{}\n".format(definition))
	sys.exit(0)

def example(word):
	url = "https://wordsinasentence.com/{}-in-a-sentence/".format(word)
	source = requests.get(url)
	data = source.text
	try:
		data = data[data.index("var txts = [")+14:]
	except:
		print('cant find sentences :(')
		return 
	for line in data.split('];')[0].split('\','):
		if line.strip() != '\'' and line.strip() != '\'\'':
			print(line.strip()[1:])
			print('*')
	
def synonym(word):
	url = "https://www.thesaurus.com/browse/"+word
	source = requests.get(url)
	data = source.text
	try:
		data = data[data.index("\"pos\":\"adj\",\"synonyms\":[")+24:]
		data = data[:data.index("],\"antonyms\":")]
	except: 
		print('\ncant find synonyms :|\n')
		return 
	for line in data.split('},'):
		print(((line.split(',')[-1]).split(":")[-1]).replace("\"","").replace("}",""))

def antonym(word):
	url = "https://www.thesaurus.com/browse/"+word
	source = requests.get(url)
	data = source.text
	try:
		data = data[data.index("}],\"antonyms\":")+15:]
		data = data[:data.index("]}],\"synonyms\":[],\"antonyms\":[],")]
	except:
		print('\ncant find antonyms :|\n')
		return
	for line in data.split('},'):
		print(((line.split(',')[-1]).split(":")[-1]).replace("\"","").replace("}",""))

	
if __name__ == '__main__':
	if len(sys.argv) == 1:
		usage(0)
	elif len(sys.argv) == 2:
		definition(sys.argv[1])
	else:
		args = sys.argv[2:]
		while len(args) and args[0].startswith('-') and len(args[0]) > 1:
			arg = args.pop(0)
			if arg == '-e':
				print('\n*')
				example(sys.argv[1])
				print()
			elif arg == '-s':
				synonym(sys.argv[1])
			elif arg == '-a':
				antonym(sys.argv[1])
			else:
				usage(1)
