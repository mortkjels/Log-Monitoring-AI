import pandas as pd
import numpy as np
from pathlib import Path

current_path = Path(__file__).parent

file_path = current_path.parent / "dataset" / "synthetic_dataset_log.csv"

df = pd.read_csv(file_path)

print(df.head())