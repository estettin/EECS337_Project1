import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from tweet_parser import df_2013
import spacy
import config
data = df_2013
# with open('gg2013.json') as f:
# 	data = json.load(f)

def findTweetsWithAwardName(data, a):
	awardname = a.regex
	friendlyname= a.name
	
	keystrings = []
	presenters = []
	stringList = []
	found = False
	for i in range(0,len(data)):
		for r in awardname:	
			x = []
			found = False
			x = re.findall(r, data[i], flags=re.IGNORECASE)
			if x:
				found = True
				break
		if found and "present" in data[i]:
			stringList.append(data[i])
	presenters = getPresenters(stringList, friendlyname)
	# print (stringList)
	if len(presenters) > 0:
		print ("Award:", friendlyname)
		print("Presenters", presenters)

def getPresenters(stringList, awardname):
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
	
	return removeDuplicatePresenters(presenters)

def containsKeywords(string, keywords):
	for k in keywords:
		if not k in string:
			return False
	return True

def removeDuplicatePresenters(presenters): #change to dictionary 
	finalpresenters = []
	for k in presenters:
		subset = False
		for kk in presenters:
			if not k == kk:
				if k in kk:
					subset = True
					presenters[kk] = presenters[kk] + presenters[k]
		if not subset:
			finalpresenters.append((k, presenters[k]))
	return finalpresenters

# class award(object):
# 	name = ""
# 	regex = ""
# 	awardtype = ""

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

# for a in awards:
# 	findTweetsWithAwardName(data, a)	
for a in config.awardarray:
	findTweetsWithAwardName(data, a)