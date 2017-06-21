import subprocess
import os
import nltk
from nltk.corpus import brown
import mallet
from collections import Counter
import itertools
from itertools import product
from nltk.corpus import wordnet as wn
from nltk.stem.snowball import GermanStemmer

def cosine_similarity(a,b):
    a_vals = Counter(a)
    b_vals = Counter(b)
    words  = list(a_vals.keys() | b_vals.keys())
    a_vect = [a_vals.get(word, 0) for word in words]
    b_vect = [b_vals.get(word, 0) for word in words]
    len_a  = sum(av*av for av in a_vect) ** 0.5
    len_b  = sum(bv*bv for bv in b_vect) ** 0.5
    dot    = sum(av*bv for av,bv in zip(a_vect, b_vect))
    cosine = dot / (len_a * len_b)
    return(cosine)

def wup_similarity(s1,s2):
	t=0
	count=0
	sim=[]
	for word1, word2 in product(s1,s2):
			syns1 = wn.synsets(word1)
			syns2 = wn.synsets(word2)
			for sense1, sense2 in product(syns1, syns2):
				d = wn.wup_similarity(sense1, sense2)
				if(d!=None and d>0.5):
                                        #sim.append(d)
					t=t+d
				count=count+1
	avg=t/count
	return(avg)

def path_similarity(s1,s2):
    t=0
    count=0
    for word1, word2 in product(s1,s2):
            syns1 = wn.synsets(word1)
            syns2 = wn.synsets(word2)
            for sense1, sense2 in product(syns1, syns2):
                d = wn.path_similarity(sense1, sense2)
                if(d!=None and d>0.5):
                    t=t+d
            count=count+1
    avg = t/count
    return(avg)

    
def modelling(a):
    # a is string containing the destination of the file to be modelled
    if(os.path.isfile('C:\\mallet\\example.mallet')):
       os.remove('C:\\mallet\\example.mallet')
    if(os.path.isfile('C:\\mallet\\o_keys.txt')):
       os.remove('C:\\mallet\\o_keys.txt')
    subprocess.run(['C:\\mallet\\bin\\mallet', 'import-file', '--input', a, '--output', 'C:\\mallet\\example.mallet','--keep-sequence', '--remove-stopwords'], shell=True)
    subprocess.run(['C:\\mallet\\bin\\mallet', 'train-topics', '--input','C:\\mallet\\example.mallet','--num-topics','250','--num-iterations','350', '--output-state', 'C:\\mallet\\topic-state.gz','--output-topic-keys', 'C:\\mallet\\o_keys.txt', '--output-doc-topics', 'C:\\mallet\\o_compostion.txt' ], shell = True)
    dir = os.path.normpath('C:\\mallet\\')
    f = open(os.path.join(dir,'o_keys.txt'))
    a = f.read()
    i=0
    a = a.split()
    a=(set(a))
    stemmer = GermanStemmer()
    a = [stemmer.stem(w) for w in a]
    l = []
    for char in a:
        l.append(char)
        i=i+1
        if(i==100):
            break
    a = []
    for char in l:
        if (char.isalpha()):
            a.append(char)
        
    
    return (a)



def corpus_text(a):
    dir=os.path.normpath('C:\\mallet\sample-data')
    news_text = brown.words(categories=a)
    x=' '.join(news_text)
    f = open(os.path.join(dir,a), "w")
    f.write(x)
    f.close()



def jaccard_similarity(x,y):
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality/float(union_cardinality)



def mwup_similarity(s1,s2):
	t=0
	count=0
	for word1, word2 in product(s1,s2):
		syns1 = wn.synsets(word1)
		syns2 = wn.synsets(word2)
		sim=[]
		for sense1, sense2 in product(syns1, syns2):
			d = wn.wup_similarity(sense1, sense2)
			if(d!=None):
				sim.append(d)
		if (sim):
			x=max(sim)
			t=t+x
		count=count+1
	avg=t/count
	return avg
