from sklearn.model_selection import train_test_split as tts

# define class labels and the doucment ids


reader = PickledCorpusReader('corpus/')
for category in reader.categories():
    n_docs = len(reader.fileids(categories=[category]))
    n_words = sum(1 for word in reader.words(categories=[category]))

    print("- '{}' contains {:,} docs and {:,} words".format(category, n_docs,n_words))


labels = ["books","cinema","cooking","gaming","sports", "tech"]

docs = reader.fileids(categories=lables)

X = [reader.docs(fileids=[doc]) for doc in docs]
y = [reader.categories(fileids=[doc])[0] for doc in docs]

X_train, X_test, y_train, y_test = tts(X,y,test_size=0.2)