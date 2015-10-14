__author__ = 'morita'

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter, defaultdict
import seaborn as sns
from nltk.stem.porter import *
from wordcloud import WordCloud

sns.set_style('whitegrid')

# loading the dataset
df = pd.read_json("../data/train.json")

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





# convert to mac
# stem

# pearson coefficient



'''
 Model
'''
# train_test_split os train data
# count, multinomial nb
# hash, multinomial nb
# tfidf, multinomial nb
# tfidf, ova

# DecisionsTreeClassifier - loocvs tune it, max desth, min sasple leaf, gridcv
# loocv - cross_vsl_score
# lassocv, gridcv
# fessture_impsrtsances, and cosparess agaisst worss cloud
s
# random forest, decision tree classifierss

# evaluation: accuracy, mis-classification error, precision, recall, f-score


# plots of error

# 2 * precisaion * recsll / (precision + rescall)
#
s

