__author__ = 'morita'


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter, defaultdict
import seaborn as sns
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *
from wordcloud import WordCloud
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer, TfidfTransformer
from sklearn.cross_validation import train_test_split, cross_val_score, KFold
from sklearn import metrics
from scipy.stats import sem
from sklearn.manifold import MDS
from sklearn.metrics import euclidean_distances, roc_curve, auc
from sklearn.datasets import make_classification
import matplotlib.pylab as pyl
from sklearn.ensemble import RandomForestClassifier

sns.set_style('whitegrid')

##############################################
#
##############################################
# cross validate each model
def cross_val_models(models, X, y, K):
    predLst = []
    for model in models:
        print "Cross_val %s..." % model[0]
        score, sem_score = cross_val_validation(model[1], X, y, K)
        predLst.append({'name': model[0],
                        'score': score,
                        'sem' : sem_score})
    return predLst

# get the mean score, and standard error mean
def cross_val_validation(clf, X, y, K):
    # create a k-fold cross validation iterator of K folds
    cv = KFold(len(y), K, shuffle=True, random_state=0)
    # get the mean score, and standard error mean
    scores = cross_val_score(clf, X, y, cv=cv, scoring="accuracy")
    return np.mean(scores), sem(scores)

# replacement data. Philadelphia Cream Cheese -> cream cheese
thesauri = {}
with open("code/thesauri.txt", "r") as f:
    for line in f:
        entry = line.strip().split(",")
        key = entry[0]
        value = entry[1]
        thesauri[key] = value
f.close()


# custom stop words
stopwords = []
with open("code/stopwords.txt", "r") as f:
    for line in f:
        stopwords.append(line.strip())
f.close()

# clean ingredients
def clean_ingredients(ingredients):
    stemmer = PorterStemmer()
    new_ingredients = []
    for one in ingredients:
        # if match thesauri, then use its simpler form
        newone = one
        if one in thesauri:
            newone = thesauri[one]
        # if is not a stop word, then append
        new_ingredients.append(
            " ".join([stemmer.stem(t) for t in word_tokenize(one) if not t in stopwords])
        )
    return ",".join(new_ingredients)


##############################################
#
##############################################
# read the data
df = pd.read_json('data/train.json')
# mapping categorical response var
df['cuisine_idx'] = pd.factorize(df['cuisine'])[0]
# combine the ingredients list into one sentence
# now do it for all observations
df['ingredients_all'] = df.ingredients.apply(clean_ingredients)


# calculating the usage of each ingredient, and for each cuisine
cuisine_dict = defaultdict(Counter)
index_dict = defaultdict(Counter)
total_counter = Counter()
# iterate each row
for index, row in df.iterrows():
    # get the counters
    row_counter = index_dict[row.id]
    local_counter = cuisine_dict[row.cuisine]
    # count the ingredients usage
    arr = row.ingredients
    for ingredient in row.ingredients:
        key = ingredient.lower()
        # increment each word count
        total_counter[key] += 1
        local_counter[key] += 1
        row_counter[key] += 1
    # update the counters
    cuisine_dict[row.cuisine] = local_counter
    index_dict[row.id] = row_counter


import itertools


total_ingredients_dict = {}
for key, value in cuisine_dict.iteritems():
    total_ingredients_dict[key] = len(value)

df['ingredients_all'] = df.ingredients.apply(lambda x: " ".join(x))
# stem the ingredients
stemmer = PorterStemmer()
df['ingredients_stem'] = df.ingredients_all.apply(lambda x: " ".join([stemmer.stem(word.lower()) for word in x.split(" ")]))
# set the X, y
X = df['ingredients_stem']
y = df['cuisine_idx']
#
predDf = []
# models
models = [
    ('rf',
        Pipeline([('vect', TfidfVectorizer(strip_accents='unicode')),
                  ('clf', RandomForestClassifier(n_estimators=1000, random_state=0))
                 ])
    ),
]
# evaluate them
rf = cross_val_models(models, X, y, 5)
predDf = predDf.append(rf, ignore_index=True)
predDf



