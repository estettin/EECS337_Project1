import json
from pprint import pprint as pp

import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
# from nltk.tokenize import TweetTokenizer
import pymongo

"""
[{
	u'id': 554402424728072192, 
	u'text': u'just had to scramble to find a golden globes stream for my brother. :D', 
	u'user': {u'id': 19904553, u'screen_name': u'baumbaTz'}, 
	u'timestamp_ms': u'1421014813011'},
	{"text": "What?!? https://t.co/NSPtGtbCvO", "id_str": "950142397194821632"},
 ...
]"""

# with open('data/gg2013.json') as f:
# 	gg2013 = json.load(f)

#connection = pymongo.MongoClient("mongodb://admin:admin@337-1-shard-00-00-tcqfq.mongodb.net:27017,337-1-shard-00-01-tcqfq.mongodb.net:27017,337-1-shard-00-02-tcqfq.mongodb.net:27017/test?ssl=true&ssl_cert_reqs=CERT_NONE&replicaSet=337-1-shard-0&authSource=admin")
#db = connection["gg_data"]
#col = db.gg2013

# print(db.gg2013)
page = open('data/gg2013.json', 'r')
gg2013 = json.loads(page.read())

# print("\n\n", str(col))
df_2013 = pd.DataFrame(json_normalize(gg2013)).get("text").tolist()
	#tolist()
# for item in df:
# 	col.insert(item)
# print parsed[:10]



# pp(df_2013[0:10])
