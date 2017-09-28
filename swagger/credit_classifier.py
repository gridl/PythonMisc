import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from pandas import DataFrame
from sklearn import cross_validation, model_selection

# Feature extraction


df = pd.read_csv('cs-training.csv', sep=',', header=0)

data = df.drop(df.columns[0],axis=1)

data = data.dropna()

data = data.to_dict(orient='records')

# separate target and outcome features

vec = DictVectorizer()

df_data = vec.fit_transform(data).toarray()
feature_names = vec.get_feature_names()
df_data = DataFrame(df_data, columns=feature_names)


outcome_feature = df_data['SeriousDlqin2yrs']
target_features  = df_data.drop('SeriousDlqin2yrs', axis=1)

# separate data into trainign and test data set

"""
    X_1: independent (target) variables for first data set
    Y_1: dependent (outcome) variable for first data set
    X_2: independent (target) variables for the second data set
    Y_2: dependent (outcome) variable for the second data set
"""

X_1,X_2,Y_1,Y_2 = model_selection.train_test_split( target_features, outcome_feature, test_size=0.5, random_state=0)

# use naive Bayes classifier

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

# Train classifier
clf.fit(X_1,Y_1)

# Validate classifier
# print accuracy and confusion matrix

output = clf.predict(X_2)

from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(output, Y_2)
score = clf.score(X_2,Y_2)
print('Accuracy: {}'.format(score.mean()))
print(matrix)

#Save classifier
from sklearn.externals import joblib
joblib.dump(clf, 'nb.pkl')