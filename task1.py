import nltk
import matplotlib
import os

dir = os.path.normpath("E:\\books\\")
f = open(os.path.join(dir,'Lord_Edgware_Dies.txt'),'r')
a = f.read()
token = nltk.word_tokenize(a)
token = nltk.pos_tag(token)

words, tags = zip(*token)
cfd = nltk.FreqDist(tags)


i=0
for word in tags:
    if (word.startswith('NN')):
        i = i+1

print(i)
