import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')

train=pd.read_csv('tweet.txt')

print("Train head")
 
print(train.head())

