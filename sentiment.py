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

with open('gg2013.json') as f:
	data = json.load(f)

stringlist = []

stops = set(stopwords.words('english'))
stops.update([u"host",u"hosts",u"hosting",u"goldenglobes", u"golden", u"globes", u"rt", u"http"])

for i in range(0,len(data)):
	if "Tina Fay" in data[i]["text"].encode("UTF-8") or "Amy Poehler" in data[i]["text"].encode("UTF-8") or "tina fay" in data[i]["text"].encode("UTF-8") or "amy poehler" in data[i]["text"].encode("UTF-8"):
		string = ''.join([i if ord(i) < 128 else '' for i in data[i]["text"].encode("UTF-8")])
		j = 0
		tstring = word_tokenize(string)
		slen = len(tstring)
		while j < slen:
			if not tstring[j].isalpha():
				tstring.pop(j)
				slen = slen - 1
				continue
			if tstring[j].lower() == "rt" or tstring[j].lower() == "http" or tstring[j].lower() == "goldenglobes":
				tstring.pop(j)
				slen = slen - 1
				continue
			j = j + 1
		stringlist.append(' '.join(tstring))



sid = SentimentIntensityAnalyzer()
sum = 0
for sentence in stringlist:
	ss = sid.polarity_scores(sentence)
	sum = ss["compound"] + sum
	#for k in sorted(ss):
		#print('{0}: {1}, '.format(k, ss[k]), end='')
avgscore = sum/len(stringlist)
print "Avg score = " + str(avgscore)
if avgscore > .5 :
	print "Very Positive"
elif avgscore > .25:
	print "Positive"
elif avgscore < -.5:
	print "Very Negative"
elif avgscore < -.25:
	print "Negative"
else:
	print "Neutral"


	

