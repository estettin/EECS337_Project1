import tweetsorter
import config
import json
import pandas as pd
from pandas.io.json import json_normalize
import csv
from collections import Counter
import re

#creating preprocessed dictionaries into json
# def createDictionary(year):
# 	d = tweetsorter.sortTweets(year, config.awardarray)
# 	with open('dicts/d' + year + '.json', 'w') as fp:
# 		json.dump(d, fp)

def removeRetweets(year):
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


#loading preprocessed dictionaries from json
def loadTweetsFromJson(year):
	name = 'countDicts/d' + year + '.json'
	return json.load(open(name))

def loadTweets(year):
	# print("year: ", year)
	name = 'csvs/tweets' + year + '.csv'
	# print("name: ", name)
	with open(name, 'r') as f:
		reader = csv.reader(f)
		data = list(reader)
	data=data[0]
	return data

#create csv files with all the tweets
def createCSV(year):
	name = "data/gg" + year + ".json"
	name2 = "csvs/tweets" + year + ".csv"
	file = open(name, 'r')
	data_json = json.loads(file.read())
	tweets2013 = pd.DataFrame(json_normalize(data_json)).get("text").tolist() 
	with open(name2,'w') as resultFile:
		wr = csv.writer(resultFile, quoting=csv.QUOTE_ALL)
		wr.writerow(tweets2013)

