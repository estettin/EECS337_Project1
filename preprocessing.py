import helpers
import re
from collections import Counter
import json

def preprocess(year):
	data = helpers.loadTweets(year)
	tweets = Counter()
	for t in data:
		r = re.findall("RT(?:.*): (.*)", t)
		if r:
			tweets[r[0]] += 1
		else:
			tweets[t] += 1

	# print (tweets.most_common(100))
	# print(len(tweets))

	with open('countDicts/d' + year + '.json', 'w') as fp:
			json.dump(tweets, fp)
	

preprocess("2013")
preprocess("2015")