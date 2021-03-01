import spotipy
from spotipy.oauth2 import SpotifyOAuth


YOUR_USER_NAME = ''
YOUR_CLIENT_ID = ''
YOUR_CLIENT_SECRET = ''


def get_liked_tracks():
    count = 1
    artists_list = []

    while count < 700:
        SPOTIPY_CLIENT_ID = YOUR_USER_NAME
        SPOTIPY_CLIENT_SECRET = YOUR_CLIENT_ID

        
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                    client_secret=SPOTIPY_CLIENT_SECRET,
                                                    redirect_uri= "http://127.0.0.1:8000/spotify/",
                                                    username=YOUR_USER_NAME,
                                                    scope="user-library-read"))

        results = sp.current_user_saved_tracks(offset=count)
        count += 20

        for item in results['items']:
            artists_list.append(item['track']['album']['artists'][0]['name'])

    artists_list = set(artists_list)
    
    return(artists_list)
        
