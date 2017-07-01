import subprocess
import mallet

import os
import nltk
list=['phy_filtered','chem_filtered','bio_filtered','geo_filtered','hist_filtered']
dir=os.path.normpath('C:\\Users\\hp\\Documents')
for k in list:
	    dir=os.path.normpath('C:\\Users\\hp\\Documents')
	    f = open(os.path.join(dir,(k+'.txt')), "r")
	    x=k[1]
	    i= 5
	    a=f.read()
	    length= len(a)
	    l=int(length/i)
	    a=a.split()
	    dir=os.path.normpath('C:\\Users\\hp\\Documents\\Batches')
	    for j in range(i):

		    n=str(j)
		    f = open(os.path.join(dir,(x+n+'.txt')), "w+")
		    for t in range(l):
			    f.write(a[(50*j)+t])

        
subprocess.run(['C:\\mallet\\bin\\mallet', 'import-file', '--input', 'C:\\Users\\hp\\Documents\\biology.txt', '--output', 'C:\\mallet\\example.mallet','--keep-sequence', '--remove-stopwords'], shell=True)

#subprocess.run(['C:\\mallet\\bin\\mallet', 'import-file', '--input', a, '--output', 'C:\\mallet\\example.mallet','--keep-sequence', '--remove-stopwords'], shell=True)
