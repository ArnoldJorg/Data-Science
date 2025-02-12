import os

import matplotlib.pyplot as plt
import pandas as pd
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

spotify_id = os.getenv("SPOTIPY_CLIENT_ID")
spotify_secret = os.getenv("SPOTIPY_CLIENT_SECRET_NAME")

# Set up authentication
client_credentials_manager = SpotifyClientCredentials(
    client_id=spotify_id, client_secret=spotify_secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []
images = []

for i in range(0, 1000, 50):
    track_results = sp.search(q="year:2021", type="track", limit=50, offset=i)
    for t in track_results["tracks"]["items"]:
        artist_name.append(t["artists"][0]["name"])
        track_name.append(t["name"])
        track_id.append(t["id"])
        popularity.append(t["popularity"])
        images.append(t["album"]["images"][0]["url"])

print(artist_name)
