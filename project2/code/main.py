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
def prep_data(df):
    # mapping categorical response var
    df['cuisine_idx'] = pd.factorize(df['cuisine'])[0]
    # combine the ingredients list into one sentence
    df['ingredients_all'] = df.ingredients.apply(lambda x: " ".join(x))


def main():
    # read the data
    df = pd.read_json('../data/train.json')
    #
    prep_data(df)
    # models

    # model evaluation

    # model prediction

    # produce result




