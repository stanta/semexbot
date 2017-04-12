#coding: utf-8

 
def text2rel(text):
	from pprint import pprint
	import nltk
	import json
	import string
	import re
	# get training and testing data
	from nltk.corpus import conll2000
	reltokens=[]
	class ChunkParser(nltk.ChunkParserI):
		import nltk

		def __init__(self, train_sents):
			train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
			self.tagger = nltk.TrigramTagger(train_data)
		def parse(self, sentence):
			pos_tags = [pos for (word,pos) in sentence]
			tagged_pos_tags = self.tagger.tag(pos_tags)
			chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
			conlltags = [(word, pos, chunktag) for ((word,pos),chunktag) in zip(sentence, chunktags)]
			return nltk.chunk.conlltags2tree(conlltags)
	
	
	test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
	train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
	# training the chunker, ChunkParser is a class defined in the next slide
	NPChunker = ChunkParser(train_sents)
	
	from nltk.tokenize import word_tokenize
	newschunk = word_tokenize (text)

	newstag= nltk.pos_tag (newschunk)

	news_chunk_tree = NPChunker.parse (newstag)
	#text_tokens = nltk.Text(tokens)

	from nltk.sem import relextract	
	news_chunk_pairs = relextract.tree2semi_rel(news_chunk_tree)

	news_reldicts = relextract.semi_rel2reldict(news_chunk_pairs)
	#2Do https://developers.google.com/apis-explorer/#p/kgsearch/v1/kgsearch.entities.search 
	strrels = str(json.dumps(news_reldicts))
	
	#strrels = strrels.translate(' ', '_/')
	return   list (re.sub('[_/]', ' ', strrels.translate(None, '!@#$"[]{},:'))) #aeiouAEIOU

from pprint import pprint

#newstitle = "Ultimaker Launches Two New 3D Printers At CES Las Vegas 2016 PR Newswire via Yahoo! FinanceJan 05 10:06 AM LAS VEGAS, Jan. 5, 2016 /PRNewswire/ -- Ultimaker, a leading 3D printer manufacturer, launches two new 3D printers at CES Las Vegas 2016. Ultimaker will reveal the new Ultimaker 2+ and Ultimaker 2 Extended+ based on the popular Ultimaker 2 family of 3D printers. Ultimaker will also share its vision and projection of the 3D printing market in 2016. Most popular online courses in India The Indian Express via Yahoo! India News Dec 23 03:41 AM They say there is no end to learning. A lot of Indians, both students and professionals, are fast taking up online courses from prestigious foreign universities to give an extra edge to their career. A US-based advanced online learning platform, Coursera has come up with a survey on the most popular online courses and certificates in India in 2015."
newstitle = " Bayer forms gene editing partnership with CRISPR Therapeutics Reuters via Yahoo! NewsDec 21 07:15 AM Bayer will spend 325 million euros ($353 million) on research into a promising new gene editing technology as part of a joint venture with biotech firm CRISPR Therapeutics. Under the deal, the German drugmaker will pay for the joint ventures research over the next five years, 300 million euros in total. Bayer will buy a minority stake in CRISPR Therapeutics for 35 million euros. ', 'Springboard Raises $1.7M For Its Mentor-Based Approach To Online Learning TechCrunchDec 17 03:57 AM  Springboard, an India-U.S. company formerly known as SlideRule, has raised a $1.7 million seed round to accelerate its concept of learning through mentors and a community. Each mentor provides a weekly catch-up session with their students, and Springboard partners with other MOOCs for courses, and creates its own where it sees gaps in content', 'Intel to Chinese electronics company Xiaomi: Let make a deal Intel is engaging in an intriguing business relationship with Chinese electronics manufacturer Xiaomi — if the latest rumors are to be believed, that is. Apparently, the deal gives Xiaomi a major incentive to use Intel processors as the company begins to expand its interests in the competitive laptop market. Every Core i7 processor that Xiaomi purchases for use in a laptop will be accompanied by..'."
news_reldicts = text2rel(newstitle)
print 'news_reldicts -----------------------------'
pprint ((news_reldicts))
#pprint (serialize(news_reldicts))
#print str (newstitle)