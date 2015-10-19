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
class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]


##############################################
#
##############################################
def cross_val_models(models, X, y, K):
    predLst = []
    for model in models:
        print "Cross_val %s..." % model[0]
        score, sem_score = cross_val_validation(model[1], X, y, K)
        predLst.append({'name': model[0],
                        'score': score,
                        'sem' : sem_score})
    return predLst

def cross_val_validation(clf, X, y, K):
    # create a k-fold cross validation iterator of K folds
    cv = KFold(len(y), K, shuffle=True, random_state=0)
    # get the mean score, and standard error mean
    scores = cross_val_score(clf, X, y, cv=cv)
    return np.mean(scores), sem(scores)


##############################################
#
##############################################
# read the data
df = pd.read_json('data/train.json')
# mapping categorical response var
df['cuisine_idx'] = pd.factorize(df['cuisine'])[0]
# combine the ingredients list into one sentence
df['ingredients_all'] = df.ingredients.apply(lambda x: " ".join(x))
# set the X, y
X = df['ingredients_all']
y = df['cuisine_idx']
# models
models = [
    ('count_nb',
        Pipeline([('vect', CountVectorizer(strip_accents='unicode')),
                  ('clf', MultinomialNB())
                 ])
    ),
    ('hashing_nb',
        Pipeline([('vect', HashingVectorizer(strip_accents='unicode', non_negative=True)),
                  ('clf', MultinomialNB()),
                 ])
    ),
    ('tfidf_nb',
        Pipeline([('vect', TfidfVectorizer(strip_accents='unicode')),
                  ('clf', MultinomialNB())
                 ])
    ),
    ('tfidf_logistic',
        Pipeline([('vect', TfidfVectorizer(strip_accents='unicode')),
                  ('clf', LogisticRegression(C=1e9))
                 ])
    ),
]
predLst = cross_val_models(models, X, y, 5)
predDf = pd.DataFrame.from_dict(predLst)
predDf





