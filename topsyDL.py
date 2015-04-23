import time

import requests
import simplejson as json

API_HOST = 'http://api.topsy.com/v2'
API_KEY = 'F7ES7ZBRQL67DA3C44MQAAAAABSEZ3UML5KQAAAAAAAFQGYA'
DEFAULT_PERPAGE = 100

try:
	from local_settings import API_KEY
except:
	pass


def get(handle): 
	params = '&q=from:%s&include_metrics=1' % (handle)
	apikey = '?apikey=' + API_KEY
	url = '%s/content/tweets.json%s%s' % (API_HOST, apikey, params)
	print url
	request = requests.get(url)
	print request

get('barackobama')



