import socket 

def download():

    #Creating the socket passing the ip and port as parameters and trying to connect
    host = "127.0.0.1"
    port = 6000
    mySocket = socket.socket()
    mySocket.connect((host,port))
    #connection established

    mySocket.send("Hello server!".encode())

    filename=mySocket.recv(4096).decode()

    with open(filename, 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = mySocket.recv(4096)
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    print('Successfully get the file')
    mySocket.close()
    print('connection closed')

if __name__ == "__main__":
    download()
