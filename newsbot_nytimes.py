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
	api_key = "4ff70db037b3f58edd94f5de82da0725:9:74039383"
	#api_key = 'test'	
    #url="https://access.alchemyapi.com/calls/data/GetNews?apikey="+api_key+"\
#&return=enriched.url.title&start=1431561600&end=1432249200&q.enriched.url.enrichedTitle.entities.entity=|\
#text="+text+",type="+type+"|&q.enriched.url.enrichedTitle.docSentiment.type="+sentiment_type+"&q.enriched.url.enrichedTitle.taxonomy.taxonomy_.label=technology%20and%20computing&count=25&outputMode=json"
	rstr = (requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json?q='+text+'&begin_date='+date1+'&api-key='+api_key+'&fl=abstract,pub_date&end_date='+date2)) # &to-date='+date
	r_dict = json.loads(rstr.text)
	r_arr=r_dict.get('response').get('docs')
	#pprint (r_arr)
	news_arr=[]
	for new in r_arr:
		news_arr.append([new.get('pub_date'),new.get('abstract')])
	pprint (news_arr)
	return news_arr

#keyword = "BioMarin Pharmaceutical Inc"   
keyword = "Intel"
datenews_start = "20150403"
datenews_end = "20150503"
 
 
#from pprint import pprint
req = (news_api(keyword, datenews_start, datenews_end))
