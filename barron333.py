#!/usr/bin/env python3 

# scrapes words (Barron333) from vocabulary.com and makes a game/pratice tool in terminal

import requests
from bs4 import BeautifulSoup

url = "https://www.vocabulary.com/lists/176985"
source = requests.get(url)
data = source.text
soup = BeautifulSoup(data,"html.parser")

wordlist = []
deflist = []

for word in soup.find_all('a', attrs={'class':'word dynamictext'}):
	wordlist.append(str(word).split('>')[1][:-3])
for defs in soup.find_all('div', attrs={'class':'definition'}):
	deflist.append(str(defs).split('>')[1][:-5])

barron333 = dict(zip(wordlist, deflist))

for word,definition in barron333.items():
	print(("{}: {}").format(word,definition))
