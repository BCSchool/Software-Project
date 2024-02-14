import os
import base64
from requests import post

client_id = os.environ.get('SPOTIFY_CLIENT_KEY')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_base64), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headerrs=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token