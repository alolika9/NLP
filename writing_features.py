import ma_py
import os

phy = ma_py.batch_lda('C:\\Users\\user\\Documents\\physics.txt',5,100)
chem = ma_py.batch_lda('C:\\Users\\user\\Documents\\chemistry.txt',5,100)
bio = ma_py.batch_lda('C:\\Users\\user\\Documents\\biology.txt',5,100)
#bio = ma_py.batch_lda('C:\\Users\\user\\Documents\\history.txt',5,100)
#bio = ma_py.batch_lda('C:\\Users\\user\\Documents\\geography.txt',5,100)


d = os.path.normpath('C:\\Users\\user\\Documents\\python\\')

f = open(os.path.join(d,'physics_features.txt'),'w')
l=' '.join(i for i in phy)
f.write(l)

f = open(os.path.join(d,'chemistry_features.txt'),'w')
l=' '.join(i for i in chem)
f.write(l)

f = open(os.path.join(d,'biology_features.txt'),'w')
l=' '.join(i for i in bio)
f.write(l)

