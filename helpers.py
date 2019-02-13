import tweetsorter
import config
import json
import pandas as pd
from pandas.io.json import json_normalize
import csv
from collections import Counter
import re
from imdb import IMDb
ia = IMDb()

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

def loadResultJson(year, t):
	name = 'results/' + year + "/" + t + '.json'
	return json.load(open(name))

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
	name = "gg" + year + ".json"
	name2 = "csvs/tweets" + year + ".csv"
	file = open(name, 'r')
	data_json = json.loads(file.read())
	tweets2013 = pd.DataFrame(json_normalize(data_json)).get("text").tolist() 
	with open(name2,'w') as resultFile:
		wr = csv.writer(resultFile, quoting=csv.QUOTE_ALL)
		wr.writerow(tweets2013)


def finalizePresenters(d):
	presenters = d.most_common(10)
	final_list = []
	if len(presenters) > 0:
		final_list.append(presenters[0][0])
		j = 1
		while j < len(presenters):
			if presenters[j][1] >= .5 * presenters[0][1]:
				final_list.append(presenters[j][0])
			j = j + 1
	return final_list


def finalizeNominees(c, winner, a):
	atype = a.awardtype
	ndict = Counter()
	for k in c:
		count = c[k]
		if atype == "movie":
			if len(k.split(" ")) < 5:
				notMovies = ["best", "tv", "golden", "globe"]
				good = True
				for nm in notMovies:
					if nm in k.lower():
						good = False
						break
				if good:
					movies = ia.search_movie(k)
					if len(movies) > 0:
						title = movies[0]["title"]
						if not winner == title:
							ndict[title] += count
		else:
			if len(k.split(" ")) < 4:
				good = True
				notPeople = ["best", "tv", "golden", "globe"]
				for np in notPeople:
					if np in k.lower():
						good = False
						break
				if good and not winner == k:
					ndict[k] += count
	#confidence 
	nominees = ndict.most_common(7)
	final_list = []
	if len(nominees) > 0:
		final_list.append(nominees[0][0])
		j = 1
		while j < len(nominees):
			if nominees[j][1] >= .2 * nominees[0][1]:
				final_list.append(nominees[j][0])
			j = j + 1
	return final_list
