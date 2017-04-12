#coding: utf-8

#from BeautifulSoup import BeautifulSoup
#from alchemyapi import AlchemyAPI
#AApy = AlchemyAPI()
 
 
sentiments = 'any positive negative neutral'
sentiments = sentiments.split()
 
types = 'free text person city company organization'
types = types.split()
 


 
def news_api(text, date1, date2):
	from pprint import pprint
	import requests
	import json 
	api_key = "ecc5b96d-4d3e-4510-9d0c-1baed27b2c37"
	#api_key = 'test'	
    #url="https://access.alchemyapi.com/calls/data/GetNews?apikey="+api_key+"\
#&return=enriched.url.title&start=1431561600&end=1432249200&q.enriched.url.enrichedTitle.entities.entity=|\
#text="+text+",type="+type+"|&q.enriched.url.enrichedTitle.docSentiment.type="+sentiment_type+"&q.enriched.url.enrichedTitle.taxonomy.taxonomy_.label=technology%20and%20computing&count=25&outputMode=json"
	r_str=(requests.get('http://content.guardianapis.com/search?q='+text+'&from-date='+date1+'&api-key='+api_key+'&show-fields=trailText&to-date='+date2)) # &to-date='+date
	r_dict = json.loads(r_str.text)
	r_arr=r_dict.get('response').get('results')
	
	news_arr=[]
	for new in r_arr:
		news_arr.append([new.get('webPublicationDate'),new.get('fields').get('trailText')])
	pprint (news_arr)
	return news_arr

#keyword = "BioMarin Pharmaceutical Inc"   
keyword = "Intel"
datenews = "2015-04-03"
keyword = "Intel"
datenews_start = "2015-04-03"
datenews_end = "2015-05-03"
 
 
 
#from pprint import pprint
req = (news_api(keyword, datenews_start, datenews_end))
