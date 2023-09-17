# NLP
Research project on NLP, performing feature extraction using machine learning algorithms. The project involved the application of all the corpus-based similarity methods and the formulation of a new method with problem-specific variations.
The ontology is designed to categorize an input to one of the categories we train the model on with corpora.

Main idea -> Extract features from the corpuses using LDA by Gensim, and use these features to map a given input to one of our topics. Various methods were implemented starting from cosine similarity, then moving on to using more sophisticated methods for finding similarity between input and corpus features, involving using similarity methods from NLTK wordnet, and experimenting WUP.
The research also proposes a new similarity measure called the polsim similarity.
