import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from populate_db import tweets2013#, tweets2015
import spacy
import config
import tweetsorter
from imdb import IMDb
ia = IMDb()
import string 

data = tweets2013
d = tweetsorter.d

def findWinner(a, tweets):
	wdict = {}
	dict1 = {}
	dict2 = {}
	if a.awardtype == "movie":
		for t in tweets:
			# x = re.findall("(Congrats|Congratulations) to(.*)(on|for) Winning",t, re.IGNORECASE)
			# if x:
			# 	print(x)
			#get rid of cast and crew and words with 2 capitals
			y = re.findall("(\".*\") wins best",t, re.IGNORECASE)
			if y and "best" not in y[0].lower():
				potentialtitle = re.sub(r'[^\w\s]','',y[0])
				# print(potentialtitle)
				movies = ia.search_movie(potentialtitle)
				# potentialtitlerint(movies)
				if len(movies) > 0:
					title = movies[0]["title"]
					# print(title)
					if title in wdict:
						wdict[title] = wdict[title] + 1
					else:
						wdict[title] = 1
					if title in dict1:
						dict1[title] = dict1[title] + 1
					else:
						dict1[title] = 1
			#
			# z = re.findall("WINNER:(.*)",t, re.IGNORECASE)
			# if z:
			# 	print(z)
			w = re.findall("goes to (\".*\")",t, re.IGNORECASE)
			if w: # and "goldenglobes" not in w[0].lower() and "golden globes" not in w[0].lower():
				#remove quotes and punctuation 
				potentialtitle = re.sub(r'[^\w\s]','',w[0])
				# print(potentialtitle)
				movies = ia.search_movie(potentialtitle)
				# potentialtitlerint(movies)
				if len(movies) > 0:
					title = movies[0]["title"]
					# print(title)
					if title in wdict:
						wdict[title] = wdict[title] + 1
					else:
						wdict[title] = 1

					if title in dict2:
						dict2[title] = dict2[title] + 1
					else:
						dict2[title] = 1
		winner = determineWinner(wdict)
		print (winner)
		return winner
	else:
		stops = set(stopwords.words('english'))
		stops.update(["wins","hosting","goldenglobes", "golden", "globes", "rt", "http","@","#", "movies", "movie", "award"])
		awardwords=' '.join(re.sub( r"([A-Z])", r" \1", a.name).split())
		awardwords=word_tokenize(awardwords)
		awardwords=[word for word in awardwords if word.isalpha()]
		awardwords=[word.lower() for word in awardwords]
		stops.update(awardwords) 
		# stops.remove(u"and")
		for t in tweets:
			y = re.findall("(.*) wins best",t, re.IGNORECASE)
			if y and not "best" in y[0]:
				leftside = y[0]
				leftside = ' '.join(word for word in leftside.split() if word[0]!='#' and not '@' in word and word[0]!='"')
				tleftside = word_tokenize(leftside)
				leftside = [word for word in tleftside if word.lower() not in stops]
				leftside = ' '.join(leftside)
				# print(leftside)
				nlp = spacy.load('en_core_web_sm')
				if leftside:
					doc = nlp(leftside)
					for ent in doc.ents:
						if ent.label_ == "PERSON":
							if ent.text in wdict:
								wdict[ent.text] = wdict[ent.text] + 1
							else:
								wdict[ent.text] = 1
		print (a.name, wdict)
	# print(a.name, dict1)
	# print(a.name, dict2)
	# print(a.name, wdict)
	

#First word check and check year

# get rid of punctuation
# get rid of stop words


def determineWinner(d):
	maxkey = ""
	maxval = -1
	for k in d:
		if d[k] > maxval:
			maxval = d[k]
			maxkey = k
	return maxkey.lower()

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



a = config.awardarray



for award in a:
	if not award.awardtype == "movie":
		findWinner(award,d[award.name])
		






# for award in config.awardarray:
# 	findWinner(award, d[award.name])