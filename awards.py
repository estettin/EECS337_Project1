import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from tweet_parser import df_2013
import spacy


data = df_2013

keystrings = []

with open('gg2013.json') as f:
	data = json.load(f)


def findTweetsWithAwardName(data, awardname):
	keystrings = []
	presenters = []
	stringList = []
	#found = 0
	for i in range(0,len(data)):
		x = re.findall(awardname, data[i]["text"], flags=re.IGNORECASE)
		if x and "present" in data[i]["text"]:
			stringList.append(data[i]["text"])
	presenters = getPresenters(stringList, awardname)
	if len(presenters) > 0:
		print ("Award:", awardname)
		print("Presenters", presenters)

def getPresenters(stringList, awardname):
	stops = set(stopwords.words('english'))
	stops.update([u"host",u"hosts",u"hosting",u"goldenglobes", u"golden", u"globes", u"rt", u"http",u"@",u"#", u"movies", u"movie", u"award"])
	awardwords=' '.join(re.sub( r"([A-Z])", r" \1", awardname).split())
	awardwords=word_tokenize(awardwords)
	awardwords=[word for word in awardwords if word.isalpha()]
	awardwords=[word.lower() for word in awardwords]
	stops.update(awardwords)
	stops.remove(u"and")
	presenters = []
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
				if ent.text not in presenters:
					presenters.append(ent.text)
	#process presenters
	
	return removeDuplicatePresenters(presenters)

def removeDuplicatePresenters(presenters):
	finalpresenters = []
	for i in range(0, len(presenters)):
		subset = False
		for j in range(0,len(presenters)):
			if not i == j:
				if presenters[i] in presenters[j]:
					subset = True
		if not subset:
			finalpresenters.append(presenters[i])
	return finalpresenters


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

for a in awards:
	findTweetsWithAwardName(data, a)	


