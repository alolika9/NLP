import os
import subprocess
from collections import Counter
from nltk.corpus import brown

news_text = brown.words(categories='news')
subprocess.run(['C:\\mallet\\bin\\mallet', 'import-file', '--input', 'news_text', '--output', 'C:\\mallet\\computer.mallet','--keep-sequence', '--remove-stopwords'], shell=True)
subprocess.run(['C:\\mallet\\bin\\mallet', 'import-file', '--input', 'C:\\mallet\\sample-data\\web\sample1\\movies.txt', '--output', 'C:\\mallet\\movie.mallet','--keep-sequence', '--remove-stopwords'], shell=True)
'''
subprocess.run(['C:\\mallet\\bin\\mallet', 'train-topics', '--input','C:\\mallet\\computer.mallet','--num-topics','200','--num-iterations','350', '--output-state', 'C:\\mallet\\topic-state.gz','--output-topic-keys', 'C:\\mallet\\c_keys.txt', '--output-doc-topics', 'C:\\mallet\\c_compostion.txt' ], shell = True)
subprocess.run(['C:\\mallet\\bin\\mallet', 'train-topics', '--input','C:\\mallet\\computer.mallet','--num-topics','200','--num-iterations','350', '--output-state', 'C:\\mallet\\topic-state.gz','--output-topic-keys', 'C:\\mallet\\m_keys.txt', '--output-doc-topics', 'C:\\mallet\\m_compostion.txt' ], shell = True)
subprocess.run(['C:\\mallet\\bin\\mallet', 'import-file', '--input', 'C:\\mallet\\sample-data\\web\sample1\\example.txt', '--output', 'C:\\mallet\\example.mallet','--keep-sequence', '--remove-stopwords'], shell=True)
subprocess.run(['C:\\mallet\\bin\\mallet', 'train-topics', '--input','C:\\mallet\\example.mallet','--num-topics','200','--num-iterations','350', '--output-state', 'C:\\mallet\\topic-state.gz','--output-topic-keys', 'C:\\mallet\\o_keys.txt', '--output-doc-topics', 'C:\\mallet\\o_compostion.txt' ], shell = True)
dir = os.path.normpath('C:\\mallet\\')

f = open(os.path.join(dir,'c_keys.txt'))
a = f.read()

a = a.split()



l = []
for char in a:
        l.append(char)
        if(char=='20'):
            break

a = []
for char in l:
    if (char.isalpha()):
        a.append(char)
        
a=(set(a))

for char in a:
    print(char)


f = open(os.path.join(dir,'m_keys.txt'))
b = f.read()

b = b.split()



l = []
for char in b:
        l.append(char)
        if(char=='20'):
            break

b = []
for char in l:
    if (char.isalpha()):
        b.append(char)
        
b=(set(b))

for char in b:
    print(char)


f = open(os.path.join(dir,'o_keys.txt'))
c = f.read()

c = c.split()



l = []
for char in c:
        l.append(char)
        if(char=='20'):
            break

c = []
for char in l:
    if (char.isalpha()):
        c.append(char)
        
c=(set(c))

for char in c:
    print(char)


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
    print(cosine)

'''
