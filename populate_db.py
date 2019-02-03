import json
from pprint import pprint as pp
import pandas as pd
from pandas.io.json import json_normalize
import pymongo

def populate_db(file_path, collection_name, db):
	file = open(file_path, 'r')
	data_json = json.loads(file.read())
	df = pd.DataFrame(json_normalize(data_json)).drop_duplicates().to_dict('records')
	data = [{'_id' : item['id'], 'text' : item['text']} for item in df]

	print("db insertion")
	db[collection_name].insert_many(data)

def connect_to_client():
	client = pymongo.MongoClient('mongodb://admin:admin@337-1-shard-00-00-tcqfq.mongodb.net:27017,337-1-shard-00-01-tcqfq.mongodb.net:27017,337-1-shard-00-02-tcqfq.mongodb.net:27017/test?ssl=true&ssl_cert_reqs=CERT_NONE&replicaSet=337-1-shard-0&authSource=admin')
	db = client.GoldenGlobes
	serverStatusResult= db.command("serverStatus")
	pp(serverStatusResult)
	return db

def get_tweets(file_path, collection_name):
	db = connect_to_client()
	if collection_name not in db.list_collection_names():
		populate_db(file_path, collection_name, db)
	print("DB populated")
	text_list = [item["text"] for item in list(db[collection_name].find({}, {"_id":0, "text":1}))]
	return text_list


# count 174643
tweets2013 = get_tweets('data/gg2013.json', 'gg2013')
# count 1754153
tweets2015 = get_tweets('data/gg2015.json', 'gg2015')
