import pandas as pd

df = pd.read_csv("data/raw/mailing_fin.txt", sep="|")

print(df.head())
print(df.info())
print(df.describe())