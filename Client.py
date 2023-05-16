import socket
import tkinter as tk
import customtkinter as ctk

class Client:
    """Class for the client connection"""

    def __init__(self):
          self._root = ctk.CTk()
          self._host = socket.gethostname()
          self._port = 5000
          self._client_socket = socket.socket()
          self._message = tk.StringVar()
          self._msg_cnt = 0

          self.open_client()

    def open_client(self):
        # Connect client socket
        self._client_socket.connect((self._host, self._port))

        # Run the GUI
        self.setup_gui()
        self._root.mainloop()

    def setup_gui(self):
         # Setup window
        self._root.geometry('500x500')
        self._root.title = 'Client Side Service'

        # custom tkinter button
        btn_close = ctk.CTkButton(master=self._root, text="Close", width=25, command=self.close_client)
        
        # Simple messaging widgets
        lbl_msg = tk.Label(self._root, text='Message')
        ent_msg = tk.Entry(self._root, textvariable=self._message, width=50)
        btn_send = tk.Button(self._root, text='Send Message', command=self.send_message)


        # Arrange widgets
        btn_close.grid(column=0, columnspan=4, row=0, rowspan=2)
        lbl_msg.grid(column=0, row=2)
        ent_msg.grid(column=1, columnspan=2, row=2)
        btn_send.grid(column=3, row=2, padx=25, sticky='e')


    def send_message(self):
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
        lbl_sent_msg.grid(column=0, columnspan=2, row=2 + self._msg_cnt, sticky='w', padx=15)
        self._msg_cnt += 1
        lbl_rx_msg.grid(column=0, columnspan=2, row=2 + self._msg_cnt, sticky='w', padx=30)

    def close_client(self):
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