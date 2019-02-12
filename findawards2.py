import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords, treebank_chunk
from nltk.tokenize import word_tokenize 
import re
import random
# from populate_db import tweets2013
import spacy
import csv
from random import sample
import operator
import copy


with open('tweets2015.csv', 'r') as f:
  	reader = csv.reader(f)
  	tweets2015 = list(reader)[0]
  

punc = [".",":","!","?","#",",","<"]
lhs = ["wins", "Wins", "for"]
rhs = ["wins", "Wins", "for", "goes", "to", "dressed", "Goes", "winner", "Winner", "at"]

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
	# nlp = spacy.load("en_core_web_sm")
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

	print(len(phrases.keys()))

	s = [{k: phrases[k]} for k in sorted(phrases, key=phrases.get, reverse=True)]
	thresh = [v for k,v in s[1000].items()][0]
	sorted_phrases = {k: v for k, v in phrases.items() if v > thresh}

	
	# sorted_phrases = s[0]
	# for d in s[1:5000]:
	# 	sorted_phrases.update(d)

	sorted_phrases2 = {}
	for k in sorted_phrases.keys():
		s = nltk.word_tokenize(k)
		tagged = nltk.pos_tag(s)
		entities = nltk.chunk.ne_chunk(tagged)
		# pprint(entities)
		new_p =""
		print(k)
		for chunk in entities:
			if hasattr(chunk, 'label') and chunk.label:
				if chunk.label() == 'PERSON':
					break
				else:
					print(chunk)
					new_p = new_p + ' '.join(child[0] for child in chunk.leaves())


				# print(ent, new_p)
				# print(new_p)

		print(new_p)
		if new_p == '':
			continue
		else:
			if new_p.title() in [p.title() for p in sorted_phrases2.keys()]:
				sorted_phrases2[new_p.title()] += sorted_phrases[k]
			else:
				sorted_phrases2[new_p.title()] = sorted_phrases[k]

	# for k in sorted_phrases2.keys()
			
		# elif [p.lower().find(new_p) for p in sorted_phrases2.keys()] != -1:
		# 	pass
		# else:

	dup = copy.deepcopy(sorted_phrases2)

	
	for k,v in dup.items():
		for phrase in dup.keys():
			if k in phrase and k != phrase:
				del sorted_phrases2[k]
				break
				
				

	# pprint(sorted_phrases2)
	# pprint(phrases.keys())
	
	s2 = [{k: sorted_phrases2[k]} for k in sorted(sorted_phrases2, key=sorted_phrases2.get, reverse=True)]
	# for k in list(s[0].keys())[:50]:
		# pprint("%s: %s" % (k, s[0][k]))
	# print(sorted_phrases2)
	pprint(s2[:27])

# random.shuffle(tweets2015)
x = FindAwards(tweets2015)