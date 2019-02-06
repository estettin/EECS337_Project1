import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
# from populate_db import tweets2013
import spacy
import csv
from random import sample

with open('tweets2013.csv', 'r') as f:
  	reader = csv.reader(f)
  	tweets2013 = list(reader)[0]
  

punc = [".",":","!","?","#","-", ",","<"]
lhs = ["wins", "Wins", "for", "wins" "#goldenglobe" "golden globe" "Golden Globe"]
rhs = ["goes", ""]

"""
Phrases to look for:
wins _______ for
the award for
wins
"""


def FindAwards(data):
	"""
	takes in the tweets as an an array of string and identifies award names
	"""
	phrases = {}
	nlp = spacy.load("en_core_web_sm")
	for tweet in data:
		match = re.search("best\s|Best\s", tweet)
		# print(match)
		if match == None:
			continue

		# print(match.string)
		tweet_arr = re.findall(r"[\w']+|[.:,!?\#-]", tweet[match.start():])
		tweet_arr = list(filter(None, tweet_arr))
		# print(tweet_arr)

		end = 0
		for i in range(len(tweet_arr)):
			if tweet_arr[i] in punc:
				end = i
				p = " ".join(tweet_arr[0:end]).lower()
				if p in phrases.keys():
					phrases[p] += 1
				else:
					phrases[p] = 1
				break

		

	pprint(phrases.keys())
	s = [{k: phrases[k]} for k in sorted(phrases, key=phrases.get, reverse=True)]
	
	# for k in list(s[0].keys())[:50]:
		# pprint("%s: %s" % (k, s[0][k]))

	pprint(s[:50])


x = FindAwards(tweets2013)


			