import ma_py
from tabulate import tabulate
from sklearn.model_selection import train_test_split
import os


d = os.path.normpath('C:\\')
f = open(os.path.join(d,'Users\\user\\Documents\\history.txt'))
a = f.read()

train, test = ma_py.divide(a)



f = open(os.path.join(d,'mallet\\sample-data\\web\\sample1\\test1.txt'),'w')
f.write(test)
f = open(os.path.join(d,'Users\\user\\Downloads\\train1.txt'),'w')
f.write(train)

f = open(os.path.join(d,'Users\\user\\Documents\\geography.txt'))
a = f.read()

train, test = ma_py.divide(a)

f = open(os.path.join(d,'mallet\\sample-data\\web\\sample1\\test2.txt'),'w')
f.write(test)
f = open(os.path.join(d,'Users\\user\\Downloads\\train2.txt'),'w')
f.write(train)

f = open(os.path.join(d,'Users\\user\\Documents\\physics.txt'))
a = f.read()

train, test = ma_py.divide(a)

f = open(os.path.join(d,'mallet\\sample-data\\web\\sample1\\test3.txt'),'w')
f.write(test)
f = open(os.path.join(d,'Users\\user\\Downloads\\train3.txt'),'w')
f.write(train)



c1 = ma_py.modelling('C:\\Users\\user\\Downloads\\train1.txt',100)
c2 = ma_py.modelling('C:\\Users\\user\\Downloads\\train2.txt',100)
c3 = ma_py.modelling('C:\\Users\\user\\Downloads\\train3.txt',100)

x1 = ma_py.modelling('C:\\mallet\\sample-data\\web\\sample1\\test1.txt',100)
x2 = ma_py.modelling('C:\\mallet\\sample-data\\web\\sample1\\test2.txt',100)
x3 = ma_py.modelling('C:\\mallet\\sample-data\\web\\sample1\\test3.txt',100)

c1g = ma_py.extract_gen('Users\\user\\Downloads\\train1.txt',100)
c2g = ma_py.extract_gen('Users\\user\\Downloads\\train2.txt',100)
c3g = ma_py.extract_gen('Users\\user\\Downloads\\train3.txt',100)

x1g =  ma_py.extract_gen('mallet\\sample-data\\web\\sample1\\test1.txt',100)
x2g =  ma_py.extract_gen('mallet\\sample-data\\web\\sample1\\test2.txt',100)
x3g =  ma_py.extract_gen('mallet\\sample-data\\web\\sample1\\test3.txt',100)


Matrix = [[0 for x in range(4)] for y in range(4)]

i=0
j=0

'''
Matrix[0][0]=ma_py.cosine_similarity(c1,x1)
Matrix[0][1]=ma_py.cosine_similarity(c1,x2)
Matrix[0][2]=ma_py.cosine_similarity(c1,x3)

Matrix[1][0]=ma_py.cosine_similarity(c2,x1)
Matrix[1][1]=ma_py.cosine_similarity(c2,x2)
Matrix[1][2]=ma_py.cosine_similarity(c2,x3)

Matrix[2][0]=ma_py.cosine_similarity(c3,x1)
Matrix[2][1]=ma_py.cosine_similarity(c3,x2)
Matrix[2][2]=ma_py.cosine_similarity(c3,x3)




for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]
print('Cosine Similarity')
print(tabulate(Matrix))


print('\n')

Matrix[0][0]=ma_py.cosine_similarity(c1g,x1g)
Matrix[0][1]=ma_py.cosine_similarity(c1g,x2g)
Matrix[0][2]=ma_py.cosine_similarity(c1g,x3g)


Matrix[1][0]=ma_py.cosine_similarity(c2g,x1g)
Matrix[1][1]=ma_py.cosine_similarity(c2g,x2g)
Matrix[1][2]=ma_py.cosine_similarity(c2g,x3g)

Matrix[2][0]=ma_py.cosine_similarity(c3g,x1g)
Matrix[2][1]=ma_py.cosine_similarity(c3g,x2g)
Matrix[2][2]=ma_py.cosine_similarity(c3g,x3g)



for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]
print('Cosine Similarity')
print(tabulate(Matrix))

print('\n')


Matrix[0][0]=ma_py.jaccard_similarity(c1,x1)
Matrix[0][1]=ma_py.jaccard_similarity(c1,x2)
Matrix[0][2]=ma_py.jaccard_similarity(c1,x3)


Matrix[1][0]=ma_py.jaccard_similarity(c2,x1)
Matrix[1][1]=ma_py.jaccard_similarity(c2,x2)
Matrix[1][2]=ma_py.jaccard_similarity(c2,x3)


Matrix[2][0]=ma_py.jaccard_similarity(c3,x1)
Matrix[2][1]=ma_py.jaccard_similarity(c3,x2)
Matrix[2][2]=ma_py.jaccard_similarity(c3,x3)



for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]

print('Jaccard Similarity')
print(tabulate(Matrix))

print('\n')


Matrix[0][0]=ma_py.jaccard_similarity(c1g,x1g)
Matrix[0][1]=ma_py.jaccard_similarity(c1g,x2g)
Matrix[0][2]=ma_py.jaccard_similarity(c1g,x3g)


Matrix[1][0]=ma_py.jaccard_similarity(c2g,x1g)
Matrix[1][1]=ma_py.jaccard_similarity(c2g,x2g)
Matrix[1][2]=ma_py.jaccard_similarity(c2g,x3g)

Matrix[2][0]=ma_py.jaccard_similarity(c3g,x1g)
Matrix[2][1]=ma_py.jaccard_similarity(c3g,x2g)
Matrix[2][2]=ma_py.jaccard_similarity(c3g,x3g)





for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]
print('Jaccard Similarity')
print(tabulate(Matrix))

print('\n')

Matrix[0][0]=ma_py.pol_similarity(c1,x1)
Matrix[0][1]=ma_py.pol_similarity(c1,x2)
Matrix[0][2]=ma_py.pol_similarity(c1,x3)


Matrix[1][0]=ma_py.pol_similarity(c2,x1)
Matrix[1][1]=ma_py.pol_similarity(c2,x2)
Matrix[1][2]=ma_py.pol_similarity(c2,x3)

Matrix[2][0]=ma_py.pol_similarity(c3,x1)
Matrix[2][1]=ma_py.pol_similarity(c3,x2)
Matrix[2][2]=ma_py.pol_similarity(c3,x3)




for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]

print('polsim similarity')
print(tabulate(Matrix))

print('\n')

Matrix[0][0]=ma_py.pol_similarity(c1g,x1g)
Matrix[0][1]=ma_py.pol_similarity(c1g,x2g)
Matrix[0][2]=ma_py.pol_similarity(c1g,x3g)


Matrix[1][0]=ma_py.pol_similarity(c2g,x1g)
Matrix[1][1]=ma_py.pol_similarity(c2g,x2g)
Matrix[1][2]=ma_py.pol_similarity(c2g,x3g)

Matrix[2][0]=ma_py.pol_similarity(c3g,x1g)
Matrix[2][1]=ma_py.pol_similarity(c3g,x2g)
Matrix[2][2]=ma_py.pol_similarity(c3g,x3g)




for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]
print('polsim similarity')
print(tabulate(Matrix))

'''
print('\n')

