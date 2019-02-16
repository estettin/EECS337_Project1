import json
import nltk
from pprint import pprint
import re
import spacy
import config
from imdb import IMDb
ia = IMDb()
import string 
import helpers

def findWinner(a, t, wdict, count, winnertweets):
	if a.awardtype == "movie":
		y = re.findall("(\".*\") wins best",t, re.IGNORECASE)
		if y and "best" not in y[0].lower():
			potentialtitle = re.sub(r'[^\w\s]','',y[0])
			if not helpers.containsCeremonyName(potentialtitle):
				wdict[potentialtitle] += count
				if potentialtitle in winnertweets:
					winnertweets[potentialtitle].append(t)
				else:
					winnertweets[potentialtitle] = [t]
		w = re.findall("goes to (\".*\")",t, re.IGNORECASE)
		if w: 
			#remove quotes and punctuation 
			potentialtitle = re.sub(r'[^\w\s]','',w[0])
			if helpers.containsCeremonyName(potentialtitle):
				wdict[potentialtitle] += count
				if potentialtitle in winnertweets:
					winnertweets[potentialtitle].append(t)
				else:
					winnertweets[potentialtitle] = [t]
		return 
	else:
		keystrings = []
		y = re.findall("(.*) wins best",t, re.IGNORECASE)
		if y and not "best" in y[0].lower():
			# print(y[0])
			leftside = y[0]
			leftside = ' '.join(word for word in leftside.split() if word[0]!='#' and not '@' in word and word[0]!='"')
			y2 = re.findall("((?:[A-Z][a-z]+) (?:[A-Z][-a-zA-Z]+))", leftside)
			if y2:
				for name in y2:
					if not helpers.containsCeremonyName(name):
						keystrings.append(name)
		if len(keystrings) > 0:
			for k in keystrings:
				wdict[k] += count
				if k in winnertweets:
					winnertweets[k].append(t)
				else:
					winnertweets[k] = [t]

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
