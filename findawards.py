import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from tweet_parser import df_2013
import spacy

tweets = df_2013
punc = [".",":","-","!","?"]
"""
Phrases to look for:
wins _______ for
the award for
wins
"""

def FindAwards(data):
	"""
	takes in the tweets as an an array of string and identies award names
	"""
	phrases = {}
	nlp = spacy.load("en_core_web_sm")
	for tweet in tweets:
		if "best" or "Best" in tweet:
			






