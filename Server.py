import socket
from SpotifyService import SpotifyService

class Server:
    """Class for the server connection"""

    def __init__(self):
        self._host = socket.gethostname()
        self._port = 5000   # initiate port no. above 1024
        self._server_socket = socket.socket()
        self._spotify_service = SpotifyService()

        self.run_server()

    def run_server(self):
        """Open the server and process messages from client. """

        self._server_socket.bind((self._host, self._port))    # bind host addr and port together
        
        # configure how many clients the server can listen simultaneously
        self._server_socket.listen(2)

        conn, address = self._server_socket.accept()  # accept new connection
        print('Connection from: ' + str(address))

        while True:
            # receive data stream. Will not accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            action = str(data).split(' ')[0]

            # remove if you do not want server to not quit when client connection closes
            if str(data) == 'xxxSHUTDOWNxxx':
                # if data is not received - break
                break

            if action == 'search_artists':
                artist = str(data).split(' ')[1]
                data = self.return_artists(artist)
            elif action == 'artist_albums':
                artist_id = str(data).split(' ')[1]
                data = self.return_artist_songs(artist_id)
            elif action == 'top_tracks':
                artist_id = str(data).split(' ')[1]
                data = self.return_artist_top_tracks(artist_id)
            elif action == 'link_to_artist':
                artist_id = str(data).split(' ')[1]
                data = self.return_artist_url(artist_id)
            else:
                print('From connected user: ' + str(data))
                # data = input(' -> ')
                data = '-> ' + str(data)
            conn.send(data.encode())    # send data to the client

        conn.close()    # close the connection

    def return_artists(self, artist):
        """Use spotify service to get names of artists based on the search request from client. """

        artist_data = self._spotify_service.search_for_artist(artist)
        artist_string = ''

        # Create string of artist names separated by unique delimeter '?'
        for artist in artist_data:
            artist_string += artist['name'] + '=' + artist['id'] + '?'
        return artist_string
    
    def return_artist_songs(self, artist_id):
        """Use spotify service and artist id to return names of albums. """

        album_data = self._spotify_service.get_songs_by_artist(artist_id)
        album_string = ''

        for album in album_data:
            album_string += album['name'] + '?'
        return album_string
    
    def return_artist_top_tracks(self, artist_id):
        """Use spotify service to get the top tracks of the artist. """

        tracks_data = self._spotify_service.get_artist_top_tracks(artist_id)
        track_string = ''

        for track in tracks_data:
            track_string += track["name"] + '?'
        return track_string
    
    def return_artist_url(self, artist_id):
        """Use spotify service to get the link to the artist's spotify page. """
        
        url = self._spotify_service.get_artist_url(artist_id)
        return url
    
def server_program():
    server = Server()

if __name__ == '__main__':
    server_program()