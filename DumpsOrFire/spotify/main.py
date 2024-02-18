import os
import base64
from requests import post, get
import json
from requests import post

client_id = os.environ.get('SPOTIFY_CLIENT_KEY')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

def get_token():
    """ Get Spotify token to access artist and track info """
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_base64), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    """ Search for an artist and return items associated with artist """
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    
    return json_result[0]

def search_for_track(token, track_name):
    """ Search for a track and return items associated with track """
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={track_name}&type=track&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    
    if len(json_result) == 0:
        print("No tracks with this name exists...")
        return None
    
    return json_result[0]

def search_for_playlist(token, playlist_name):
    """ Search for playlist and return items associated with playlist """
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={playlist_name}&type=playlist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["playlists"]["items"]
    
    if len(json_result) == 0:
        print("No playlist with this name exists...")
        return None
    
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    """ Return top tracks from given artist """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result
    
token = get_token()


artist_result = search_for_artist(token, "Denzel Curry")
artist_id = artist_result["id"]
top_tracks = get_songs_by_artist(token, artist_id)

track_result = search_for_track(token, "blinding lights")
track_popularity = track_result["popularity"]

avg_popularity = 0

""" Test for calculating popularity of a playlist
playlist_result = search_for_playlist(token, "Today's Top Hits")

for idx, song in enumerate(playlist_tracks):
    print(f"{idx}. {song["name"]}")
"""


# print(f"{result['name']} Popularity: {track_popularity}")


""" Test: Calculate popularity of an artist's top tracks """
print(f"{artist_result['name']}'s Top Tracks")
print("--------------------------------------------")

for idx, song in enumerate(top_tracks):
  avg_popularity += song["popularity"]

avg_popularity = avg_popularity/10.0

for idx, song in enumerate(top_tracks):
    print(f"{idx+1}. {song['name']}")

print()

print(f"Artist Popularity: {artist_result["popularity"]}")

print(f"{artist_result['name']}'s Top Tracks Popularity Rating: {avg_popularity:.0f}")
    result = post(url, headerrs=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token
