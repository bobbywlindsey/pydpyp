import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


class Spotify:
    """
    parameters:
        token (str)
        username (str)
    """
    def __init__(self, token, username):
        self.sp = spotipy.Spotify(auth=token)
        self.username = username

    def get_playlist_names(self):
        playlists = self.sp.user_playlists(self.username)
        return [playlist['name'] for playlist in playlists['items'] if playlist['owner']['id'] == self.username]

    def get_playlist_songs(self, playlist_name):
        playlists = self.sp.user_playlists(self.username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == self.username and playlist['name'] == playlist_name:
                results = self.sp.user_playlist(self.username, playlist['id'],
                                                fields="tracks,next")
                tracks = results['tracks']
                return self.show_tracks(tracks)

    def show_tracks(self, tracks):
        return [(item['track']['name'], item['track']['artists'][0]['name']) for i, item in enumerate(tracks['items'])]

    def get_total_tracks(self, playlist_name):
        playlists = self.sp.user_playlists(self.username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == self.username and playlist['name'] == playlist_name:
                print('total tracks for', playlist_name, ':', playlist['tracks']['total'])
