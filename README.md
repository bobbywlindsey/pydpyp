# pydpyp

Manage playlists from both Spotify and Google Play Music.


## Install

```
$ pip install git+https://github.com/bobbywlindsey/pydpyp
```

Make sure to also install `spotipy` and `gmusicapi`:

```
$ pip install spotipy
$ pip install gmusicapi
```

To authenticate with Spotify, you first need to register an application (a quick and free process) at [My Applications](https://developer.spotify.com/my-applications/#!/applications).

## Usage

```python
import pydpyp
import spotipy.util as util 
```

Set environment variables for Spotify and Google Play Music in your iPython session:

```python
# Spotify
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = 'http://localhost/'
scope = 'playlist-read-private'
spotify_username = ''
spotify_token = util.prompt_for_user_token(spotify_username, scope, SPOTIPY_CLIENT_ID,\ 
                                   SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

# Google Play Music
gmail_address = ''
gmail_password = ''
```

You will be prompted to copy and paste the url that gets redireted to you into the iPython prompt. Once doing this, you can authenticate with Spotify.

To query Spotify-related functions:

```python
spotify = pydpyp.Spotify(spotify_token, spotify_username)
spotify.get_playlist_names()
spotify.get_playlist_songs('indie')
spotify.get_total_tracks('rock')
```

To query Google Play Music functions:

```python
gm = pydpyp.GooglePlayMusic(gmail_address, gmail_password, spotify_token, spotify_username)
gm.get_playlist_names()
gm.get_playlist_songs('electronic')
gm.find_playlist_duplicate_songs('soundtrack')
gm.delete_playlist_duplicate_songs('rap')
```

You can even copy your Spotify playlist songs over to a Google Play Music playlist.

```python
gm.spotify2google_playlist('spotify_playlist_name', 'google_playlist_name')
```
