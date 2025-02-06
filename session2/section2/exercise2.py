import pandas as pd

# Read the CSV file
df = pd.read_csv("./data/bitcoin_info.csv", sep="\t")

# Drop rows with any missing values
new_df = df.dropna()

# Print the cleaned DataFrame
print(new_df.to_string())

# Overwrite the original CSV file with the cleaned data
new_df.to_csv(
    "./data/bitcoin_info.csv",
    mode="w",  # 'w' mode overwrites the file
    header=True,  # Include the header
    encoding="utf-8",
    sep="\t",
    index=False,
)
