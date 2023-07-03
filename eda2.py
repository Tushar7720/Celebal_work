import numpy as np
import pandas as pd

data = pd.read_csv('1553768847-housing.csv')

print(data)
print(data.head(5))
print(data.shape)
print(data.info())
print(data.describe())
print(data.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(x='median_house_value', data=data, )
plt.show()

sns.boxplot( x="median_house_value", y='ocean_proximity', data=data, )
plt.show()

sns.scatterplot( x="median_house_value", y='total_rooms', data=data, hue="ocean_proximity")
plt.show()
