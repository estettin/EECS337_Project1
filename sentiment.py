import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

stringlist = []

def findSentiment(tweets):
	sid = SentimentIntensityAnalyzer()
	sum = 0
	for sentence in tweets:
		ss = sid.polarity_scores(sentence)
		sum = ss["compound"] + sum
		#for k in sorted(ss):
			#print('{0}: {1}, '.format(k, ss[k]), end='')
	avgscore = float(sum/len(tweets))
	# print(avgscore)
	#print("Avg score = " + str(avgscore))
	if avgscore > .85:
		return "Very Positive"
	elif avgscore > .25:
		return "Positive"
	elif avgscore < -.5:
		return "Very Negative"
	elif avgscore < -.7:
		return "Negative"
	else:
		return "Neutral"

# x = sentinmentOfPeople(["Tina Fey", "Amy Poehler"], data)


# print(x)
