import json
from pprint import pprint as pp

import pandas as pd
from pandas.io.json import json_normalize
from nltk.tokenize import TweetTokenizer

"""
[{
	u'id': 554402424728072192, 
	u'text': u'just had to scramble to find a golden globes stream for my brother. :D', 
	u'user': {u'id': 19904553, u'screen_name': u'baumbaTz'}, 
	u'timestamp_ms': u'1421014813011'},
	{"text": "What?!? https://t.co/NSPtGtbCvO", "id_str": "950142397194821632"},
 ...
]"""

with open('data/gg2013.json') as f:
	gg2013 = json.load(f)

# pd.read_json(gg2013, orient=)

df = pd.DataFrame(json_normalize(gg2013))

pp(df.head(20))
