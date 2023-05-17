import socket
import tkinter as tk
import customtkinter as ctk

# Global variables for row numbers
row_artist = 0
row_close = row_artist + 1
row_msg = row_close + 2

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
        self._root.geometry('500x500')
        # self._root.title = 'Client Side Service'

        # custom tkinter button
        btn_close = ctk.CTkButton(master=self._root, text="Close", width=25, command=self.close_client)

        # Artist search widgets
        btn_search_artists = ctk.CTkButton(master=self._root, text="Send Request", command=self.open_spotify_response)
        ent_artist = tk.Entry(self._root, textvariable=self._artist_name, width=50)
        lbl_artist = tk.Label(self._root, text="Search for Artist: ")
        
        # Simple messaging widgets
        lbl_msg = tk.Label(self._root, text='Message')
        ent_msg = tk.Entry(self._root, textvariable=self._message, width=50)
        btn_send = tk.Button(self._root, text='Send Message', command=self.send_message)


        # Arrange widgets
        lbl_artist.grid(column=0, row=row_artist)
        ent_artist.grid(column=1, columnspan=2, row=row_artist)
        btn_search_artists.grid(column=3, row=row_artist)
        btn_close.grid(column=0, columnspan=4, row=row_close, rowspan=2)
        lbl_msg.grid(column=0, row=row_msg)
        ent_msg.grid(column=1, columnspan=2, row=row_msg)
        btn_send.grid(column=3, row=row_msg, padx=25, sticky='e')


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
        lbl_rx_msg = tk.Label(self._root, text='Received from server: ' + data)

        # Arrange the messages dynamically
        self._msg_cnt += 1
        lbl_sent_msg.grid(column=0, columnspan=2, row=row_msg + self._msg_cnt, sticky='w', padx=15)
        self._msg_cnt += 1
        lbl_rx_msg.grid(column=0, columnspan=2, row=row_msg + self._msg_cnt, sticky='w', padx=30)

    def open_spotify_response(self):
        """Open a new window with the response message from server. """

        data = ''

        # Only open a new window and send the search key if there is not currently a window open.
        if self._new_window is None or not self._new_window.winfo_exists():
            self._new_window = ctk.CTkToplevel()
            artist_name = self._artist_name.get()
            self._artist_name.set('')
            message = "search_artists " + artist_name

            # Encode and send the message to the server
            self._client_socket.send(message.encode())

            # Decode message received from server
            data = self._client_socket.recv(1024).decode()

        self._new_window.focus()
        self._new_window.geometry("500x500")

        # Split the string of names into an array
        artist_names = data.split('?')

        # Iterate through and add them as labels to window
        for i in range(len(artist_names)):
            new_label = tk.Label(self._new_window, text=artist_names[i], justify='left')
            new_label.grid(column=0, row=i+1)
        
        # Title label
        lbl_title = tk.Label(self._new_window, text="Spotify Response")

        lbl_title.grid(column=0, row=0)
        

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