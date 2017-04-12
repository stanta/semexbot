import requests
import json 
from BeautifulSoup import BeautifulSoup
#from alchemyapi import AlchemyAPI
#AApy = AlchemyAPI()
 
 
sentiments = 'any positive negative neutral'
sentiments = sentiments.split()
 
types = 'free text person city company organization'
types = types.split()
 
api_key = "0e9e197aea00410337343201d4eb7b806f13c1ff"
keyword = "BioMarin Pharmaceutical Inc"
# python alchemyapi.py 0e9e197aea00410337343201d4eb7b806f13c1ff
 
def news_api(text, type, sentiment_type,):
    
    #url="https://access.alchemyapi.com/calls/data/GetNews?apikey="+api_key+"\
#&return=enriched.url.title&start=1431561600&end=1432249200&q.enriched.url.enrichedTitle.entities.entity=|\
#text="+text+",type="+type+"|&q.enriched.url.enrichedTitle.docSentiment.type="+sentiment_type+"&q.enriched.url.enrichedTitle.taxonomy.taxonomy_.label=technology%20and%20computing&count=25&outputMode=json"
   
	import requests 
	r = requests.get('https://gateway-a.watsonplatform.net/calls/data/GetNews?outputMode=json&start=now-30d&end=now&count=5&q.enriched.url.enrichedTitle.keywords.keyword.text='+keyword+'&return=enriched.url.url,enriched.url.title&apikey='+api_key)
	print r.text
	return r

    
from pprint import pprint
pprint(news_api("IBM", types[0], "any"))
