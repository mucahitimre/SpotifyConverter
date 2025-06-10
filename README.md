# SpotifyConverter
The app transfers your Spotify library to another music platform. It fetches
liked tracks from Spotify and searches for them on YouTube Music.

## Setup Spotify
The export step uses [Spotipy](https://github.com/spotipy-dev/spotipy) and requires the following environment variables:
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

## Setup YouTube
You must be YouTube authentication and this action easy with the following command: `` ytmusicapi oauth `` this command created `` oauth.json `` file in project root.

## Run
Once Spotify and YouTube authentication are configured you can start the application.

To export your saved tracks from Spotify and create `youtube_search_results.json` run:
```bash
python main.py Ex-Sp
```

Afterwards you can import the results into YouTube Music:
```bash
python main.py Im-You
```



## Packages
- https://github.com/spotipy-dev/spotipy
- https://github.com/sigma67/ytmusicapi
