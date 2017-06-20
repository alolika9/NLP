def wup_similarity(s1,s2):
	t=0
	count=0
	for word1, word2 in product(s1,s2):
		syns1 = wn.synsets(word1)
		syns2 = wn.synsets(word2)
		for sense1, sense2 in product(syns1, syns2):
			d = wn.wup_similarity(sense1, sense2)
			if(d!=None):
				t=t+i
				count=count+1
	avg=t/count
