# SpotifyConverter
The app will doing my spotify library transfer to another music platforms

## Setup Spotify
You must do the following configuration install before running, this configuration required for 'spotipy' package: 
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

## Setup YouTube
You must be YouTube authentication and this action easy with the following command: `` ytmusicapi oauth `` this command created `` oauth.json `` file in project root.

## Run
If spotify and another music platform setup is complate you can start the application.

When start the application firstly must gets spotify library:
```
python main.py Ex-Sp
```

Then must be another platform import action start:
- For Youtube:
  ```
  python main.py Im-You
  ```



## Packages
- https://github.com/spotipy-dev/spotipy
- https://github.com/sigma67/ytmusicapi
