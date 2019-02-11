import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
import spacy
import config
from imdb import IMDb
ia = IMDb()
import string 
from collections import Counter


def findNominees(a, tweets):
	keystrings = Counter()
	ndict = Counter()
	# takes too long
	for t in tweets:
		"""
		#find names within any sentence
		s = re.findall("(.*)(nominee|nomina)(.*)",t,re.IGNORECASE)
		if s:
			tw = cleanTweet(t,a)
			#or find names using the spacy entity
			s2 = re.findall("([A-Z][a-z]+(?=\s[A-Z])(?:\s[A-Z][a-z]+))",tw)
			if s2:
				# print (t)
				# print (s2)
				for i in s2:
					keystrings.append(i)
		"""

		#check these
		r = re.findall("(.*) (?:(?:not win)|(?:is a lock)|(?:should win)|(?:should not win)|(?:better not win)|(?:didn\'t win)|(?:doesn\'t win)|(?:deserves to win)|(?:deserved to win)|(?:better win)|(?:is nominated for)|(?:was nominated for)|(?:will win)|(?:should've won)|(?:could win)|(?:has to win)|(?:is going to win)|(?:is gonna win)|(?:win ))", t, re.IGNORECASE)
		if r and r[0] and "congrat" not in r[0].lower():
			# find # or @
			r1 = re.findall("([#@](?:[A-Z][a-z]*)(?:[A-Z][a-z]+))",r[0])
			if r1:
				for e in r1:
					e = cleanTweet(e,a)
					if not e == "":
						keystrings[e] += 1
					# print(e)
			#if its a movie look for quoted things
			if a.awardtype == "movie":
				r2 = re.findall("(\".*\")",r[0])
				if r2:
					e = cleanTweet(r2[0],a)
					if not e == "":
						keystrings[e] += 1
			#find titles
			r3 = re.findall("([A-Z](?:[a-z]+|\.)(?:\s+[A-Z](?:[a-z]+|\.))*(?:\s+[a-z][a-z\-]+){0,2}\s+[A-Z](?:[a-z]+|\.))",r[0]) #get titles #https://stackoverflow.com/questions/7653942/find-names-with-regular-expression
			if r3:
				for e in r3:
					e = cleanTweet(e,a)
					if not e == "":
						keystrings[e] += 1

		# the hashtag or users
		n = re.findall("Best(.*)nominee ([#@][A-z][a-zA-Z]*)", t, re.IGNORECASE)
		if n:
			keystrings[cleanTweet(n[0][1],a)] += 1
	# print(keystrings)
	ndict = nomineesCounter(keystrings,a)	
	nominees = ndict.most_common(10)
	finalnominees = []
	for n in nominees:
		finalnominees.append(n[0])
	return finalnominees

def nomineesCounter(c,a):
	atype = a.awardtype
	ndict = Counter()
	for k in c:
		count = c[k]
		if atype == "movie":
			if len(k.split(" ")) < 7:
				movies = ia.search_movie(k)
				if len(movies) > 0:
					title = movies[0]["title"]
					ndict[title] += count
		else:
			if len(k.split(" ")) < 4:
				nlp = spacy.load('en_core_web_sm')
				doc = nlp(k)
				for ent in doc.ents:
					if ent.label_ == "PERSON":
						ndict[ent.text] = count
	return ndict







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
	stops.update(["elvis", "duran", "perez","hilton","news","vanity","fair", "host","hosts","hosting","goldenglobes", "golden", "globes", "oscar","oscars", "movies", "yahoo", "rt", "http","@","#", "movies", "movie", "award", "win", "wins", "globe", "&"])
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


# "(didn\'t win)|(doesn\'t win)|(deserves to win)|(deserved to win)|(better win)|(is nominated for)|(was nominated for)", re.IGNORECASE)

'''
nominees are 
hope/thought "(hop(e|ed|ing|es)|thought) (.*) w(on|in)"
'''


