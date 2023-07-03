# WAP to perform Exploratory data analysis on House price or titanic dataset.

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

data = pd.read_csv('1553768847-housing.csv')

print(data)
print(data.head(5))
data1 = data
print(data.info())

# data analysis - stats analysis
df = pd.DataFrame(data)
print(df.describe())

df = df.drop("ocean_proximity", axis = 1 )

print(df)
print("\n")

#q1 = df.quantile([0.25])

#Q1 = np.percentile(data,25)

#q2 = df.quantile([0.50])

#q3 = df.quantile([0.75])

#Q3 = np.percentile(data,75)

#print(q1)
#print(q2)
#print(q3)

#IQR = q3 - q1
#iqr = Q3 - Q1

#print("inter quartile range : ")
#print(IQR)

#print("inter quartile range of numpy : ")
#print(iqr)

#min_val = q1 - 1.5*IQR
#max_val = q3 + 1.5*IQR

quartiles = df.quantile([0.25,0.75])
IQR = quartiles[0.75] - quartiles[0.25]
min_val = quartiles[0.25] - 1.5*IQR
max_val = quartiles[0.75] - 1.5 * IQR
print(min_val)
print(max_val)

