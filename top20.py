import ma_py
from tabulate import tabulate
from math import*
c1 = ma_py.modelling('C:\\Users\\user\\Downloads\\news_corpus.docx')
c2 = ma_py.modelling('C:\\Users\\user\\Downloads\\sport.txt')
x1 = ma_py.modelling('C:\\mallet\\sample-data\\web\\sample1\\news.txt')
x2 = ma_py.modelling('C:\\mallet\\sample-data\\web\\sample1\\cricket.txt')
x3 = ma_py.modelling('C:\\mallet\\sample-data\\web\\sample1\\government.txt')

Matrix = [[0 for x in range(4)] for y in range(4)]

i=0
j=0



Matrix[0][0]=ma_py.jaccard_similarity(c1,x1)
Matrix[0][1]=ma_py.jaccard_similarity(c1,x2)
Matrix[0][2]=ma_py.jaccard_similarity(c1,x3)

Matrix[1][0]=ma_py.jaccard_similarity(c2,x1)
Matrix[1][1]=ma_py.jaccard_similarity(c2,x2)
Matrix[1][2]=ma_py.jaccard_similarity(c2,x3)

for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]

print(tabulate(Matrix))
