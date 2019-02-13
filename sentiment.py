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

stops = set(stopwords.words('english'))
stops.update(["host","hosts","hosting","goldenglobes", "golden", "globes", "rt", "http"])

# def sentinmentOfPeople(people, data):
# 	# capital or non capital 
# 	for i in range(0,len(data)):
# 		found = False
# 		if people[0] in data[i] or people[0].lower() in data[i]:
# 			string = ''.join([i if ord(i) < 128 else '' for i in data[i]])
# 			found = True
# 		elif len(people) > 1 and (people[1] in data[i] or people[1].lower() in data[i]):
# 			string = ''.join([i if ord(i) < 128 else '' for i in data[i]])
# 			found = True
# 		if found:
# 			j = 0
# 			tstring = word_tokenize(string)
# 			slen = len(tstring)
# 			while j < slen:
# 				if not tstring[j].isalpha():
# 					tstring.pop(j)
# 					slen = slen - 1
# 					continue
# 				if tstring[j].lower() == "rt" or tstring[j].lower() == "http" or tstring[j].lower() == "goldenglobes":
# 					tstring.pop(j)
# 					slen = slen - 1
# 					continue
# 				j = j + 1
# 			stringlist.append(' '.join(tstring))


def findSentiment(tweets):
	sid = SentimentIntensityAnalyzer()
	sum = 0
	for sentence in tweets:
		ss = sid.polarity_scores(sentence)
		sum = ss["compound"] + sum
		#for k in sorted(ss):
			#print('{0}: {1}, '.format(k, ss[k]), end='')
	avgscore = sum/len(tweets)
	#print("Avg score = " + str(avgscore))
	if avgscore > .5 :
		return "Very Positive"
	elif avgscore > .25:
		return "Positive"
	elif avgscore < -.5:
		return "Very Negative"
	elif avgscore < -.25:
		return "Negative"
	else:
		return "Neutral"

# x = sentinmentOfPeople(["Tina Fey", "Amy Poehler"], data)


# print(x)
