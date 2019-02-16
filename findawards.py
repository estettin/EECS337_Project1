import json
import nltk
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.chunk import tree2conlltags
import re
import csv
import copy


#Parameters to the Main function:

#GLOBAL VARIABLES FOR OUR FUNCTION:
punc = [".",":","!","?","#",",","<", "@"]
rt_words = ["wins", "goes", "to", "dressed", "winner", "winners", "at", "is", "are", "for", "win", "from", "went", "won"]
rhs_nest = [[w.lower(), w.upper(), w.title()] for w in rt_words]
rhs = [item for sublist in rhs_nest for item in sublist]

def PopulatePhrasesforAwards(tweet,count, phrases):
		match = re.search(r"best\s|Best\s|BEST\s", tweet)
		if match == None:
			return
		tweet_arr = re.findall(r"[\w']+|[.:,!?\#-]", tweet[match.start():])
		tweet_arr = list(filter(None, tweet_arr))
		end = 0
		found_hyph = False
		for i in range(1,len(tweet_arr)):
			if tweet_arr[i] == "-" and not found_hyph:
				found_hyph = True
			elif tweet_arr[i] in punc or (tweet_arr[i] in rhs) or (found_hyph and tweet_arr[i] == "-"):
				end = i
				if end <= 1:
					break
				p = " ".join(tweet_arr[0:end])
				if p[end-3:end] == " - ":
					p = p[:end - 3]
				if p in phrases.keys():
					phrases[p] += count
				else:
					phrases[p] = count
				break

def PostProcessFindAwards(phrases):
	s = [{k: phrases[k]} for k in sorted(phrases, key=phrases.get, reverse=True)]
	thresh = [v for k,v in s[int((len(s)/6))].items()][0]
	sorted_phrases = {k: v for k, v in phrases.items() if v > thresh}
	s_reduced = {}

	for key, val in sorted_phrases.items():
		if " - " in key:
			r = key[key.index("-") + 1:].strip()
			l = key[:key.index("-")].strip()

			tok_arr = nltk.word_tokenize(r)
			tagged = nltk.pos_tag(tok_arr)
			tree = nltk.chunk.ne_chunk(tagged)
			iob_tagged = tree2conlltags(tree)
			if iob_tagged != [] and 'PERSON' in iob_tagged[0][2]:
				key = l
				continue	
								
		key = key.lower()
		if "-" in key:
			key = key.replace(" - ", " ")
		if key in s_reduced.keys():
			s_reduced[key] += val
		else:
			s_reduced[key] =  val

	dup = copy.deepcopy(s_reduced)
	for k,v in dup.items():
		for phrase in dup.keys():
			if k in phrase and k != phrase:
				del s_reduced[k]
				break

	final_list = [{k: s_reduced[k]} for k in sorted(s_reduced, key=s_reduced.get, reverse=True)]
	maxcount = [v for v in final_list[0].values()][0]
	awardslist = []
	for a in final_list:
		if [v for v in a.values()][0] >= .14*maxcount:
			awardslist.append(a)
	awardslist = [[v for v in d.keys()][0] for d in awardslist]
	return awardslist



