from gmusicapi import Mobileclient

class GooglePlayMusic():
    """
    parameters:
        gmail_address (str)
        gmail_pasword (str)
    """
    def __init__(self, gmail_address, gmail_password):
        # set environment variables for gmusicapi
        self.api = Mobileclient()
        self.api.login(gmail_address, gmail_password, Mobileclient.FROM_MAC_ADDRESS)

    def get_playlist_names(self):
        playlists = self.api.get_all_playlists()
        return [(playlist['name'], playlist['id']) for playlist in playlists]

    def get_playlist_songs(self, playlist_name):
        playlist_contents = self.api.get_all_user_playlist_contents()
        playlist_songs = []
        for playlist in playlist_contents:
            if playlist['name'] == playlist_name:
                tracks = playlist['tracks']
                for track in tracks:
                    id = track['trackId']
                    playlist_id = track['playlistId']
                    artist = track['track']['artist']
                    title = track['track']['title']
                    playlist_songs.append((id, playlist_id, title, artist))
        return playlist_songs

    # find duplicates in each Google Play Music playlist
    def find_playlist_duplicate_songs(self, playlist_name):
        songs = google_get_playlist_songs(playlist_name)
        song_names_and_artists = [(each[2], each[3]) for each in songs]
        return set([song for song in song_names_and_artists if song_names_and_artists.count(song) > 1])

    def delete_playlist_duplicate_songs(self, playlist_name):
        songs = get_playlist_songs(playlist_name)
        song_names_and_artists = [(each[2], each[3]) for each in songs]
        duplicate_songs = list(set([song for song in song_names_and_artists if song_names_and_artists.count(song) > 1]))
        # TODO: duplicate_songs_ids don't have just one id for each song, but should
        duplicate_songs_ids = [song[0] for song in songs if (song[2], song[3]) in duplicate_songs]
        self.api.delete_songs(duplicate_songs_ids)

    def spotify2google_playlist(self, spotify_playlist_name, google_playlist_name):
        google_playlists = google_get_playlist_names()
        for each in google_playlists:
            if each[0] == google_playlist_name:
                playlist_id = each[1]
        spot_songs = spot_get_playlist_songs(spotify_playlist_name)
        spot_songs = [' '.join(each) for each in spot_songs]
        songs_to_add = []
        for spot_song in spot_songs:
            search = self.api.search(spot_song, max_results=1)
            try:
                song_id = search['song_hits'][0]['track']['storeId']
                songs_to_add.append(song_id)
            except:
                print("Trouble searching song:", spot_song)
        self.api.add_songs_to_playlist(playlist_id, songs_to_add)

