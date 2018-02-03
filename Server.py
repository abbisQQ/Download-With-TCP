import socket

def server():

    port = 6000                  # Reserve a port for your service.
    s = socket.socket()             # Create a socket object
    host = "127.0.0.1"     # Get local machine name
    s.bind((host, port))            # Bind to the port
    s.listen(5)                     # Now wait for client connection.

    print('Server listening....')

    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        data = conn.recv(4096).decode()
        print('Server received', repr(data))
        filename='image.jpg'
        conn.send(filename.encode())
        f = open(filename,'rb')
        l = f.read(4096)
        while (l):
           conn.send(l)
           print('Sent ',repr(l))
           l = f.read(4096)
        f.close()

        print('Done sending')
        conn.send('Thank you for connecting'.encode())
        conn.close()

if __name__ == "__main__":
    server()
