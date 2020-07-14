"""
Step 1: Log into Youtube
Step 2: Grab our liked videos
Step 3: Create a new playlist
Step 4: Search for the song
Step 5: Add song into new Spotify playlist
"""
import json
import os


import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl
from secrets import spotify_token, spotify_user_id

class CreatePlaylist:
    def __init__(self):
        self.youtube_client = self.get_youtube_client()
        self.all_song_info = {}
    # Step 1: Log into Youtube
    def get_youtube_client(self):
        pass
    # Step 2: Grab our liked videos
    def get_liked_videos(self):
        pass
    # Step 3: Create a new playlist
    def create_playlist(self):
        pass
    # Step 4: Search for the song
    def get_spotify_url(self):
        pass
    # Step 5: Add song into new Spotify playlist
    def add_song_to_playlist(self):
        pass
    