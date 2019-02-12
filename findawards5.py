import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.chunk import tree2conlltags
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
rt_words = ["wins", "for", "goes", "to", "dressed", "winner", "winners", "at", "win", "from", "went", "won"]
rhs_nest = [[w.lower(), w.upper(), w.title()] for w in rt_words]

rhs = [item for sublist in rhs_nest for item in sublist]
# ["wins", "Wins", "for", "goes", "to", "dressed", "Goes", "winner", "Winner", "at", "win", "Win", "WIN", "For", "FOR", "AT", "At"]

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
	thresh = [v for k,v in s[1000].items()][0]
	sorted_phrases = {k: v for k, v in phrases.items() if v > thresh}
	s_reduced = {}

	for key, val in sorted_phrases.items():
		if " - " in key:
			r = key[key.index("-") + 1:].strip()
			l = key[:key.index("-")].strip()

			tok_arr = nltk.word_tokenize(r)
			tagged = nltk.pos_tag(tok_arr)
			tree = nltk.chunk.ne_chunk(tagged)
			iob_tagged = tree2conlltags(tree)
			if iob_tagged != [] and 'PERSON' in iob_tagged[0][2]:
				key = l
				continue
			# doc = nlp(r)
			# for ent in doc.ents:
			# 	if ent.label_ == "PERSON" or ent.label_ == "WORK_OF_ART":
					
		key = key.lower()
		if "-" in key:
			key = key.replace(" - ", " ")
		if key in s_reduced.keys():
			s_reduced[key] += val
		else:
			s_reduced[key] =  val

	dup = copy.deepcopy(s_reduced)
	for k,v in dup.items():
		for phrase in dup.keys():
			if k in phrase and k != phrase:
				del s_reduced[k]
				break

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