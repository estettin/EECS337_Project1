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
	for t in tweets:
		# x = re.findall("(Congrats|Congratulations) to(.*)(on|for) Winning",t, re.IGNORECASE)
		# if x:
		# 	print(x)
		#get rid of cast and crew and words with 2 capitals
		y = re.findall("(\".*\") wins best",t, re.IGNORECASE)
		if y:
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
			print("HERE!")
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

	print(a.name, dict1)
	print(a.name, dict2)
	print(a.name, wdict)

			#First word check and check year

# get rid of punctuation
# get rid of stop words





a = config.awardarray[:10]


for award in a:
	findWinner(award,d[award.name])
		






# for award in config.awardarray:
# 	findWinner(award, d[award.name])