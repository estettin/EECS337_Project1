import tweetsorter
import config
import json
import pandas as pd
from pandas.io.json import json_normalize
import csv

#creating preprocessed dictionaries into json
def createDictionary(year):
	d = tweetsorter.sortTweets(year, config.awardarray)
	with open('dicts/d' + year + '.json', 'w') as fp:
		json.dump(d, fp)

#loading preprocessed dictionaries from json
def loadDictionary(year):
	name = 'dicts/d' + year + '.json'
	return json.load(open(name))
#loading all tweets from csv
def loadData(year):
	return tweetsorter.data

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