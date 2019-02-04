from hosttest import *
from redcarpet import *
from populate_db import tweets2013, getTweets
from awards import *
from results import *
from sentiment import *
from pprint import pprint as pp
import pandas as pd
import json
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import spacy

"""
main file where we will call functions to find the 
information requested and use the resulting values to populate
a Results object
"""

def getResults(file_path, year, award_names=[]):
	tweets = getTweets(file_path, "gg" + str(year))
	rc = getBestAndWorstDressed(tweets)
	host = getHost(tweets)
	sentiment = sentinmentOfPeople(host, tweets)
	awards_data = [findTweetsWithAwardName(tweets, award) for award in award_names]
	results = Results(
		host = host,
		awards = awards_data,
		bestDressed = rc.bestDressed,
		worstDressed = rc.worstDressed,
		hostSentiment = sentiment,
		year=year)

	humanPrint(results)

getResults("data/gg2013.json", 2013, [])