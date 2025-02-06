import pandas as pd

df = pd.read_csv("../../data/exercise_data.csv")
print(df.corr())
# there is a strong correlation of 0.9 between the calories duration and the calories burned - the higher the duration, the more calories burned. There is a positive correlation.
# Also, the higher the pulse, the higher maximum pulse, therefore there is also a correlation with this.
