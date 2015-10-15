__author__ = 'morita'

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter, defaultdict
import seaborn as sns
from nltk.stem.porter import *
from wordcloud import WordCloud
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
from sklearn.cross_validation import train_test_split, cross_val_score, KFold
from sklearn import metrics
from scipy.stats import sem

sns.set_style('whitegrid')

# loading the dataset
df = pd.read_json("data/train.json")

'''
' Exploratory Statistics
'''
print("shape:", df.shape)
print("unique cuisine count:", len(df.cuisine.unique()))

# plot number of cuisines
cuisines = df.cuisine.value_counts(sort=True)
cuisines.plot(kind="bar", figsize=(12,6), title="Number of Cuisines")


# calculating the usage of each ingredient, and for each cuisine
cuisine_dict = defaultdict(Counter)
index_dict = defaultdict(Counter)
total_counter = Counter()
stemmer = PorterStemmer()
# iterate each row
for index, row in df.iterrows():
    # get the counters
    row_counter = index_dict[row.id]
    local_counter = cuisine_dict[row.cuisine]
    # count the ingredients usage
    arr = row.ingredients
    for ingredient in row.ingredients:
        # stemm the ingredient string, e.g. 'eggs' is the same as 'egg'
        lemm_ingredient = ' '.join([stemmer.stem(word) for word in ingredient.split(' ')])
        # increment each word count
        total_counter[lemm_ingredient] += 1
        local_counter[lemm_ingredient] += 1
        row_counter[lemm_ingredient] += 1
    # update the counters
    cuisine_dict[row.cuisine] = local_counter
    index_dict[row.id] = row_counter

# plot most common ingredients
data1 = pd.DataFrame(total_counter.most_common(10), columns=["ingredient", "count"])
data1.plot(kind="bar", x="ingredient", figsize=(10,6), title="10 Most Common Ingredients")

# word cloud plot on most common ingredients
wordcloudobj = WordCloud( background_color='white')
wordcloud = wordcloudobj.generate_from_frequencies(total_counter.most_common(100))
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Most common ingredients")
plt.show()

# word cloud most common ingredients per cuisine
for key, value in cuisine_dict.iteritems():
    wc = wordcloudobj.generate_from_frequencies(value.most_common(100))
    plt.imshow(wc)
    plt.title("100 most common ingredients for '%s' cuisine" % key)
    plt.axis("off")
    plt.show()

# mds (multi-dimensional) map


# map of ingredients per cuisine



# lda topic modeling



'''
 Modeling
'''
# mapping categorical response var
df['cuisine_idx'] = df.cuisine.map({
    'brazilian':    0,
    'british':      1,
    'cajun_creole': 2,
    'chinese':      3,
    'filipino':     4,
    'french':       5,
    'greek':        6,
    'indian':       7,
    'irish':        8,
    'italian':      9,
    'jamaican':     10,
    'japanese':     11,
    'korean':       12,
    'mexican':      13,
    'moroccan':     14,
    'russian':      15,
    'southern_us':  16,
    'spanish':      17,
    'thai':         18,
    'vietnamese':   19
})

# combine the ingredients list into one sentence
df['ingredients_all'] = df.ingredients.apply(lambda x: " ".join(x))

# set the X, y
X = df['ingredients_all']
y = df['cuisine_idx']

# split data to train set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y)

# evaluate model function
def cross_val_validation(clf, X, y, K):
    # create a k-fold cross validation iterator of K folds
    cv = KFold(len(y), K, shuffle=True, random_state=0)
    # get the mean score, and standard error mean
    scores = cross_val_score(clf, X, y, cv=cv)
    print scores
    print ("Mean score: {0:.3f} (+/-{1:.3f})").format(np.mean(scores), sem(scores))

# compare the models
clf_1 = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', MultinomialNB()),
])
clf_2 = Pipeline([
    ('vect', HashingVectorizer(non_negative=True)),
    ('clf', MultinomialNB()),
])
clf_3 = Pipeline([
    ('vect', TfidfVectorizer()),
    ('clf', MultinomialNB()),
])
clfs = [clf_1, clf_2, clf_3]
for clf in clfs:
    cross_val_validation(clf, X, y, 5)

# tfidf, ova
# decisiontreeregressor
# knn
# random forest, decision tree classifier
# lassocv, gridcv

# evaluation: accuracy, mis-classification error, precision, recall, f score

#

# Arguments for Python:

# Python is easy to learn. Python is a scripting language that is easy to learn

# Python has
