import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from populate_db import tweets2013#, tweets2015
import spacy
import config

data = tweets2013

def findTweetsWithAwardName(a, tweets):
	presenters = []
	finaltweets = []
	bytweets = []
	for t in tweets:
		if "presented by" in t:
			bytweets.append(t)
		if "present" in t:
			finaltweets.append(t)
	presenters = getPresenters(finaltweets, bytweets, a.name)
	return presenters

  
	# if len(presenters) > 0:
	# 	print ("Award:", friendlyname)
	# 	print("Presenters", presenters)

def getPresenters(stringList, byStringList, awardname):
	stops = set(stopwords.words('english'))
	stops.update(["host","hosts","hosting","goldenglobes", "golden", "globes", "rt", "http","@","#", "movies", "movie", "award"])
	awardwords=' '.join(re.sub( r"([A-Z])", r" \1", awardname).split())
	awardwords=word_tokenize(awardwords)
	awardwords=[word for word in awardwords if word.isalpha()]
	awardwords=[word.lower() for word in awardwords]
	stops.update(awardwords) 
	stops.remove(u"and")
	presenters = {}
	for string in stringList:
		leftside = string.split(" present")[0]
		#print(leftside)
		leftside = ' '.join(re.sub( r"([A-Z])", r" \1", leftside).split())
		tleftside = word_tokenize(leftside)
		leftside = [word for word in tleftside if word.lower() not in stops]
		# leftside = ' '.join(leftside)
		leftside = " ".join(leftside)
		leftside = re.sub(r'\s([?.,!"](?:\s|$))', r'\1', leftside)
		#print (leftside)
		nlp = spacy.load('en_core_web_sm')
		if leftside:
			doc = nlp(leftside)
			for ent in doc.ents:
				if ent.label_ == "PERSON":
					if ent.text in presenters:
						presenters[ent.text] = presenters[ent.text] + 1
					else:
						presenters[ent.text] = 1
				#process presenters (change to dictionary)
	for string in byStringList:
		rightside = string.split("presented by")[1]
		# print(rightside)
		#print(leftside)
		rightside = ' '.join(re.sub( r"([A-Z])", r" \1", rightside).split())
		trightside = word_tokenize(rightside)
		rightside = [word for word in trightside if word.lower() not in stops]
		# leftside = ' '.join(leftside)
		rightside = " ".join(rightside)
		rightside = re.sub(r'\s([?.,!"](?:\s|$))', r'\1', rightside)
		#print (leftside)
		nlp = spacy.load('en_core_web_sm')
		if rightside:
			doc = nlp(rightside)
			for ent in doc.ents:
				if ent.label_ == "PERSON":
					if ent.text in presenters:
						presenters[ent.text] = presenters[ent.text] + 1
					else:
						presenters[ent.text] = 1
				#process presenters (change to dictionary)
	return removeDuplicatePresenters(presenters)

def containsKeywords(string, keywords):
	for k in keywords:
		if not k in string:
			return False
	return True

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

# class award(object):
# 	name = ""
# 	regex = ""
# 	awardtype = ""
"""
awards = ['Best Motion Picture(.*)Drama',
'Best Actress(.*)Motion Picture(.*)Drama',
'Best Actor(.*)Motion Picture(.*)Musical(.*)Comedy',
'Best Animated Feature Film',
'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Drama',
'Best Performance(.*)Actress(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
'Best Performance(.*)Actor(.*)(TV|Television) Series(.*)Drama',
'Best Actor(.*)Motion Picture(.*)Drama',
'Best Director(.*)Motion Picture',
'Cecil B. DeMille Award',
'Best Supporting Actor(.*)Motion Picture',
'Best Mini[\s-]*series(.*)(TV|Television) Film',
'Best Supporting Actor(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
'Best Performance(.*)Actor(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
'Best Motion Picture(.*)Musical(.*)Comedy',
'Best Actress(.*)Motion Picture(.*)Musical(.*)Comedy',
'Best Screenplay(.*)Motion Picture',
'Best Original Score',
'Best Performance(.*)Actress(.*)(TV|Television) Series(.*)Musical(.*)Comedy',
'Best Supporting Actress(.*)Series(.*)Mini[\s-]*series(.*)Motion Picture(.*)(for|made for) (TV|Television)',
'Best (TV|Television) Series(.*)Drama',
'Best Supporting Actress(.*)Motion Picture',
'Best Original Song',
'Best Foreign Language Film',
'Best (TV|Television) Series(.*)Musical(.*)Comedy',
'Best Actor(.*)(TV|Television) Series(.*)Musical(.*)Comedy']
"""
# for a in config.awardarray:
# 	print (findTweetsWithAwardName(data, a))