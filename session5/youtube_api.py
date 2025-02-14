import os
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build
from textblob import TextBlob

load_dotenv()

youtube_api_key = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=youtube_api_key)
request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode="US",
    maxResults=10,
    videoCategoryId=0,
)
response = request.execute()

# print(response)
# printed to test and is working :)!

video_data = []

for item in response["items"]:
    video_data.append(
        {
            "Title": item["snippet"]["title"],
            "Views": int(item["statistics"]["viewCount"]),
            "Likes": int(item["statistics"].get("likeCount", 0)),
            "Comments": int(item["statistics"].get("commentCount", 0)),
            "CategoryId": item["snippet"]["categoryId"],
        }
    )

video_df = pd.DataFrame(video_data)
print(video_df.head())

plt.figure(figsize=(10, 5))
plt.bar(video_df["Title"], video_df["Likes"], color="blue")
plt.xlabel("Video Title")
plt.tight_layout()
plt.ylabel("Likes")
plt.title("Likes on Trending Videos")
plt.xticks(rotation=45, ha="right")
plt.subplots_adjust(bottom=0.4)
plt.show()

video_id = response["items"][0]["id"]  # Get first video's ID

comment_request = youtube.commentThreads().list(
    part="snippet", videoId=video_id, maxResults=20
)
comment_response = comment_request.execute()

# print(comment_response)

comments = []
sentiments = []

for item in comment_response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    sentiment = TextBlob(comment).sentiment.polarity  # Analyzes sentiment
    comments.append(comment)
    sentiments.append(sentiment)

comment_df = pd.DataFrame({"Comment": comments, "Sentiment": sentiments})
print(comment_df.head())

plt.hist(comment_df["Sentiment"], bins=20, color="green", alpha=0.7)
plt.xlabel("Sentiment Score")
plt.ylabel("Frequency")
plt.title("YouTube Comment Sentiment Analysis")
plt.show()

# category_request = youtube.videoCategories().list(part="snippet", regionCode="US")
# category_response = category_request.execute()  # Use category_request here

# for item in category_response["items"]:
#     title = item["snippet"].get("title", "No title provided")
#     print(title)

video_df


# Extra challenge 1: Find out which category of videos gets the most views (this is out of the maxResult set).
top_5_categories = Counter(video_df["CategoryId"]).most_common()

print("these are the most common 5 categories", top_5_categories)

# Extra challenge 2: Compare comments vs. likes.

sum_of_comments = video_df["Comments"].sum()
sum_of_likes = video_df["Likes"].sum()

print(sum_of_likes)
print(sum_of_comments)

# There are more likes than comments

plt.scatter(video_df["Likes"], video_df["Comments"], alpha=0.7)
plt.xlabel("Likes")
plt.ylabel("Comments")
plt.title("Comparison of Likes vs Comments")
plt.show()

# 3. Find the most commonly used words in YouTube comments.

joined_comment = " ".join(comments)
#  Now I have a long sentence
# print(joined_comment) -- to see if it works as expected (which it did)
# seperate it on each word again into an array

array_words = joined_comment.split()

common_word = Counter(array_words).most_common()
print(common_word)

# Note: I am working with live data so this is changeing all the time
