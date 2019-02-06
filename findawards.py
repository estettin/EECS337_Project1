import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from populate_db import tweets2013
import spacy

tweets = tweets2013
punc = [".",":","!","?","#"]
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
		if tweet[0:2] == "RT":
			continue
		if " best " in tweet.lower():
			s = ""
			doc = nlp(tweet)
			flag = False
			for element in doc:
				if element.text.lower() == "best": #found the word best
					flag = True
				if (element.text in punc or element.pos_ == "VERB" or element.pos_ == "ADP") and flag:
					#if the word is a punction, verb, or adposition ("for"), stop
					break
				if flag and element.text != ",":
					#if we have seen the word best, add the word to the string
					s = s + element.text.lower()
			if s != "best":
					#add to the dictionary
				if s in phrases:
					phrases[s] += 1
				else:
					phrases[s] = 1

	#remove keys that have only one occurance - these are most likely insignificant
	k = list(phrases.keys()).copy()
	for key in k:
		if phrases[key] <= 3:
			del phrases[key]
	return phrases

	
x = FindAwards(tweets[0:50000])



			






