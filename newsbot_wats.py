import requests
import json 
#from BeautifulSoup import BeautifulSoup
from pprint import pprint
#from alchemyapi import AlchemyAPI
#AApy = AlchemyAPI()
 
 
sentiments = 'any positive negative neutral'
sentiments = sentiments.split()
 
types = 'free text person city company organization'
types = types.split()
 
api_key = "0e9e197aea00410337343201d4eb7b806f13c1ff"
keyword = "BioMarin Pharmaceutical Inc"
# python alchemyapi.py 0e9e197aea00410337343201d4eb7b806f13c1ff
def news_api(text, date1, date2):
    
    #url="https://access.alchemyapi.com/calls/data/GetNews?apikey="+api_key+"\
#&return=enriched.url.title&start=1431561600&end=1432249200&q.enriched.url.enrichedTitle.entities.entity=|\
#text="+text+",type="+type+"|&q.enriched.url.enrichedTitle.docSentiment.type="+sentiment_type+"&fields&count=25&outputMode=json"
   
	r_str = requests.get('https://gateway-a.watsonplatform.net/calls/data/GetNews?outputMode=json&start=now-30d&end=now&count=5&q.enriched.url.enrichedTitle.keywords.keyword.text='+text+'&return=,enriched.url.publicationDate.date,enriched.url.text,enriched.url.entities,enriched.url.relations,&apikey='+api_key)
	#pprint (r_str)
	r_dict = json.loads(r_str.text)
	#pprint (r_dict)
	if r_dict <> "" :
		r_arr=r_dict.get('result').get('docs')
		#pprint (r_arr)
		news_arr=[]
		for new in r_arr:
			news_arr.append([new.get('source').get('enriched').get('url').get('publicationDate'),new.get('source').get('enriched').get('url').get('text')]) #u'source': {u'enriched': {u'url':  u'source': {u'enriched': {u'url': {u'publicationDate':
		pprint (news_arr)
		return news_arr

#keyword = "BioMarin Pharmaceutical Inc"   
keyword = "Intel"
datenews_start = "20150403"
datenews_end = "20150503"
 
 
#from pprint import pprint
req = (news_api(keyword, datenews_start, datenews_end))

