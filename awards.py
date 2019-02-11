import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
import spacy
import config
import tweetsorter
from collections import Counter

def findPresenters(a, tweets):
	presenters = []
	finaltweets = []
	bytweets = []
	possnames = Counter()
	for t in tweets:
		# if "presented by" in t:
		# 	bytweets.append(t)
		# if "present" in t:
		# 	finaltweets.append(t)
		# r = re.findall("(.*)and(.*)present(?:s|ed|ing)", t, re.IGNORECASE)
		ha = re.findall("(.*)present(?:s|ed|ing)", t, re.IGNORECASE)
		if ha:
			h1 = re.findall("([#@](?:[A-Z][a-z]*)(?:[A-Z][a-z]+))",t)
			if h1:
				for e in h1:
					e = cleanTweet(e,a)
					if " " in e:
						possnames[e] += 1
			h2 = re.findall("((?:[A-Z][-A-Za-z]*)(?:\s[A-Z][-A-Za-z]+))", ha[0])
			if h2: 
				for e in h2:
					e = cleanTweet(e,a)
					if " " in e:
						possnames[e] += 1
			morenames = getNames(ha[0],a)
			for name in morenames:
				possnames[name] += 1
					# print(e)
					# possnames.append()
		ha2 = re.findall(" presented by (.*)", t, re.IGNORECASE)
		if ha2:
			morenames = getNames(cleanTweet(ha2[0],a),a)
			for name in morenames:
				possnames[name] += 1
					# print(e)
					# possnames.append()
	pres = possnames.most_common(3)
	finalpresenters = []
	for p in pres:
		finalpresenters.append(p[0])
	return finalpresenters

def getNames(tweet, award):
	names = []
	cleaned = cleanTweet(tweet,award)
	#print (leftside)
	nlp = spacy.load('en_core_web_sm')
	if cleaned:
		doc = nlp(cleaned)
		for ent in doc.ents:
			if ent.label_ == "PERSON":
				names.append(ent.text)
			#process presenters (change to dictionary)
	return names




def removeDuplicatePresenters(presenters): #change to dictionary 
	presenterslist = []
	d = {}
	for k in presenters:
		presenterslist.append((k, presenters[k]))
	# finalpresenters = []
	# print(presenterslist)
	l = len(presenterslist)
	i = 0
	while i < l:
		subset = False
		j = 0
		# print("i", i, presenterslist[i])
		while j < l:
			# print ("j",j, presenterslist[j])
			if not i == j and i < l:
				if presenterslist[i][0] in presenterslist[j][0]:
					subset = True
					presenterslist[j] = (presenterslist[j][0], presenterslist[j][1] + presenterslist[i][1])
					l = l - 1
					presenterslist.pop(i)
					# print("i", i, presenterslist[i])
					j = -1
			j = j + 1
		i = i + 1 
	# print(presenterslist)
	for t in presenterslist:
		d[t[0]] = t[1]
	return d


def cleanTweet(t, award):
	tweet = t
	#separate words with 2 caps
	tweet = tweet.replace('@',"")
	tweet = tweet.replace('#',"")
	r = re.sub("(?<=\w)([A-Z])", r" \1", tweet) # split at capital letter
	if r:
		tweet = " ".join(r.split())
	# remove stopwords
	awardname = award.name
	stops = set(stopwords.words('english'))
	stops.update(["elvis", "duran","perez","hilton","news","vanity","fair", "host","hosts","hosting","goldenglobes", "golden", "globes", "oscar","oscars", "movies", "yahoo", "rt", "http","@","#", "movies", "movie", "award", "win", "wins", "globe", "&"])
	awardwords=' '.join(re.sub( r"([A-Z])", r" \1", awardname).split())
	awardwords=word_tokenize(awardwords)
	awardwords=[word for word in awardwords if word.isalpha()]
	awardwords=[word.lower() for word in awardwords]
	stops.update(awardwords) 
	stops.remove(u"and")
	stops.remove(u"or")
	stops.remove(u"don")
	stops.update(["to", "win", "best", "if"])
	tweet = word_tokenize(tweet)
	tweet = [word for word in tweet if word.lower() not in stops]
	return " ".join(tweet)
