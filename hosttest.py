import json
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from collections import Counter
import re
import helpers
import config

""" Gets the name(s) of the host(s) given a set of tweets """
def getHostBigrams(tweet):
	stops = set(stopwords.words('english'))
	stops.update(["host","hosts","hosting", "rt", "http", "next", "year"])
	stops.update(helpers.awardStopwords())
	if "host" in tweet:
		print(tweet)
		string = ''.join([i if ord(i) < 128 else '' for i in tweet])
		tstring = word_tokenize(string)
		swstring = [word for word in tstring if word.lower() not in stops]
		j = 0
		slen = len(swstring)
		while j < slen: 
			swstring[j] = swstring[j].lower()
			if not swstring[j].isalpha():
				swstring.pop(j)
				slen = slen - 1
				continue
			if "host" in swstring[j].lower():
				swstring.pop(j)
				slen = slen - 1
				continue
			j = j + 1
		if len(swstring) > 1:
			bigrams = list(nltk.bigrams(swstring))
			return bigrams
	return []

def regexHosts(tweet, hosttweets):
	hosts = []
	r1 = re.findall("((?:[A-Z][a-z]+) (?:[A-Z][a-z]+)) (?:and|&amp;) ((?:[A-Z][a-z]+) (?:[A-Z][a-z]+)) host", tweet)
	if r1:
		for r in r1[0]:
			if not r == config.ceremony_name.title():
				hosts.append(r)
				if r in hosttweets:
					hosttweets[r].append(tweet)
				else:
					hosttweets[r] = []
					hosttweets[r].append(tweet)
	else:
		r2 = re.findall("(.*) host", tweet)
		if r2:
	 		r3 = re.findall("((?:[A-Z][a-z]+) (?:[A-Z][a-z]+))", r2[0])
	 		if r3: 
	 			for r in r3:
	 				if not r == config.ceremony_name.title():
	 					if r in hosttweets:
	 						hosttweets[r].append(tweet)
	 					else:
	 						hosttweets[r] = []
	 						hosttweets[r].append(tweet)
	return hosts


def determineHosts(bigramCounter):
	possible_hosts = bigramCounter.most_common(2)
	final_hosts = []
	host_one = possible_hosts[0][0]
	final_hosts.append(host_one)
	if possible_hosts[1][1] > possible_hosts[0][1] * 4/5:
		host_two = possible_hosts[1][0]
		final_hosts.append(host_two)
	return final_hosts
