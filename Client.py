import socket

def client_program():
    # get the host name (both code running on same PC)
    host = socket.gethostname()
    port = 5000     # socket server port number

    client_socket = socket.socket() # get instance
    client_socket.connect((host, port)) # connect to server

    message = input(' -> ') # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())    # send message
        data = client_socket.recv(1024).decode()    # receive response

        print('Received from server: ' + data)

        message = input(' -> ') # take input again

    client_socket.close()   # close connection

if __name__ == '__main__':
    client_program()