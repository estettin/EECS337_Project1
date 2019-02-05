import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from populate_db import tweets2013#, tweets2015
import spacy
import config
import awards

data = tweets2013

# return dictionary of tweets for each award
def sortTweets(data, awards):
	awarddict = {}
	for a in awards:
		awarddict[a.name] = []
	for i in range(0,len(data)):
		for award in awards:
			# check must nots
			mustnot = award.mustnot
			foundmn = False
			for mn in mustnot:
				if mn in data[i]:
					foundmn = True
					break
			if foundmn:
				continue
			# check regex
			found = regexCheck(data[i], award)
			if not found:
				#check keywords
				found = keywordCheck(data[i],award)
			if found:
				awarddict[award.name].append(data[i])
	for k in awarddict:
		print(k, len(awarddict[k]))
	return awarddict


def regexCheck(tweet, award):
	regexs = award.regex
	found = False
	for r in regexs:				
		x = []
		x = re.findall(r, tweet, flags=re.IGNORECASE)
		if x:
			found = True
			break
	return found

def keywordCheck(tweet, award):
	must = award.must
	mustnot = award.mustnot
	ors = award.ors
	for m in must:
		if m not in tweet.lower():
			return False
	for mn in mustnot:
		if mn in tweet.lower():
			return False
	found = False
	for o in ors:
		if o in tweet.lower():
			found = True
	if len(ors) == 0:
		found = True
	return found


d = sortTweets(data, config.awardarray)

# a1 = config.awardarray[0]
# print(awards.findTweetsWithAwardName(a1,d[a1.name]))
# for award in config.awardarray:
	# print(awards.findTweetsWithAwardName(award,d[award.name]))
# for i in range(0,len(data)):
# 	if "presented by" in data[i]:
# 		print(data[i])

