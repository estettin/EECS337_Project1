import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from tweet_parser import df_2013

data = df_2013
def getHostNames(data):
	keystrings = []

	stops = set(stopwords.words('english'))
	stops.update(["host","hosts","hosting","goldenglobes", "golden", "globes", "rt", "http"])

	for i in range(0,len(data)):
		if "host" in data[i]:
			string = ''.join([i if ord(i) < 128 else '' for i in data[i]])
			tstring = word_tokenize(string)
			swstring = [word for word in tstring if word.lower() not in stops]
			j = 0
			slen = len(swstring)
			while j < slen: 
				swstring[j] = swstring[j].lower()
				if not swstring[j].isalpha():
					swstring.pop(j)
					slen = slen - 1
					continue
				if "host" in swstring[j].lower():
					swstring.pop(j)
					slen = slen - 1
					continue
				j = j + 1
			if len(swstring) > 1:
				keystrings.append(list(nltk.bigrams(swstring)))

	finalbigrams = []

	for x in keystrings:
		if x not in finalbigrams:
			finalbigrams.append(x)

	d = {}
	for x in finalbigrams:
		for y in x:
			if y in d:
				d[y] = d[y] + 1
			else:
				d[y] = 1

	maxCount = -1
	maxKey = ""
	hosts = []
	for k in d:
		if d[k] > maxCount:
			maxCount = d[k]
			maxKey = k
	## top 2 (are they names)
	for k in d:
		if d[k] > (maxCount*4/5):
			hosts.append(k[0].capitalize() + " " + k[1].capitalize())

	print(hosts)

getHostNames(data)