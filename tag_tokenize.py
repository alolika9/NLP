path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
      raw = open(path, 'rU').read()
      print(raw)

      tokens = nltk.word_tokenize(raw)
      words = [w.lower() for w in tokens]
      vocab = sorted(set(words))
      print (vocab)

      nltk.pos_tag(token)
  
      for (a,b) in tagged:
      if (b.startswith('NN')):
	i=i+1
      print (i)
      
      f=nltk.pos_tag(tokens)
      tag_fd = nltk.FreqDist(tag for (word, tag) in f)
