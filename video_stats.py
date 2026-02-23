import requests
import json
import os 
from dotenv import load_dotenv
from urllib3 import response

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
for_Handle = "speedsters7200"

def get_playlist_id(): #best practice to wrap up codes
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={for_Handle}&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        channel_items = data['items'][0]
        channel_playlistID = channel_items['contentDetails']['relatedPlaylists']['uploads']
        print(channel_playlistID)
        return channel_playlistID
    except requests.exceptions.RequestException as e:
        raise e #any exception relating to requests will be set to the variable E. then we raise exception E

if __name__ == "__main__": #best practices in python
    #print("get_palylist_id will be executed")
    get_playlist_id()
# else:
    # print("get_playlist_id won't be executed")
