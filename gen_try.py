import os
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
from gensim import corpora
from nltk.corpus import stopwords 
from nltk.corpus import wordnet as wn
from nltk.stem.snowball import GermanStemmer

import nltk


d = os.path.normpath('C:\\mallet\\sample-data\\web\\sample1')
f = open(os.path.join(d,'tech.txt'))
a = f.read()

stop = set(stopwords.words('english'))


tokens = nltk.word_tokenize(a)

tokens = [w for w in tokens if not w in stop]

a=(set(tokens))
stemmer = GermanStemmer()
a = [stemmer.stem(w) for w in a]

a = " ".join([i for i in a])
a= a.split()

dictionary = corpora.Dictionary([a])

doc_term_matrix = [dictionary.doc2bow(doc) for doc in [a]]


Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=30, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=30, num_words=3))
