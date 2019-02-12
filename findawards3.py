import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
import random
# from populate_db import tweets2013
import spacy
import csv
from random import sample
import operator
import copy

with open('tweets2015.csv', 'r', encoding = "utf-8") as f:
  	reader = csv.reader(f)
  	tweets2015 = list(reader)[0]

punc = [".",":","!","?","#",",","<", "@"]
rhs = ["wins", "Wins", "for", "goes", "to", "Goes", "winner", "Winner", "at"]

def FindAwards(data, num_awards):
	"""
	takes in the tweets as an an array of string and identifies award names
	"""
	phrases = {}
	nlp = spacy.load("en_core_web_sm")
	for tweet in data:
		match = re.search(r"best\s|Best\s|BEST\s", tweet)
		# print(match)
		if match == None:
			continue

		# print(match.string)
		tweet_arr = re.findall(r"[\w']+|[.:,!?\#-]", tweet[match.start():])
		tweet_arr = list(filter(None, tweet_arr))
		# print(tweet_arr)

		end = 0
		found_hyph = False
		for i in range(1,len(tweet_arr)):
			if tweet_arr[i] == "-" and not found_hyph:
				found_hyph = True
			elif tweet_arr[i] in punc or (tweet_arr[i] in rhs) or (found_hyph and tweet_arr[i] == "-"):
				end = i
				if end <= 1:
					break
				p = " ".join(tweet_arr[0:end])
				if p[end-3:end] == " - ":
					p = p[:end - 3]
				if p in phrases.keys():
					phrases[p] += 1
				else:
					phrases[p] = 1
				break

	s = [{k: phrases[k]} for k in sorted(phrases, key=phrases.get, reverse=True)]
	s_reduced = {}

	for d in s:
		key = [v for v in d.keys()][0]
		if " - " in key:
			r = key[key.index("-") + 1:].strip()
			l = key[:key.index("-")].strip()
			doc = nlp(r)
			for ent in doc.ents:
				if ent.label_ == "PERSON" or ent.label_ == "WORK_OF_ART":
					key = l
					break
		key = key.lower()
		if "-" in key:
			key = key.replace(" - ", " ")
		if key in s_reduced.keys():
			s_reduced[key] += [v for v in d.values()][0]
		else:
			s_reduced[key] =  [v for v in d.values()][0]

	final_list = [{k: s_reduced[k]} for k in sorted(s_reduced, key=s_reduced.get, reverse=True)]
	awardslist = final_list[:num_awards]
	# maxcount = [v for v in final_list[0].values()][0]
	# awardslist = []
	# for a in final_list:
	# 	if [v for v in a.values()][0] >= .1*maxcount:
	# 		awardslist.append(a)
	# awardslist = [[v.title() for v in d.keys()][0] for d in awardslist]


	pprint(awardslist)

#random.shuffle(tweets2015)
x = FindAwards(tweets2015, 26)