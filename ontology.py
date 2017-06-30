import ma_py
import os

query = input("Enter Query\n")

query = query.split()

print('Recieved.\n')

phy = ma_py.modelling('C:\\Users\\user\\Documents\\physics.txt',100)
chem = ma_py.modelling('C:\\Users\\user\\Documents\\chemistry.txt',100)
bio = ma_py.modelling('C:\\Users\\user\\Documents\\biology.txt',100)

geo = ma_py.modelling('C:\\Users\\user\\Documents\\geography.txt',100)
his = ma_py.modelling('C:\\Users\\user\\Documents\\history.txt',100)

sc = phy + chem + bio
ar = geo + his



print('Your query is related to:\n')

s = ma_py.pol_similarity(query,sc)
a = ma_py.pol_similarity(query,ar)

if(s>a):
    p = ma_py.pol_similarity(query,phy) 
    c = ma_py.pol_similarity(query,chem)
    b = ma_py.pol_similarity(query,bio)
    m = max(p,c,b)
    if(m==p):
        print('Physics')
    elif(m==c):
        print('Chemistry')
    else:
        print('Biology')
else:
    g = ma_py.pol_similarity(query,geo)
    h = ma_py.pol_similarity(query,his)
    if(g>h):
        print('Geography')
    else:
        print('History')
 
