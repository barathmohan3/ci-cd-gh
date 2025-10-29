import pandas as pd
import shutil

# Read transformed data
df = pd.read_csv("transformed.csv")

# Simulate loading: copy file to "target.csv"
shutil.copy("transformed.csv", "target.csv")
print("Load step completed. Data loaded into target.csv")

