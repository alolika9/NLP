from nltk.corpus import wordnet as wn
import itertools
from itertools import product
s1 = 'This is a dog.'
s1 = s1.split()
s2 = 'This is a cat.'
s2 = s2.split()

def wup_similarity(s1,s2):
    t=0
    x=0 
    count=0
    for word1, word2 in product(s1,s2):
        syns1 = wn.synsets(word1)
        syns2 = wn.synsets(word2)
        for x in range(0,30):
            d = max(i.wup_similarity(syns1[x]) for i in syns2)
            x=x+1
            if(d!=None):
                t=t+d
            count=count+1
    avg=t/count
    return(avg)

print(wup_similarity(s1,s2))
 
