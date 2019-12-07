import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Load data:
# Convert CSV data file to pandas DataFrame:
# TODO: Create config.
cols = ['comment_author', 'num_chars', 'has_digits', 'num_tokens', 'has_first_name', 'has_last_name', 'num_words']
path_to_data = './data/output.csv'
usernames_data = pd.read_csv(path_to_data)
#print(usernames_data)

path_to_target = './data/comments_1.5k.target'
usernames_target = pd.read_csv(path_to_target)
#print(usernames_target)

# Convert data to numeric types:
# Scikit can't handle strings. I learned that the hard way.
le = preprocessing.LabelEncoder()
# What unique values are.
#print("comment_author: ",usernames_data['comment_author'].unique()) # Strings.
# TODO: Create config.
# Data:
str_cols = ['comment_author', 'has_digits', 'has_first_name', 'has_last_name'] # Includes string and Boolean.
for col in str_cols:
    usernames_data[col] = le.fit_transform(usernames_data[col])
#print(usernames_data)
# Target:
#print("is_anonymous: ",usernames_target['is_anonymous'].unique()) # Strings.
str_cols = ['is_anonymous'] # Includes string and Boolean.
for col in str_cols:
    usernames_target[col] = le.fit_transform(usernames_target[col])
#print(usernames_target.head(n=25))


# Train/Test split:
# TODO: Create config.
cols = [col for col in usernames_data.columns if col not in ['comment_author']]
data = usernames_data[cols]
target = usernames_target
#print(data)
#print(target)
# Split data set into train and test sets:
data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.20, random_state = 10)




# Training:
svc_model = LinearSVC(random_state=0)
# Train the algorithm on training data and predict using the testing data
pred = svc_model.fit(data_train, target_train).predict(data_test)
# Print the accuracy score of the model
print('LinearSVC accuracy : ', accuracy_score(target_test, pred, normalize = True))

#print("target_test: ", target_test['is_anonymous'])
print(type(target_test)) # DataFrame.
print(type(pred)) # Numpy array.
target_test.to_csv('./data/target_test.csv', encoding='utf-8')
pd.DataFrame(pred).to_csv('./data/pred.csv', encoding='utf-8')

quit()






#clf = svm.SVC()
#clf.fit(usernames_data, usernames_target)
'''
# Option A:
# Setup SVC with certain parameters.
clf = svm.SVC(gamma=0.001, C=100.)
# Train on all data but last one.
clf.fit(iris.data[:-1], iris.target[:-1])
'''
'''
# Option B:
clf = svm.SVC()
#X, y = datasets.load_iris(return_X_y=True)
#clf.fit(X, y)
'''

# Save model:
'''
import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
'''

# Check prediction against labelled data:
#pred = clf.predict(usernames_data[-1:])
#print(pred)
'''Option A:
pred = clf.predict(iris.data[-1:])
print(pred)
''' 
'''
# Option B:
print(clf2.predict(X[0:1]))
print(y[0])
'''
