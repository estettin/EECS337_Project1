import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import re
import helpers
def getRedCarpetInfo(tweet, best_dressed_counter, worst_dressed_counter, count):

	br = re.findall("(.*) best dressed", tweet, re.IGNORECASE)
	if br:
		br1 = re.findall("((?:[A-Z][a-z]+) (?:[A-Z][a-z]+))", br[0])
		if br1:
			for n in br1:
				if not helpers.containsCeremonyName(n):
					best_dressed_counter[n] += count

	wr = re.findall("(.*) worst dressed", tweet, re.IGNORECASE)
	if wr:
		wr1 = re.findall("((?:[A-Z][a-z]+) (?:[A-Z][a-z]+))", wr[0])
		if wr1:
			for n in wr1:
				if not helpers.containsCeremonyName(n):
					worst_dressed_counter[n] += count


