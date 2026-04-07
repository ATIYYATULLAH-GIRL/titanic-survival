import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset("Bestsellers.csv")
print(data.head())

from pandas.core.arrays import categorical
genre=["non-fiction","fiction"]
data["type_num"]=pd.Categorical(data["Genre"],genre,ordered=True)
median_value=np.median(data["type_num"].cat.codes)
median_text=genre[int(median_value)]
print(median_text)

print(data["Genre"].value_counts())