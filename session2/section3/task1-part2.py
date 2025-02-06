import pandas as pd

df = pd.read_csv("../../data/bitcoin_info_cleaned.csv", sep="\t")

# Drop rows where the 'Value' column has NaN values
df_cleaned = df.dropna(subset=["Value"])

df_cleaned = df_cleaned.reset_index(drop=True)

df_cleaned.to_csv(
    "../../data/bitcoin_info_cleaned.csv", index=False, sep="\t", encoding="utf-8"
)

print(df_cleaned.head())
