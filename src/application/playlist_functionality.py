
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from application.SpotifyCredentials import SPOTIFY_CLIENT_ID,SPOTIFY_CLIENT_SECRET,SPOTIFY_REDIRECT_URI


class Playlist_Gen:

    def __init__(self,playlist_name,playlist_desc):

        self.username = "21as4yvrgnnnjpzb7qqbcoyva"
        self.scope = "playlist-modify-public"
        self.token = None
        self.spotifyObject = None
        self.playlist_name = playlist_name
        self.playlist_desc = playlist_desc
        #self.create_playlist()

   # def handle_click(self):
      #  self.get_token()
      #  self.create_playlist()

    def get_token(self):
        if self.token == None:
            self.token = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,client_secret=SPOTIFY_CLIENT_SECRET,redirect_uri=SPOTIFY_REDIRECT_URI,scope=self.scope)
        
        self.spotifyObject = spotipy.Spotify(auth_manager= self.token)

    def create_playlist(self):
        
        # this function creates a new playlist to the users spotify library

        #playlist_name = "AI playlist"
        #playlist_desc = "by niko demus"

        self.spotifyObject.user_playlist_create(user=str(self.username),name=str(self.playlist_name),public=True,description=str(self.playlist_desc))
        print(self.playlist_name,self.playlist_desc)

#playlist = Playlist_Gen()

#def __init__(self,username,playlist_name,playlist_desc):

#username: 21as4yvrgnnnjpzb7qqbcoyva