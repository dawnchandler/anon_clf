# Anonymous Username Classifier

This repo is the implementation of an anonymous username classifier for LING 807 at SFU in Fall 2019.

### Goal
The goal of this project was to see whether usernames could be successfully classified by a machine learning model as Anonymous or Identified *using only features extracted from the username string.* 

### Implementation

##### Data
The data comes from [the SOCC dataset](https://github.com/sfu-discourse-lab/SOCC/). Using a combination of Excel, vim, and bash, I extracted 1,500 unique usernames from the raw data comments corpus. This did not comprise even 1% of the data. I manually annotated all the usernames as Identifiable or Anonymous.

The data files are not currently available in this repo. As a todo item for myself, I intend to modify the existing scripts (and create a username extraction script) to automate the pipeline for anyone who clones this repo. Once that is done, the data will be available here.

##### Features
From each username string, I extracted the following features with the script [extract_features.py](https://github.com/dawnchandler/anon_clf/blob/master/extract_features.py).
```comment_author,num_chars,has_digits,num_tokens,has_first_name,has_last_name,num_words```
To construct some of these features, I used [the SOWPODS Scrabble word list](https://www.wordgamedictionary.com/sowpods/) and [the Names Database](https://github.com/smashew/NameDatabases).

##### Model
With the unlabelled data file of usernames with features and the file of their labels, I trained an SVM classifier using scikit-learn and an 80/20 train/test split.

### Results
In general, this classifier works okay. It shows promise, but it could use a lot of improvements.

To learn more about the results of this project, please read [my paper](https://github.com/dawnchandler/anon_clf/blob/master/chandler_2019.pdf). 
