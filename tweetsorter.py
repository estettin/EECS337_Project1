import json
import re
import spacy
import config
# import awards
import csv
import random

data = []

def loadTweets(year):
	# print("year: ", year)
	name = 'csvs/tweets' + year + '.csv'
	# print("name: ", name)
	with open(name, 'r') as f:
		reader = csv.reader(f)
		data = list(reader)
	data=data[0]

	# print("length: ", len(data))
	if len(data) > 400000:
		random.shuffle(data)

	data = data[:400000]
	return data


# data = tweets2013
def sortTweet(tweet, award):
	mustnot = award.mustnot
	foundmn = False
	for mn in mustnot:
		if mn in tweet:
			return False
	# check regex
	found = False
	found = regexCheck(tweet, award)
	if not found:
		#check keywords
		found = keywordCheck(tweet,award)
	return found


# return dictionary of tweets for each award
# def sortTweets(year, awards):
# 	data = loadTweets(year)
# 	# print("starting tweet sorting")
# 	awarddict = {}
# 	for a in awards:
# 		awarddict[a.name] = []
# 	for i in range(0,len(data)):
# 		for award in awards:
# 			# check must nots
# 			mustnot = award.mustnot
# 			foundmn = False
# 			for mn in mustnot:
# 				if mn in data[i]:
# 					foundmn = True
# 					break
# 			if foundmn:
# 				continue
# 			# check regex
# 			found = regexCheck(data[i], award)
# 			if not found:
# 				#check keywords
# 				found = keywordCheck(data[i],award)
# 			if found:
# 				awarddict[award.name].append(data[i])
# 	# for k in awarddict:
# 	 	# print(k, len(awarddict[k]))
# 	# print("Tweet Preprocessing Complete")
# 	return awarddict


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

