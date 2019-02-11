import csv
import json
import pandas as pd
from pandas.io.json import json_normalize
# from populate_db import tweets2013#, tweets2015

# file = open("data/gg2013.json", 'r')
# data_json = json.loads(file.read())
# tweets2013 = pd.DataFrame(json_normalize(data_json)).get("text").tolist()

file = open("data/gg2015.json", 'r')
data_json = json.loads(file.read())
tweets2015 = pd.DataFrame(json_normalize(data_json)).get("text").tolist()

# with open("tweets2013.csv",'w') as resultFile:
#     wr = csv.writer(resultFile, quoting=csv.QUOTE_ALL)
#     wr.writerow(tweets2013)

with open("tweets2015.csv",'w') as resultFile:
   wr = csv.writer(resultFile, quoting=csv.QUOTE_ALL)
   wr.writerow(tweets2015)

""" 
file = open("data/gg____.json", 'r')
data_json = json.loads(file.read())
tweets2015 = pd.DataFrame(json_normalize(data_json)).get("text").tolist()

with open("csvs/tweets____.csv",'w') as resultFile:
    wr = csv.writer(resultFile, quoting=csv.QUOTE_ALL)
    wr.writerow(tweets____)

"""