fields = "enriched.url.entities.entity.text,enriched.url.entities.entity.type,enriched.url.entities.entity.knowledgeGraph.typeHierarchy,enriched.url.entities.entity.count,enriched.url.entities.entity.relevance,enriched.url.entities.entity.sentiment.type,enriched.url.entities.entity.sentiment.score,enriched.url.entities.entity.sentiment.mixed,enriched.url.entities.entity.disambiguated.name,enriched.url.entities.entity.disambiguated.geo,enriched.url.entities.entity.disambiguated.dbpedia,enriched.url.entities.entity.disambiguated.website,enriched.url.entities.entity.disambiguated.subType,enriched.url.entities.entity.disambiguated.subType.subType_,enriched.url.entities.entity.quotations,enriched.url.entities.entity.quotations.quotation_.quotation,enriched.url.entities.entity.quotations.quotation_.sentiment.type,enriched.url.entities.entity.quotations.quotation_.sentiment.score,enriched.url.entities.entity.quotations.quotation_.sentiment.mixed,enriched.url.concepts,enriched.url.concepts.concept.text,enriched.url.concepts.concept.relevance,enriched.url.concepts.concept.knowledgeGraph.typeHierarchy,enriched.url.relations,enriched.url.relations.relation.sentence,enriched.url.relations.relation.subject.text,enriched.url.relations.relation.subject.entities,enriched.url.relations.relation.subject.entities.entity.text,enriched.url.relations.relation.subject.entities.entity.type,enriched.url.relations.relation.subject.entities.entity.knowledgeGraph.typeHierarchy,enriched.url.relations.relation.subject.entities.entity.count,enriched.url.relations.relation.subject.entities.entity.relevance,enriched.url.relations.relation.subject.entities.entity.sentiment.type,enriched.url.relations.relation.subject.entities.entity.sentiment.score,enriched.url.relations.relation.subject.entities.entity.sentiment.mixed,enriched.url.relations.relation.subject.entities.entity.disambiguated.name,enriched.url.relations.relation.subject.entities.entity.disambiguated.geo,enriched.url.relations.relation.subject.entities.entity.disambiguated.dbpedia,enriched.url.relations.relation.subject.entities.entity.disambiguated.website,enriched.url.relations.relation.subject.entities.entity.disambiguated.subType,enriched.url.relations.relation.subject.entities.entity.disambiguated.subType.subType_,enriched.url.relations.relation.subject.entities.entity.quotations,enriched.url.relations.relation.subject.entities.entity.quotations.quotation_.quotation,enriched.url.relations.relation.subject.entities.entity.quotations.quotation_.sentiment.type,enriched.url.relations.relation.subject.entities.entity.quotations.quotation_.sentiment.score,enriched.url.relations.relation.subject.entities.entity.quotations.quotation_.sentiment.mixed,enriched.url.relations.relation.subject.keywords,enriched.url.relations.relation.subject.keywords.keyword.text,enriched.url.relations.relation.subject.keywords.keyword.relevance,enriched.url.relations.relation.subject.keywords.keyword.sentiment.type,enriched.url.relations.relation.subject.keywords.keyword.sentiment.score,enriched.url.relations.relation.subject.keywords.keyword.sentiment.mixed,enriched.url.relations.relation.subject.keywords.keyword.knowledgeGraph.typeHierarchy,enriched.url.relations.relation.subject.sentiment.type,enriched.url.relations.relation.subject.sentiment.score,enriched.url.relations.relation.subject.sentiment.mixed,enriched.url.relations.relation.action.text,enriched.url.relations.relation.action.lemmatized,enriched.url.relations.relation.action.verb.text,enriched.url.relations.relation.action.verb.tense,enriched.url.relations.relation.action.verb.negated,enriched.url.relations.relation.object.text,enriched.url.relations.relation.object.entities,enriched.url.relations.relation.object.entities.entity.text,enriched.url.relations.relation.object.entities.entity.type,enriched.url.relations.relation.object.entities.entity.knowledgeGraph.typeHierarchy,enriched.url.relations.relation.object.entities.entity.count,enriched.url.relations.relation.object.entities.entity.relevance,enriched.url.relations.relation.object.entities.entity.sentiment.type,enriched.url.relations.relation.object.entities.entity.sentiment.score,enriched.url.relations.relation.object.entities.entity.sentiment.mixed,enriched.url.relations.relation.object.entities.entity.disambiguated.name,enriched.url.relations.relation.object.entities.entity.disambiguated.geo,enriched.url.relations.relation.object.entities.entity.disambiguated.dbpedia,enriched.url.relations.relation.object.entities.entity.disambiguated.website,enriched.url.relations.relation.object.entities.entity.disambiguated.subType,enriched.url.relations.relation.object.entities.entity.disambiguated.subType.subType_,enriched.url.relations.relation.object.entities.entity.quotations,enriched.url.relations.relation.object.entities.entity.quotations.quotation_.quotation,enriched.url.relations.relation.object.entities.entity.quotations.quotation_.sentiment.type,enriched.url.relations.relation.object.entities.entity.quotations.quotation_.sentiment.score,enriched.url.relations.relation.object.entities.entity.quotations.quotation_.sentiment.mixed,enriched.url.relations.relation.object.keywords,enriched.url.relations.relation.object.keywords.keyword.text,enriched.url.relations.relation.object.keywords.keyword.relevance,enriched.url.relations.relation.object.keywords.keyword.sentiment.type,enriched.url.relations.relation.object.keywords.keyword.sentiment.score,enriched.url.relations.relation.object.keywords.keyword.sentiment.mixed,enriched.url.relations.relation.object.keywords.keyword.knowledgeGraph.typeHierarchy,enriched.url.relations.relation.object.sentiment.type,enriched.url.relations.relation.object.sentiment.score,enriched.url.relations.relation.object.sentiment.mixed,enriched.url.relations.relation.object.sentimentFromSubject.type,enriched.url.relations.relation.object.sentimentFromSubject.score,enriched.url.relations.relation.object.sentimentFromSubject.mixed,enriched.url.relations.relation.location.text,enriched.url.relations.relation.location.sentiment.type,enriched.url.relations.relation.location.sentiment.score,enriched.url.relations.relation.location.sentiment.mixed,enriched.url.relations.relation.location.entities,enriched.url.relations.relation.location.entities.entity.text,enriched.url.relations.relation.location.entities.entity.type,enriched.url.relations.relation.location.entities.entity.knowledgeGraph.typeHierarchy,enriched.url.relations.relation.location.entities.entity.count,enriched.url.relations.relation.location.entities.entity.relevance,enriched.url.relations.relation.location.entities.entity.sentiment.type,enriched.url.relations.relation.location.entities.entity.sentiment.score,enriched.url.relations.relation.location.entities.entity.sentiment.mixed,enriched.url.relations.relation.location.entities.entity.disambiguated.name,enriched.url.relations.relation.location.entities.entity.disambiguated.geo,enriched.url.relations.relation.location.entities.entity.disambiguated.dbpedia,enriched.url.relations.relation.location.entities.entity.disambiguated.website,enriched.url.relations.relation.location.entities.entity.disambiguated.subType,enriched.url.relations.relation.location.entities.entity.disambiguated.subType.subType_,enriched.url.relations.relation.location.entities.entity.quotations,enriched.url.relations.relation.location.entities.entity.quotations.quotation_.quotation,enriched.url.relations.relation.location.entities.entity.quotations.quotation_.sentiment.type,enriched.url.relations.relation.location.entities.entity.quotations.quotation_.sentiment.score,enriched.url.relations.relation.location.entities.entity.quotations.quotation_.sentiment.mixed,enriched.url.relations.relation.location.keywords,enriched.url.relations.relation.location.keywords.keyword.text,enriched.url.relations.relation.location.keywords.keyword.relevance,enriched.url.relations.relation.location.keywords.keyword.sentiment.type,enriched.url.relations.relation.location.keywords.keyword.sentiment.score,enriched.url.relations.relation.location.keywords.keyword.sentiment.mixed,enriched.url.relations.relation.location.keywords.keyword.knowledgeGraph.typeHierarchy,enriched.url.relations.relation.temporal.text,enriched.url.relations.relation.temporal.decoded.type,enriched.url.relations.relation.temporal.decoded.value,enriched.url.relations.relation.temporal.decoded.start,enriched.url.relations.relation.temporal.decoded.end,enriched.url.docSentiment.type,enriched.url.docSentiment.score,enriched.url.docSentiment.mixed,enriched.url.taxonomy,enriched.url.taxonomy.taxonomy_.label,enriched.url.taxonomy.taxonomy_.score,enriched.url.taxonomy.taxonomy_.confident,enriched.url.enrichedTitle.keywords,enriched.url.enrichedTitle.keywords.keyword.text,enriched.url.enrichedTitle.keywords.keyword.relevance,enriched.url.enrichedTitle.keywords.keyword.sentiment.type,enriched.url.enrichedTitle.keywords.keyword.sentiment.score,enriched.url.enrichedTitle.keywords.keyword.sentiment.mixed,enriched.url.enrichedTitle.keywords.keyword.knowledgeGraph.typeHierarchy,enriched.url.enrichedTitle.entities,enriched.url.enrichedTitle.entities.entity.text,enriched.url.enrichedTitle.entities.entity.type,enriched.url.enrichedTitle.entities.entity.knowledgeGraph.typeHierarchy,enriched.url.enrichedTitle.entities.entity.count,enriched.url.enrichedTitle.entities.entity.relevance,enriched.url.enrichedTitle.entities.entity.sentiment.type,enriched.url.enrichedTitle.entities.entity.sentiment.score,enriched.url.enrichedTitle.entities.entity.sentiment.mixed,enriched.url.enrichedTitle.entities.entity.disambiguated.name,enriched.url.enrichedTitle.entities.entity.disambiguated.geo,enriched.url.enrichedTitle.entities.entity.disambiguated.dbpedia,enriched.url.enrichedTitle.entities.entity.disambiguated.website,enriched.url.enrichedTitle.entities.entity.disambiguated.subType,enriched.url.enrichedTitle.entities.entity.disambiguated.subType.subType_,enriched.url.enrichedTitle.entities.entity.quotations,enriched.url.enrichedTitle.entities.entity.quotations.quotation_.quotation,enriched.url.enrichedTitle.entities.entity.quotations.quotation_.sentiment.type,enriched.url.enrichedTitle.entities.entity.quotations.quotation_.sentiment.score,enriched.url.enrichedTitle.entities.entity.quotations.quotation_.sentiment.mixed,enriched.url.enrichedTitle.concepts,enriched.url.enrichedTitle.concepts.concept.text,enriched.url.enrichedTitle.concepts.concept.relevance,,enriched.url.enrichedTitle.concepts.concept.knowledgeGraph.typeHierarchy,enriched.url.enrichedTitle.relations,enriched.url.enrichedTitle.relations.relation.sentence,enriched.url.enrichedTitle.relations.relation.subject.text,enriched.url.enrichedTitle.relations.relation.subject.entities,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.text,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.type,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.knowledgeGraph.typeHierarchy,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.count,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.relevance,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.sentiment.type,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.sentiment.score,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.disambiguated.name,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.disambiguated.geo,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.disambiguated.dbpedia,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.disambiguated.website,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.disambiguated.subType,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.disambiguated.subType.subType_,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.quotations,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.quotations.quotation_.quotation,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.quotations.quotation_.sentiment.type,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.quotations.quotation_.sentiment.score,enriched.url.enrichedTitle.relations.relation.subject.entities.entity.quotations.quotation_.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.subject.keywords,enriched.url.enrichedTitle.relations.relation.subject.keywords.keyword.text,enriched.url.enrichedTitle.relations.relation.subject.keywords.keyword.relevance,enriched.url.enrichedTitle.relations.relation.subject.keywords.keyword.sentiment.type,enriched.url.enrichedTitle.relations.relation.subject.keywords.keyword.sentiment.score,enriched.url.enrichedTitle.relations.relation.subject.keywords.keyword.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.subject.keywords.keyword.knowledgeGraph.typeHierarchy,enriched.url.enrichedTitle.relations.relation.subject.sentiment.type,enriched.url.enrichedTitle.relations.relation.subject.sentiment.score,enriched.url.enrichedTitle.relations.relation.subject.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.action.text,enriched.url.enrichedTitle.relations.relation.action.lemmatized,enriched.url.enrichedTitle.relations.relation.action.verb.text,enriched.url.enrichedTitle.relations.relation.action.verb.tense,enriched.url.enrichedTitle.relations.relation.action.verb.negated,enriched.url.enrichedTitle.relations.relation.object.text,enriched.url.enrichedTitle.relations.relation.object.entities,enriched.url.enrichedTitle.relations.relation.object.entities.entity.text,enriched.url.enrichedTitle.relations.relation.object.entities.entity.type,enriched.url.enrichedTitle.relations.relation.object.entities.entity.knowledgeGraph.typeHierarchy,enriched.url.enrichedTitle.relations.relation.object.entities.entity.count,enriched.url.enrichedTitle.relations.relation.object.entities.entity.relevance,enriched.url.enrichedTitle.relations.relation.object.entities.entity.sentiment.type,enriched.url.enrichedTitle.relations.relation.object.entities.entity.sentiment.score,enriched.url.enrichedTitle.relations.relation.object.entities.entity.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.object.entities.entity.disambiguated.name,enriched.url.enrichedTitle.relations.relation.object.entities.entity.disambiguated.geo,enriched.url.enrichedTitle.relations.relation.object.entities.entity.disambiguated.dbpedia,enriched.url.enrichedTitle.relations.relation.object.entities.entity.disambiguated.website,enriched.url.enrichedTitle.relations.relation.object.entities.entity.disambiguated.subType,enriched.url.enrichedTitle.relations.relation.object.entities.entity.disambiguated.subType.subType_,enriched.url.enrichedTitle.relations.relation.object.entities.entity.quotations,enriched.url.enrichedTitle.relations.relation.object.entities.entity.quotations.quotation_.quotation,enriched.url.enrichedTitle.relations.relation.object.entities.entity.quotations.quotation_.sentiment.type,enriched.url.enrichedTitle.relations.relation.object.entities.entity.quotations.quotation_.sentiment.score,enriched.url.enrichedTitle.relations.relation.object.entities.entity.quotations.quotation_.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.object.keywords,enriched.url.enrichedTitle.relations.relation.object.keywords.keyword.text,enriched.url.enrichedTitle.relations.relation.object.keywords.keyword.relevance,enriched.url.enrichedTitle.relations.relation.object.keywords.keyword.sentiment.type,enriched.url.enrichedTitle.relations.relation.object.keywords.keyword.sentiment.score,enriched.url.enrichedTitle.relations.relation.object.keywords.keyword.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.object.keywords.keyword.knowledgeGraph.typeHierarchy,enriched.url.enrichedTitle.relations.relation.object.sentiment.type,enriched.url.enrichedTitle.relations.relation.object.sentiment.score,enriched.url.enrichedTitle.relations.relation.object.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.object.sentimentFromSubject.type,enriched.url.enrichedTitle.relations.relation.object.sentimentFromSubject.score,enriched.url.enrichedTitle.relations.relation.object.sentimentFromSubject.mixed,enriched.url.enrichedTitle.relations.relation.location.text,enriched.url.enrichedTitle.relations.relation.location.sentiment.type,enriched.url.enrichedTitle.relations.relation.location.sentiment.score,enriched.url.enrichedTitle.relations.relation.location.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.location.entities,enriched.url.enrichedTitle.relations.relation.location.entities.entity.text,enriched.url.enrichedTitle.relations.relation.location.entities.entity.type,enriched.url.enrichedTitle.relations.relation.location.entities.entity.knowledgeGraph.typeHierarchy,enriched.url.enrichedTitle.relations.relation.location.entities.entity.count,enriched.url.enrichedTitle.relations.relation.location.entities.entity.relevance,enriched.url.enrichedTitle.relations.relation.location.entities.entity.sentiment.type,enriched.url.enrichedTitle.relations.relation.location.entities.entity.sentiment.score,enriched.url.enrichedTitle.relations.relation.location.entities.entity.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.location.entities.entity.disambiguated.name,enriched.url.enrichedTitle.relations.relation.location.entities.entity.disambiguated.geo,enriched.url.enrichedTitle.relations.relation.location.entities.entity.disambiguated.dbpedia,enriched.url.enrichedTitle.relations.relation.location.entities.entity.disambiguated.website,enriched.url.enrichedTitle.relations.relation.location.entities.entity.disambiguated.subType,enriched.url.enrichedTitle.relations.relation.location.entities.entity.disambiguated.subType.subType_,enriched.url.enrichedTitle.relations.relation.location.entities.entity.quotations,enriched.url.enrichedTitle.relations.relation.location.entities.entity.quotations.quotation_.quotation,enriched.url.enrichedTitle.relations.relation.location.entities.entity.quotations.quotation_.sentiment.type,enriched.url.enrichedTitle.relations.relation.location.entities.entity.quotations.quotation_.sentiment.score,enriched.url.enrichedTitle.relations.relation.location.entities.entity.quotations.quotation_.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.location.keywords,enriched.url.enrichedTitle.relations.relation.location.keywords.keyword.text,enriched.url.enrichedTitle.relations.relation.location.keywords.keyword.relevance,enriched.url.enrichedTitle.relations.relation.location.keywords.keyword.sentiment.type,enriched.url.enrichedTitle.relations.relation.location.keywords.keyword.sentiment.score,enriched.url.enrichedTitle.relations.relation.location.keywords.keyword.sentiment.mixed,enriched.url.enrichedTitle.relations.relation.location.keywords.keyword.knowledgeGraph.typeHierarchy,enriched.url.enrichedTitle.relations.relation.temporal.text,enriched.url.enrichedTitle.relations.relation.temporal.decoded.type,enriched.url.enrichedTitle.relations.relation.temporal.decoded.value,enriched.url.enrichedTitle.relations.relation.temporal.decoded.start,enriched.url.enrichedTitle.relations.relation.temporal.decoded.end"  
