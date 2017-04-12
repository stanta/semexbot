#coding: utf-8

import sklearn
from sklearn.datasets import fetch_20newsgroups
categories = [
'alt.atheism', 
'comp.graphics', 
'comp.os.ms-windows.misc',
'comp.sys.ibm.pc.hardware',
'comp.sys.mac.hardware',
'comp.windows.x',
'misc.forsale',
'rec.autos',
'rec.motorcycles',
'rec.sport.baseball',
'rec.sport.hockey',
'sci.crypt',
'sci.electronics',
'sci.med',
'sci.space',
'soc.religion.christian',
'talk.politics.guns',
'talk.politics.mideast',
'talk.politics.misc',
'talk.religion.misc']

twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
print twenty_train.target_names, len(twenty_train.data) 

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print " X_train_counts.shape ",X_train_counts.shape


from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print "X_train_tf.shape ", X_train_tf.shape

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print 'X_train_tfidf.shape', X_train_tfidf.shape

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
docs_new = [' Bayer forms gene editing partnership with CRISPR Therapeutics Reuters via Yahoo! NewsDec 21 07:15 AM Bayer will spend 325 million euros ($353 million) on research into a promising new gene editing technology as part of a joint venture with biotech firm CRISPR Therapeutics. Under the deal, the German drugmaker will pay for the joint ventures research over the next five years, 300 million euros in total. Bayer will buy a minority stake in CRISPR Therapeutics for 35 million euros. ', 'Springboard Raises $1.7M For Its Mentor-Based Approach To Online Learning TechCrunchDec 17 03:57 AM  Springboard, an India-U.S. company formerly known as SlideRule, has raised a $1.7 million seed round to accelerate its concept of learning through mentors and a community. Each mentor provides a weekly catch-up session with their students, and Springboard partners with other MOOCs for courses, and creates its own where it sees gaps in content', 'Intel to Chinese electronics company Xiaomi: Let make a deal Intel is engaging in an intriguing business relationship with Chinese electronics manufacturer Xiaomi — if the latest rumors are to be believed, that is. Apparently, the deal gives Xiaomi a major incentive to use Intel processors as the company begins to expand its interests in the competitive laptop market. Every Core i7 processor that Xiaomi purchases for use in a laptop will be accompanied by..']

X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))