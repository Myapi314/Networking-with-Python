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

            # remove if you do not want server to not quit when client connection closes
            if str(data) == 'xxxSHUTDOWNxxx':
                # if data is not received - break
                break
            if str(data).split(' ')[0] == 'search_artists':
                artist = str(data).split(' ')[1]
                data = self.return_artists(artist)
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
            artist_string += artist['name'] + '?'
        return artist_string
    
def server_program():
    server = Server()

if __name__ == '__main__':
    server_program()