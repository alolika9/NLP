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


for s in range(2):
    c1 = ma_py.modelling('C:\\Users\\user\\Downloads\\train1.txt',100)
    c2 = ma_py.modelling('C:\\Users\\user\\Downloads\\train2.txt',100)
    c3 = ma_py.modelling('C:\\Users\\user\\Downloads\\train3.txt',100)

    x1 = ma_py.modelling('C:\\mallet\\sample-data\\web\\sample1\\test1.txt',30)
    x2 = ma_py.modelling('C:\\mallet\\sample-data\\web\\sample1\\test2.txt',30)
    x3 = ma_py.modelling('C:\\mallet\\sample-data\\web\\sample1\\test3.txt',30)

    c1g = ma_py.extract_gen('Users\\user\\Downloads\\train1.txt',100)
    c2g = ma_py.extract_gen('Users\\user\\Downloads\\train2.txt',100)
    c3g = ma_py.extract_gen('Users\\user\\Downloads\\train3.txt',100)

    x1g =  ma_py.extract_gen('mallet\\sample-data\\web\\sample1\\test1.txt',30)
    x2g =  ma_py.extract_gen('mallet\\sample-data\\web\\sample1\\test2.txt',30)
    x3g =  ma_py.extract_gen('mallet\\sample-data\\web\\sample1\\test3.txt',30)

    
    m_sum = 0
    temp = 0

    Matrix = [[0 for x in range(4)] for y in range(4)]
    Matrix_temp =  [[0 for x in range(4)] for y in range(4)]
    


    Matrix[0][0]=ma_py.p_similarity(c1,x1)
    Matrix[0][1]=ma_py.p_similarity(c1,x2)
    Matrix[0][2]=ma_py.p_similarity(c1,x3)

    Matrix[1][0]=ma_py.p_similarity(c2,x1)
    Matrix[1][1]=ma_py.p_similarity(c2,x2)
    Matrix[1][2]=ma_py.p_similarity(c2,x3)

    Matrix[2][0]=ma_py.p_similarity(c3,x1)
    Matrix[2][1]=ma_py.p_similarity(c3,x2)
    Matrix[2][2]=ma_py.p_similarity(c3,x3)

    print(tabulate(Matrix))

    for i in range(3):
        for j in range(3):
            if(i==j):
                m_sum = m_sum + 2*(Matrix[i][j])
            else:
                m_sum = m_sum - Matrix[i][j]

    if(m_sum>temp):
        Matrix_temp = Matrix
        temp = m_sum

    
Matrix = Matrix_temp

for i in range(0,3):
    Matrix[i][3]= Matrix[i][0]+ Matrix[i][1]+ Matrix[i][2]

Matrix[3][3]=Matrix[0][3]+ Matrix[1][3]+ Matrix[2][3]
print('Cosine Similarity')
print(tabulate(Matrix))
