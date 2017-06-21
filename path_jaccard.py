def path_jaccard(s1,s2):
	    i=0
	    for word1, word2 in product(s1,s2):
		    t=0
		    count=0
		    syns1 = wn.synsets(word1)
		    syns2 = wn.synsets(word2)
		    for sense1, sense2 in product(syns1, syns2):

			     d = wn.path_similarity(sense1, sense2)
			     if(d!=None and d>0.5):

				     t=t+d
		    count=count+1
		    avg = t/count
		    if(avg>0.5):
			    i=i+1
	    intersection_cardinality = i
	    union_cardinality = len(set.union(*[set(s1), set(s2)]))
	    return intersection_cardinality/float(union_cardinality)
