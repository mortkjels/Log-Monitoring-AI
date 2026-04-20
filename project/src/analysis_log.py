
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

print("Laster inn datasettet")
df = pd.read_csv("./project/dataset/synthetic_dataset_log.csv")

print(df.head())

df['Label'].value_counts().plot(kind='bar')

plt.title("Benign against Malicious")
plt.show()

# X = df.drop('Label', axis=1).select_dtypes(include=['number'])
# y = df['Label']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# DTC = DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42)

# d = DTC.fit(X_train,y_train)





