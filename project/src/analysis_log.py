import pandas as pd
import numpy as np

df = pd.read_csv("./project/dataset/synthetic_dataset_log.csv")

print(df.head())


#Thinking about Decision-Tree prediction rather than Log.Reg, since
#There is not always yes, or always no in network traffic due to nuances.
#Therefore deciding on decision tree.
