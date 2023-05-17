from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

class SpotifyService:
    """Class for methods to make calls to Spotify API"""

    def __init__(self):
        load_dotenv()
        self._client_id = os.getenv("CLIENT_ID")
        self._client_secret = os.getenv("CLIENT_SECRET")
        self._domain = 'https://api.spotify.com'
        self._token = self.get_token()

    def get_token(self):
        """Returns the authorization token necessary to make calls to the Spotify API"""

        # Base64 encoding of the auth string
        auth_string = self._client_id + ":" + self._client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        # URL for the request endpoint 
        url = 'https://accounts.spotify.com/api/token'

        # Headers for the post request
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}

        # token parsed from the response of the post request
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result['access_token']
        return token
    
    def get_auth_header(self):
        """Returns authorization header for other calls"""
        return{
            "Authorization": "Bearer " + self._token
        }
    
    def search_for_artist(self, artist_name):
        """GET request for searching an artist name. Returns data for first artist found."""

        # Build the request parameters
        base_url = self._domain + '/v1/search'
        headers = self.get_auth_header()
        query = f'?q={artist_name}&type=artist&limit=10'  #artist,track for either or
        query_url = base_url + query

        # Send the get request
        result = get(query_url, headers=headers)

        # Load as JSON data and parse for the artists returned
        json_res = json.loads(result.content)
        artists_found = json_res["artists"]["items"]

        # Handle when there are no artists returned
        if len(artists_found) == 0:
            print("No artist found")
            return None
        
        # Return the first artist in array
        return artists_found

    def get_songs_by_artist(self, artist):
        """Return the albums by an artist"""

        # Search for the artist ID
        artist_id = self.search_for_artist(artist)[0]["id"]

        # Set up request parameters
        base_url = self._domain + '/v1/artists/' + artist_id + '/albums'
        headers = self.get_auth_header()

        query_url = base_url + ''   # Additional optional parameters can be added see docs

        # Send the GET request
        result = get(query_url, headers=headers)

        # Load as JSON data and parse for the albums
        json_res = json.loads(result.content)
        albums = json_res['items']

        print(albums[0]['name'])


def main():
    spotifyService = SpotifyService()
    # print(spotifyService.get_token())
    print(spotifyService.search_for_artist(''))
    # spotifyService.get_songs_by_artist('Taylor Swift')

if __name__=='__main__':
    main()
    