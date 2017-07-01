import os
import nltk
dir=os.path.normpath('C:\\Users\\hp\\Documents')
f = open(os.path.join(dir,'geography.txt'), "r")
a=f.read()
tokens = nltk.word_tokenize(a)
words = [w.lower() for w in tokens]
tagged=nltk.pos_tag(tokens)
f = open(os.path.join(dir,'geo_filtered.txt'), "w")
for (a,b) in tagged:
	if (b.startswith('NN') or b=='JJ'):
		f.write(a)
		f.write(" ")
