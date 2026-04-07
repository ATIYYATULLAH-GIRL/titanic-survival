import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset("Iris Dataset.csv")
print(data.head())

from pandas.core.arrays import categorical
species=["setosa","virginica","versicolor"]
data["flower_num"]=pd.Categorical(data["species"],species,ordered=True)
median_value=np.median(data["flower_num"].cat.codes)
median_text=species[int(median_value)]
print(median_text)

print(data["species"].value_counts())

titanic=sns.load_dataset("titanic")
titanic.head()

print(titanic.dtypes)

nominal_cat=["sex","who"]
ordinal_cat=["alive","pclass"]

titanic["sex"].value_counts()

gender_cat=["Male","Female"]
titanic["Gender"]=pd.Categorical(titanic["sex"],gender_cat,ordered=True)
median_index=np.median(titanic["Gender"].cat.codes)
median_gender=gender_cat[int(median_index)]
print(median_gender)

sns.set_style("whitegrid")
sns.countplot(x="Gender",data=titanic,hue="survived")
plt.show()