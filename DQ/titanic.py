import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset

test = pd.read_csv("test.csv")
test_shape = test.shape

train = pd.read_csv("train.csv")
train_shape = train.shape

print(test_shape)

# Learn the dataset

sex_pivot = train.pivot_table(index="Sex",values="Survived")
#sex_pivot.plot.bar()
#plt.show()

pclass_pivot = train.pivot_table(index="Pclass",values="Survived")
#pclass_pivot.plot.bar()
#plt.show()

# Clean up
# cuts the Age column into three segments: Missing, Child, and Adult using pandas.cut().

def process_age(df,cut_points,label_names):
    df["Age"] = df["Age"].fillna(-0.5)
    df["Age_categories"] = pd.cut(df["Age"],cut_points,labels=label_names)
    return df

cut_points = [-1,0,5,12,18,35,60,100]
label_names = ["Missing","Infant","Child", "Teenager","Young Adult","Adult","Senior"]

train = process_age(train,cut_points, label_names)
test = process_age(test,cut_points,label_names)
pivot = train.pivot_table(index="Age_categories", values="Survived")
#pivot.plot.bar()
#plt.show()

# create_dummies() function to create dummy variables for the Sex column:
# can create dummy columns for each unique value in the column
def create_dummies(df,column_name):
    dummies = pd.get_dummies(df[column_name],prefix=column_name)
    df = pd.concat([df,dummies],axis=1)
    return df

train = create_dummies(train,"Pclass")
test = create_dummies(test,"Pclass")

train = create_dummies(train,"Sex")
test = create_dummies(test,"Sex")

train = create_dummies(train,"Age_categories")
test = create_dummies(test,"Age_categories")


columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']

# Train model using Logistic Regression

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train[columns],train['Survived'])

holdout = test # from now on we will refer to this
               # dataframe as the holdout data

from sklearn.model_selection import train_test_split

columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']

all_X = train[columns]
all_y = train['Survived']

train_X,test_X, train_y,test_y = train_test_split(all_X,all_y, test_size=0.2,random_state=0)

# Predictions

from sklearn.metrics import accuracy_score
lr = LogisticRegression()
lr.fit(train_X, train_y)
predictions = lr.predict(test_X)

accuracy = accuracy_score(test_y, predictions)
print(accuracy)

# Cross Validation to train and test our model on different splits of our data, and then average the accuracy scores.
#

from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.metrics import accuracy_score
lr = LogisticRegression()
scores = cross_val_score(lr,all_X,all_y,cv=10)

accuracy = np.mean(scores)
print(scores)
print(accuracy)

# Train our final model and then make predictions on our unseen holdout data
columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']
lr = LogisticRegression()
lr.fit(all_X,all_y)
holdout_predictions = lr.predict(holdout[columns])


# Create submissions

holdout_ids = holdout["PassengerId"]
submission_df = {"PassengerID": holdout_ids,"Survived":holdout_predictions}
submission = pd.DataFrame(submission_df)
submission.to_csv("submission.csv", index=False)


