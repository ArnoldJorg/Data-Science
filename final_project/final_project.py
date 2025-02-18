import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

df = pd.read_csv("bitcoin_historical_data.csv", sep=";")

# getting a glimpse of the data - and seeing if it was seperated properly
df["timeOpen"] = pd.to_datetime(df["timeOpen"])
df["timeClose"] = pd.to_datetime(df["timeClose"])
df["timeHigh"] = pd.to_datetime(df["timeHigh"])
df["timeLow"] = pd.to_datetime(df["timeLow"])
df["timestamp"] = pd.to_datetime(df["timestamp"])


print(df.head())

#  visualise and analyse and describe

#  checking if anything is null / missing values

print(df.isnull().sum())

# there are no missing values (all zeros)

s = df.duplicated()
print(s)

print(df.describe())

plt.figure(figsize=(12, 6))

plt.plot(df["timeOpen"], df["high"], label="high prices", color="green")
plt.plot(df["timeOpen"], df["low"], label="low prices", color="red")

plt.title("bitcoin price USD 2024-2025 (highs & lows)")
plt.xlabel("Date / Time")
plt.ylabel("Price USD")
plt.grid(True)
# plt.xticks()


# plt.legend()
plt.tight_layout()
plt.show()
