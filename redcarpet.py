import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from populate_db import tweets2013 #, tweets2015

class RedCarpet(object):
	bestDressed = ""
	worstDressed = ""

	def __init__(self, best, worst):
		self.bestDressed = best
		self.worstDressed = worst

def getBestAndWorstDressed(tweets=None):
	if tweets == None:
		tweets = tweets2013
	bkeystrings = []
	wkeystrings = []

	stops = set(stopwords.words('english'))
	stops.update(["best","worst","dressed","goldenglobes", "golden", "globes", "rt", "http", "outfit", "dress", "tux", "gown", "tuxedo", "eredcarpet"])

	for i in range(0,len(tweets)):
		if "best dressed" in tweets[i] and "worst" not in tweets[i]:
			bstring = ''.join([z if ord(str(z)) < 128 else '' for z in tweets[i]])
			btstring = word_tokenize(bstring)
			bswstring = [word for word in btstring if word.lower() not in stops]
			j = 0
			slen = len(bswstring)
			while j < slen:
				if not bswstring[j].isalpha():
					bswstring.pop(j)
					slen = slen - 1
					continue
				bswstring[j] = bswstring[j].lower()
				j = j + 1
			if len(bswstring) > 1:
				bkeystrings.append(list(nltk.bigrams(bswstring)))
		elif "worst dressed" in tweets[i] and "best" not in tweets[i]:
			wstring = ''.join([i if ord(i) < 128 else '' for i in tweets[i]])
			wtstring = word_tokenize(wstring)
			wswstring = [word for word in wtstring if word.lower() not in stops]
			j = 0
			slen = len(wswstring)
			while j < slen:
				if not wswstring[j].isalpha():
					wswstring.pop(j)
					slen = slen - 1
					continue
				wswstring[j] = wswstring[j].lower()
				j = j + 1
			if len(wswstring) > 1:
				wkeystrings.append(list(nltk.bigrams(wswstring)))

	bfinalbigrams = []
	wfinalbigrams = []

	for x in bkeystrings:
		if x not in bfinalbigrams:
			bfinalbigrams.append(x)

	for x in wkeystrings:
		if x not in wfinalbigrams:
			wfinalbigrams.append(x)

	bd = {}
	wd = {}

	for x in bfinalbigrams:
		for y in x:
			if y in bd:
				bd[y] = bd[y] + 1
			else:
				bd[y] = 1

	for x in wfinalbigrams:
		for y in x:
			if y in wd:
				wd[y] = wd[y] + 1
			else:
				wd[y] = 1

	bmaxCount = -1
	bmaxKey = ""
	wmaxCount = -1
	wmaxKey = ""

	# print("BEST")
	for k in bd:
		# if bd[k] > 5:
			# print(k, bd[k])
		if bd[k] > bmaxCount:
			bmaxCount = bd[k]
			bmaxKey = k
	# print("max: ", str(bmaxKey), ", ", str(bmaxCount))
	# print("")
	# print("WORST")
	for k in wd:
		# if wd[k] > 1:
		# 	# print(k, wd[k])
		if wd[k] > wmaxCount:
			wmaxCount = wd[k]
			wmaxKey = k

	# print("max: ", str(wmaxKey), ", ", str(wmaxCount))
	
	return RedCarpet(("%s, %s" % bmaxKey, bmaxCount), ("%s, %s" % wmaxKey, wmaxCount))

getBestAndWorstDressed()