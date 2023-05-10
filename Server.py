import socket

def server_program():
    # get the host name
    host = socket.gethostname()
    port = 5000     # initiate port no. above 1024

    server_socket = socket.socket() # get instance
    server_socket.bind((host, port))    # bind host addr and port together

    # configure how many clients the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print('Connection from: ' + str(address))

    while True:
        # receive data stream. Will not accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()

        # remove if you do not want server to not quit when client connection closes
        # if not data:
        #     # if data is not received - break
        #     break

        
        print('From connected user: ' + str(data))
        data = input(' -> ')
        conn.send(data.encode())    # send data to the client

    conn.close()    # close the connection

if __name__ == '__main__':
    server_program()