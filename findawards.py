import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re
from tweet_parser import df_2013
import spacy

tweets = df_2013

def FindAwards(data):
	"""
	takes in the tweets as an an array of string and identies award names
	"""
	
