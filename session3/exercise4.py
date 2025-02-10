import matplotlib.pyplot as plt
import pandas as pd

# Exercise 4: Exploratory Data Analysis - Count of firespots by state
# Analyze the distribution of firespots across different states.

# grouping the data by 'state' and sum the number of 'firespots'

# sorting the results by the number of firespots in descending order

# plot the results using a bar plot
# remember in the lecture example we used plt.plot for a basic line plot but now we need a bar , follow that example to set color too

# show your plot

# titanic.groupby("Sex")["Age"].mean() - line from pandas docs

df = pd.read_csv("brazilian_amazon_fires_1999_2019.csv")

fire_spots_by_state = df[["state", "firespots"]].groupby("state").sum()

# print(fire_spots_by_state)

# is working - now I need to sort it in descending order

fire_spots_sorted = fire_spots_by_state.sort_values(ascending=False, by="firespots")
print(fire_spots_sorted)

# this is also working so I now need to plot this.

plt.figure(figsize=(12, 6))

plt.bar(fire_spots_sorted.index, fire_spots_sorted["firespots"], color="orange")

plt.title("amount of firespots per state")

plt.xlabel("state")
plt.ylabel("Number of Firespots")
plt.grid(True)
# plt.xticks(rotation=90)
plt.show()
