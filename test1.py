import os
import nltk

dir = os.path.normpath('E:\\')
f = open(os.path.join(dir,'text.txt'))

a = f.read()

a = nltk.word_tokenize(a)
a = nltk.pos_tag(a)

string=[]

temp =""
flag = 0
for name,tag in a:
    if(tag=='NNP'):
        if(flag ==0):
            temp = name
            flag = 1
        elif(temp == name):
            name = 'She'
        else:
            temp = name
        print(temp)
        
    string.append(name)

fstr = ""

for word in string:
    fstr +=word
    fstr+=" "

print(fstr)
print(temp)
f = open(os.path.join(dir,'text.txt'), "w")
f.write(fstr)
f.close()


