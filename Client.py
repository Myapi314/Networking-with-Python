import socket
import tkinter as tk
import customtkinter as ctk
import webbrowser

# Global variables for row numbers
row_artist = 0
row_msg = row_artist + 1
row_close = row_msg + 2

class Client:
    """Class for the client connection"""

    def __init__(self):
          self._root = ctk.CTk()
          self._host = socket.gethostname()
          self._port = 5000
          self._client_socket = socket.socket()
          self._message = tk.StringVar()
          self._artist_name = tk.StringVar()
          self._msg_cnt = 0

          self._new_window = None

          self.open_client()

    def open_client(self):
        """Setup connection and open GUI"""

        # Connect client socket
        self._client_socket.connect((self._host, self._port))

        # Run the GUI
        self.setup_gui()
        self._root.mainloop()

    def setup_gui(self):
        """Settings and widgets for main window"""

         # Setup window
        self._root.geometry('700x500')
        # self._root.title = 'Client Side Service'

        # custom tkinter button
        btn_close = ctk.CTkButton(self._root, text="Close Connection", width=25, fg_color='red', command=self.close_client)

        # Artist search widgets
        btn_search_artists = ctk.CTkButton(self._root, text="Find Artist", command=self.open_spotify_response)
        ent_artist = tk.Entry(self._root, textvariable=self._artist_name, width=50)
        lbl_artist = ctk.CTkLabel(self._root, text="Search for Artist: ")
        
        # Simple messaging widgets
        lbl_msg = ctk.CTkLabel(self._root, text='Message')
        ent_msg = tk.Entry(self._root, textvariable=self._message, width=50)
        btn_send = ctk.CTkButton(self._root, text='Send Message', command=self.send_message)

        # Arrange widgets
        lbl_artist.grid(column=0, row=row_artist, columnspan=2, padx=30)
        ent_artist.grid(column=2, columnspan=2, row=row_artist)
        btn_search_artists.grid(column=4, row=row_artist)
        btn_close.grid(column=4, row=row_close, rowspan=2)
        lbl_msg.grid(column=0, row=row_msg, columnspan=2)
        ent_msg.grid(column=2, columnspan=2, row=row_msg)
        btn_send.grid(column=4, row=row_msg, padx=25, sticky='e')


    def send_message(self):
        """Use the entry box to send messages to the server. """
        # Get the message string
        message = self._message.get()

        # Encode and send the message to the server
        self._client_socket.send(message.encode())

        # Decode message received from server
        data = self._client_socket.recv(1024).decode()

        # Reset the label to blank, ready to send new message
        self._message.set('')

        # Create labels to display in gui the messages sent/recvd
        lbl_sent_msg = tk.Label(self._root, text='You sent: ' + message, justify='left')
        lbl_rx_msg = tk.Label(self._root, text='Received back from server: ' + data)

        # Arrange the messages dynamically
        self._msg_cnt += 1
        lbl_sent_msg.grid(column=0, columnspan=2, row=row_msg + self._msg_cnt, sticky='w', padx=15)
        self._msg_cnt += 1
        lbl_rx_msg.grid(column=0, columnspan=2, row=row_msg + self._msg_cnt, sticky='w', padx=30)

    def open_spotify_response(self):
        """Open a new window with the response message from server. """

        data = ''
        artist_name = ''

        # Only open a new window and send the search key if there is not currently a window open.
        if self._new_window is None or not self._new_window.winfo_exists():
            self._new_window = ctk.CTkToplevel()
        else:
            self.clear_response_window()
        
        # Window settings
        self._new_window.focus()
        self._new_window.geometry("700x700")
        
        # Get the search parameter
        artist_name = self._artist_name.get()

        # Use to send request message
        data = self.send_spotify_request(message="search_artists " + artist_name)

        # Split the string of names into an array
        artist_names = data.split('?')

        # Iterate through and add them as labels to window
        for i in range(len(artist_names) - 1):

            def show_artist_details(artist=artist_names[i]):
                """ Callback for each artist available from search. """

                self.clear_response_window()
                
                artist_id = artist.split('=')[1]
                artist_name = artist.split('=')[0]

                # Widgets for specific artist
                lbl_artist = ctk.CTkLabel(self._new_window, text="Find more on " + artist_name, height=20)
                btn_album = ctk.CTkButton(self._new_window, text="Find Albums", fg_color='green', 
                                          command=lambda: self.get_artist_data(message="artist_albums " + artist_id))
                btn_top_tracks = ctk.CTkButton(self._new_window, text="Top Tracks", fg_color='green', 
                                               command=lambda: self.get_artist_data(message="top_tracks " + artist_id))
                btn_spotify_url = ctk.CTkButton(self._new_window, text="Link to their Spotify", fg_color='green',
                                                command= lambda: webbrowser.open(self.send_spotify_request(message="link_to_artist " + artist_id)))
                btn_back = ctk.CTkButton(self._new_window, text="Back to Artists", command=self.open_spotify_response)
                btn_clear = ctk.CTkButton(self._new_window, text="Clear Response", fg_color='green',
                                          command=lambda: show_artist_details(artist))
                # Arrange widgets
                lbl_artist.grid(column=0, row=0)
                btn_album.grid(column=0, row=2)
                btn_top_tracks.grid(column=0, row=3)
                btn_spotify_url.grid(column=0, row=4)
                btn_back.grid(column=0, row=1)
                btn_clear.grid(column=0, row=5)
            
            # Each artist from search is a button that allows user to view more
            new_button = ctk.CTkButton(self._new_window, text=artist_names[i].split('=')[0], command=show_artist_details)
            new_button.grid(column=0, row=i+2, padx=30)
        
        # Title label
        lbl_title = ctk.CTkLabel(self._new_window, text="Results for searching \"" + artist_name + "\"", height=20)
        lbl_title.grid(column=0, row=0)

        # Back to main Window button
        btn_close = ctk.CTkButton(self._new_window, text="Back to Main", fg_color='green',
                                  command=self.back_to_main)
        btn_close.grid(column=0, row=1)

    def back_to_main(self):
        """Callback function for closing the spotify response window and resetting the artist name entry box. """
        self._artist_name.set('') 
        self._new_window.destroy()
    
    def get_artist_data(self, message):
        """Sort through data from response that is a list of names. """
        data = self.send_spotify_request(message)
        names = data.split('?')

        # Create labels of data returned from the response
        for i in range(len(names) - 1):
            new_label = ctk.CTkLabel(self._new_window, text=names[i], justify='left')
            new_label.grid(column=1, row=i+2, columnspan=3, padx=25, pady=0) 

    def clear_response_window(self):
        """Clear the spotify response window. """
        for widget in self._new_window.winfo_children():
            widget.destroy()

    def send_spotify_request(self, message):
        """Send request with a message that will result in specific spotify requests. """
        self._client_socket.send(message.encode())
        data = self._client_socket.recv(1024).decode()
        return data

    def close_client(self):
        """Close the connection for both client and server and close the GUI. """

        # Send unique message for server to close
        exit_status = 'xxxSHUTDOWNxxx'
        self._client_socket.send(exit_status.encode())

        # Close GUI
        self._root.destroy()

        # Cclose client connection
        self._client_socket.close()   


def main_client_program():
    client = Client()

if __name__ == '__main__':
    main_client_program()