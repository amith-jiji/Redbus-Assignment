import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = 'utf-8'

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("Server is listening")

    while True:
        conn,addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        filename = conn.recv(SIZE).decode(FORMAT)
        print(f'[RECV] Filename recieved')

        file = open("files/destination/"+filename,'w')
        conn.send("Filename recieved".encode(FORMAT))

        data = conn.recv(SIZE).decode(FORMAT)
        print(f'[RECV] File data recieved')

        file.write(data)
        conn.send("File data recieved".encode(FORMAT))

        file.close()
        conn.close()

        print(f"[DISONNECTION] {addr} disconnected.")