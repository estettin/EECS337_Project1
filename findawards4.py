import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import re
import spacy
import csv
import copy
from nltk.chunk import tree2conlltags


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

def FindAwards(data, num_awards):
	"""
	takes in the tweets as an an array of string and identifies award names
	"""
	phrases = {}

	# nlp = spacy.load("en_core_web_sm")
	for tweet in data:
		match = re.search(r'best\s|Best\s|BEST\s', tweet)
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
				if i+1 >= len(tweet_arr):
					tok_arr = nltk.word_tokenize(' '.join([j for j in tweet_arr[i:]]))
				else:
					tok_arr = nltk.word_tokenize(' '.join([j for j in tweet_arr[i+1:i+3]]))
				tagged = nltk.pos_tag(tok_arr)
				tree = nltk.chunk.ne_chunk(tagged)
				iob_tagged = tree2conlltags(tree)
				if iob_tagged != [] and 'PERSON' not in iob_tagged[0][2] and iob_tagged[0][0] != '-':
					continue

			if tweet_arr[i] in punc or (tweet_arr[i] in rhs) or (found_hyph and tweet_arr[i] == "-"):
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
	print("DONE")
	print(len(phrases.keys()))

	s = [{k: phrases[k]} for k in sorted(phrases, key=phrases.get, reverse=True)]
	thresh = [v for k,v in s[1000].items()][0]
	sorted_phrases = {k: v for k, v in phrases.items() if v > thresh}


	sorted_phrases2 = {}
	for k in sorted_phrases.keys():
		# st = nltk.word_tokenize(k)
		# tagged = nltk.pos_tag(st)
		# print(tagged)

		# entities = nltk.chunk.ne_chunk(tagged)
		# print(entities)
		# pprint(entities)
		new_p = k
		# # print(k)
		# for chunk in tagged:
		# 	if chunk[1] == 'PERSON':
		# 		break
		# 	if chunk[1] == ':':
		# 		new_p = new_p + chunk[0] + ' '
		# 	else:
		# 		print(chunk[0])
		# 		new_p = new_p + ' ' + chunk[0]


				# print(ent, new_p)
		# print(new_p)

		# print(new_p)
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
	for k in list(s[0].keys())[:50]:
		pprint("%s: %s" % (k, s[0][k]))
	# print(sorted_phrases2)
	pprint(s2[:num_awards])

# random.shuffle(tweets2015)
x = FindAwards(tweets2015, 26)