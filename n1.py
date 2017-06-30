import os
from nltk.corpus import wordnet as wn
import ma_py

d = os.path.normpath('C:\\Users\\user\\Downloads\\')
f = open(os.path.join(d,'random.txt'))
a = f.read()

f = open(os.path.join(d,'t.txt'),'w')
f.write('')

f = open(os.path.join(d,'nt.txt'),'w')
f.write('')

c1 = ma_py.modelling('C:\\Users\\user\\Downloads\\technical_corpus.txt',100)
c2 = ma_py.modelling('C:\\Users\\user\\Downloads\\non-technical.txt',100)

a = a.split('\n')

for i in range(len(a)):
    f = open(os.path.join(d,'test.txt'),'w')
    f.write(a[i])
    f.close()
    x = ma_py.modelling('C:\\Users\\user\\Downloads\\test.txt',30)
    t = ma_py.pol_similarity(c1,x)
    nt = ma_py.pol_similarity(c2,x)
    print(a[i])
    print (t)
    print (nt)
    if (t>nt):
        f = open(os.path.join(d,'t.txt'),'a')
        f.write(a[i])
        f.write('\n')
        f.close()
    else:
        f = open(os.path.join(d,'nt.txt'),'a')
        f.write(a[i])
        f.write('\n\n\n')
        f.close()
