import pandas as pd

df = pd.read_csv("./data/data.csv")

new_df = df.dropna()

new_df.loc[7, "Duration"] = 45
new_df.drop_duplicates(inplace=True)

# print(new_df.to_string())


new_df.to_csv("exercise_data.csv")