Matrix[0][0]=ma_py.path_similarity(c1,x1)
Matrix[0][1]=ma_py.path_similarity(c1,x2)
Matrix[0][2]=ma_py.path_similarity(c1,x3)


Matrix[1][0]=ma_py.path_similarity(c2,x1)
Matrix[1][1]=ma_py.path_similarity(c2,x2)
Matrix[1][2]=ma_py.path_similarity(c2,x3)

Matrix[2][0]=ma_py.path_similarity(c3,x1)
Matrix[2][1]=ma_py.path_similarity(c3,x2)
Matrix[2][2]=ma_py.path_similarity(c3,x3)



for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]
print('path similarity')
print(tabulate(Matrix))

print('\n')

Matrix[0][0]=ma_py.path_similarity(c1g,x1g)
Matrix[0][1]=ma_py.path_similarity(c1g,x2g)
Matrix[0][2]=ma_py.path_similarity(c1g,x3g)

Matrix[1][0]=ma_py.path_similarity(c2g,x1g)
Matrix[1][1]=ma_py.path_similarity(c2g,x2g)
Matrix[1][2]=ma_py.path_similarity(c2g,x3g)

Matrix[2][0]=ma_py.path_similarity(c3g,x1g)
Matrix[2][1]=ma_py.path_similarity(c3g,x2g)
Matrix[2][2]=ma_py.path_similarity(c3g,x3g)




for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]
print('path similarity')
print(tabulate(Matrix))


print('\n')

Matrix[0][0]=ma_py.wup_similarity(c1,x1)
Matrix[0][1]=ma_py.wup_similarity(c1,x2)
Matrix[0][2]=ma_py.wup_similarity(c1,x3)

Matrix[1][0]=ma_py.wup_similarity(c2,x1)
Matrix[1][1]=ma_py.wup_similarity(c2,x2)
Matrix[1][2]=ma_py.wup_similarity(c2,x3)

Matrix[2][0]=ma_py.wup_similarity(c3,x1)
Matrix[2][1]=ma_py.wup_similarity(c3,x2)
Matrix[2][2]=ma_py.wup_similarity(c3,x3)



for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]
print('wup similarity')
print(tabulate(Matrix))


print('\n')

Matrix[0][0]=ma_py.wup_similarity(c1g,x1g)
Matrix[0][1]=ma_py.wup_similarity(c1g,x2g)
Matrix[0][2]=ma_py.wup_similarity(c1g,x3g)


Matrix[1][0]=ma_py.wup_similarity(c2g,x1g)
Matrix[1][1]=ma_py.wup_similarity(c2g,x2g)
Matrix[1][2]=ma_py.wup_similarity(c2g,x3g)

Matrix[2][0]=ma_py.wup_similarity(c3g,x1g)
Matrix[2][1]=ma_py.wup_similarity(c3g,x2g)
Matrix[2][2]=ma_py.wup_similarity(c3g,x3g)




for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]
print('wup similarity')
print(tabulate(Matrix))
