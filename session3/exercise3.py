import pandas as pd

# basic summary statistics:

df = pd.read_csv("brazilian_amazon_fires_1999_2019.csv")

print(df.describe())
