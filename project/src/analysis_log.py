
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("./project/dataset/synthetic_dataset_log.csv")

print(df.head())

# Have not done EDA, just process in the start for correct syntax. 

X = df.drop('Label', axis=1)
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

DTC = DecisionTreeClassifier(criterion='log_loss', max_depth=5, random_state=42)

d = DTC.fit(X_train,y_train)


#Thinking about Decision-Tree prediction rather than Log.Reg, since
#There is not always yes, or always no in network traffic due to nuances.
#Therefore deciding on decision tree.

