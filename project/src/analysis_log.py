
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from xgboost import XGBClassifier

print("Laster inn datasettet")
df = pd.read_csv("./project/dataset/synthetic_dataset_log.csv")

print(df.head())

df['Label'].value_counts().plot(kind='bar')

x = df.drop('Label', axis=1).select_dtypes(include=['number'])

dict = {'BENIGN': 0, 'DDoS': 1, 'Bot':2 , 'DoS-Hulk': 3, 'FTP-Patator': 4, 'SSH-Patator': 5, 'Infiltration': 6 , 'DoS-Slowloris': 7, 'WebAttack-BruteForce': 8 ,'PortScan': 9}

df['Label'] = df['Label'].replace(dict)

y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

bst = XGBClassifier(n_estimators = 2, learning_rate = 1)

pred = bst.fit(X_train,y_train)


