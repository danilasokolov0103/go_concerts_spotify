from bandsintown import Client
import json
from get_liked_tracks import get_liked_tracks



client = Client('mybandapp')


artists_names = get_liked_tracks()
concert_list = []

for artist in artists_names:
    try:
        concert = client.artists_events(artist)
    except json.JSONDecodeError : 
        pass
    for i in concert:
        try:
            if i['venue']['location'] == 'Moscow, Russia':
                moscow =  i['venue']['location']
                date = i['datetime']
                club = i['venue']['name']
                concert_list.append(f'{artist} ---- {moscow} ----- {date} ---- {club}')
        except (TypeError):
            pass


for i in concert_list:
    print(i)