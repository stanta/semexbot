#coding: utf-8

def text2frame(text, recurse_level):
	from pprint import pprint
	#from string import lowercase
	from nltk.corpus import framenet as fn
	from nltk.corpus import wordnet as wn
	from nltk.tokenize import wordpunct_tokenize
	frametokens = []
	newschunk = wordpunct_tokenize (text)
	for ns in newschunk:
	
				synonyms = wn.synsets(ns)
				print '---------'
				print ns
				print synonyms
				for syns in synonyms:
					offset = str(syns.offset()).zfill(8)+"-"+str(syns.pos())
					print offset 
					syns_lemmas = syns.lemmas()
					#syn_def = syns.name()
					#syn_def=str(syns)
					#print (syns_lemmas)
					for lemmas in syns_lemmas:
						syn_def = lemmas.name()
						print (syn_def)
						
						
						#print recurse_level
					#	if recurse_level  < 4:
					#		frametokens.extend( text2frame (str(syn_def), recurse_level) )# or .append?
					# may be save new frames?
					# ConsecutiveNPChunkTagger 
					#or NN to f..king classificate 
	#recurse_level-=1
	return frametokens
# pprint(fn.frames(r'(?i)medical'))
newstitle = "Intel to Chinese electronics company Xiaomi: Let’s make a deal Intel is engaging in an intriguing business relationship with Chinese electronics manufacturer Xiaomi — if the latest rumors are to be believed, that is. Apparently, the deal gives Xiaomi a major incentive to use Intel processors as the company begins to expand its interests in the competitive laptop market. Every Core i7 processor that Xiaomi purchases for use in a laptop will be accompanied by..."
frametokens = text2frame(newstitle,1)
print(frametokens)