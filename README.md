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
username = ''
token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID,\ 
                                   SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

# Google Play Music
gmail_address = ''
gmail_password = ''
```

You will be prompted to copy and paste the url that gets redireted to you into the iPython prompt. Once doing this, you can authenticate with Spotify.

To query Spotify-related functions:

```python
spotify = pydpyp.Spotify(token, username)
spotify.get_playlist_names()
spotify.get_playlist_songs('indie')
spotify.get_total_tracks('indie')
```

To query Google Play Music functions:

```python
gm = pydpyp.GooglePlayMusic(gmail_address, gmail_password)
gm.get_playlist_names()
gm.get_playlist_songs('indie')
gm.find_playlist_duplicate_songs()
gm.delete_playlist_duplicate_songs()
```
