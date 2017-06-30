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
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
from gensim import corpora
from nltk.corpus import stopwords 
from sklearn.model_selection import train_test_split
import random
from nltk.stem.wordnet import WordNetLemmatizer
import string
from math import e

def get_height(a,b):
        try:
                a=wn.synsets(a)
                a = a[0]
                b=wn.synsets(b)
                b = b[0]
                hyper = lambda s: s.hypernyms()
                l1=list(a.closure(hyper))
                l2=list(b.closure(hyper))
                intersection_cardinality = len(set.intersection(*[set(l1), set(l2)]))
        except IndexError:
                return None
        return (intersection_cardinality - 1)

def get_length(a,b):
        try:
                a=wn.synsets(a)
                a = a[0]
                b=wn.synsets(b)
                b = b[0]
                distance = a.shortest_path_distance(
                    b,
                    simulate_root=True and a._needs_root
                )
        except IndexError:
                return None
        return distance

def paper_sim(a,b):
        alpha = 0.2
        beta = 0.45
        try:
                sim= (e**(beta*get_height(a,b))-e**(-beta*get_height(a,b)))/(e**(beta*get_height(a,b))+e**(-beta*get_height(a,b)))* (e**(-alpha*get_length(a,b)))
        except:
                return 0
        return sim

def p_similarity(a,b):
        s = 0
        count = 0
        for i in range(len(a)):
                for j in range(len(b)):
                        if(paper_sim(a[i],b[j])>0.5):
                                s = s + paper_sim(a[i],b[j])
                                count = count + 1
        avg = s/count
        return avg

def polsim(word1,word2):
        j=0
        k=0
        alpha = 0.5
        beta = 0.4
        a = wn.synsets(word1)
        b = wn.synsets(word2)
        try:
                x = a[0]
                y = b[0]
        except IndexError:
                return None
        hyper = lambda s: s.hypernyms()
        l1 = list(x.closure(hyper))
        l2 = list(y.closure(hyper))
        while(l1==[] or l2 ==[]):
                l1 = list(x.closure(hyper))
                l2 = list(y.closure(hyper))
                if(l1 == []):
                        j=j+1
                        try:
                                x = a[j]
                        except IndexError:
                                return None
                if(l2 == []):
                        k = k+1
                        try:
                                y = b[k]
                        except IndexError:
                                return None
        f1=[]
        f2=[]
        for i in range(len(l1)):
                s=str(l1[i])
                s=s[8:(len(s)-7)]
                f1.append(s)
        for i in range(len(l2)):
                s=str(l2[i])
                s=s[8:(len(s)-7)]
                f2.append(s)
                x=cosine_similarity(f1,f2)
                h = get_height(word1,word2)
                l = get_length (word1,word2)
                x = (e**alpha*(h))*x*(e**(-beta*l))
        return (x)

def pol_similarity(a,b):
    count = 0
    x = 0
    for i in range(len(a)):
        for j in range(len(b)):
            d = polsim(a[i],b[j])
            if(d!=None and d>0.8):
                x=x+d
                count = count+1
    try:
        avg = x/count
    except:
            return 0
    return(avg)

def jacc(a,b):
        intersection_cardinality = len(set.intersection(*[set(a), set(b)]))
        union_cardinality = len(b)
        return (intersection_cardinality/(union_cardinality))


def path_jaccard(s1,s2):
    i=0
    for word1, word2 in product(s1,s2):
        t=0
        count=0
        syns1 = wn.synsets(word1)
        syns2 = wn.synsets(word2)
        for sense1, sense2 in product(syns1, syns2):
            d = wn.path_similarity(sense1, sense2)
            if(d!=None and d>0.6):
                t=t+d
                count=count+1
        if(count!=0):
            avg = t/count
        else:
            avg =0
        if(avg>0.12):
            i=i+1
        intersection_cardinality = i
    union_cardinality = len(set.union(*[set(s1), set(s2)]))
    return intersection_cardinality/float(union_cardinality)

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
    for i in range(len(s1)):
        for j in range(len(s2)):
            syns1 = wn.synsets(s1[i])
            syns2 = wn.synsets(s2[j])
            if(len(syns1)>0 and len(syns2)>0):
                syns1 = syns1[0]
                syns2 = syns2[0]
                d = wn.wup_similarity(syns1, syns2)
                if(d!=None):
                    t=t+d
                    count=count+1
    if(count!=0):
        avg=t/count
    else:
        avg=0
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

    
def modelling(a,num):
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
    a = a.lower()
    a = a.split()
    a=(set(a))
    #lmtzr = WordNetLemmatizer()
    l = []
    for char in a:
        if (char.isalpha()):
            #char = lmtzr.lemmatize(char)
            l.append(char)

    a = []
    for char in l:
        a.append(char)
        i=i+1
        if(i==num):
            break
    
    
        
    
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

def extract_gen(a,num):
    d = os.path.normpath('C:\\')
    f = open(os.path.join(d,a))
    a = f.read()
    a = a.lower()

    exclude = set(string.punctuation)
    s = ''.join(ch for ch in a if ch not in exclude)
    

    stop = set(stopwords.words('english'))


    tokens = nltk.word_tokenize(a)

    tokens = [w for w in tokens if not w in stop]
    lmtzr = WordNetLemmatizer()
    l = []
    for char in tokens:
        l.append(lmtzr.lemmatize(char))

    a=(set(l))

    a = " ".join([i for i in a])
    a= a.split()
    


    dictionary = corpora.Dictionary([a])

    doc_term_matrix = [dictionary.doc2bow(doc) for doc in [a]]


    Lda = gensim.models.ldamodel.LdaModel

    # Running and Trainign LDA model on the document term matrix.
    ldamodel = Lda(doc_term_matrix, num_topics=num, id2word = dictionary, passes=50)

    

    l = []
    for i in range(100):
        if((ldamodel.id2word[i]).isalpha()):
            l.append(ldamodel.id2word[i])
    return l

def divide(a):
        a=a.split('\n')
        l = list(a)
        random.shuffle(l)
        y = ' '.join(l)
        train_data = y[:int((len(y)+1)*.80)]
        test_data = y[int(len(y)*.80+1):]
        return train_data, test_data
        

