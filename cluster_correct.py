from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import os  # for os.path.basename

import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.manifold import MDS



text_file = open("tweet.txt", "r")
documents = text_file.read().split('\n')


#vectorize the text i.e. convert the strings to numeric features
vectorizer = TfidfVectorizer(encoding='latin-1')
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)
#cluster documents
true_k = 8
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=1000, n_init=1)
model.fit(X)
#print top terms per cluster clusters
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
#text_file1 = open("event_clusters.txt", "w")
for i in range(true_k):
    print("Cluster %d:" % i,)
    for ind in order_centroids[i, :50]:
        print('%s' % terms[ind],)
    print()