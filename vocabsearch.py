#!/usr/bin/env python3 

# quick search of a vocab
# usage: ./vocabsearch {word}

import sys
import requests
from bs4 import BeautifulSoup

url = "https://www.vocabulary.com/dictionary/"+sys.argv[1]
source = requests.get(url)
data = source.text
soup = BeautifulSoup(data,"html.parser")

definition = str(soup.find('meta', attrs={'name':'description'})).split('=')[1][1:-6]
if 'Try the world\'s fastest, smartest dictionary' in definition:
	definition = "cant find this word :|"
print("\n{}\n".format(definition))


