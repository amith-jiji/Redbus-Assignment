import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP,PORT)
FORMAT = 'utf-8'
SIZE = 1024

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)

    filename = "test.csv"

    file = open("files/source/"+filename,'r')
    data = file.read()

    client.send(filename.encode(FORMAT))

    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER] {msg}")
    
    client.send(data.encode(FORMAT))

    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER] {msg}")

    file.close()
    client.close()