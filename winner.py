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

data = tweets2013
d = tweetsorter.d

def findWinner(a, tweets):
	for t in tweets:
		x = re.findall("(Congrats|Congratulations) to(.*)(on|for) Winning",t, re.IGNORECASE)
		if x:
			print(x)
		y = re.findall("(.*)wins best",t, re.IGNORECASE)
		if y:
			print(y)

a = config.awardarray[0]
findWinner(a,d[a.name])
		

# for award in config.awardarray:
# 	findWinner(award, d[award.name])