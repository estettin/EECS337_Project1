import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import results 

with open('gg2013.json') as f:
	data = json.load(f)

keystrings = []

stops = set(stopwords.words('english'))
stops.update([u"host",u"hosts",u"hosting",u"goldenglobes", u"golden", u"globes", u"rt", u"http"])

for i in range(0,len(data)):
	if "host" in data[i]["text"].encode("UTF-8"):
		string = ''.join([i if ord(i) < 128 else '' for i in data[i]["text"].encode("UTF-8")])
		tstring = word_tokenize(string)
		swstring = [word for word in tstring if word.lower() not in stops]
		j = 0
		slen = len(swstring)
		while j < slen:
			if not swstring[j].isalpha():
				swstring.pop(j)
				slen = slen - 1
				continue
			if "host" in swstring[j].lower():
				swstring.pop(j)
				slen = slen - 1
				continue
			swstring[j] = swstring[j].lower()
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

print hosts