import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


def connect_user(scope):
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            redirect_uri="http://localhost:8000/",
            scope=scope,
        )
    )
