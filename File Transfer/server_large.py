import socket
import tqdm
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 4455

BUFFER_SIZE = 4096

s = socket.socket()


s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"Listening {SERVER_HOST}:{SERVER_PORT}")

conn, address = s.accept() 

print(f"{address} is connected.")

received = conn.recv(BUFFER_SIZE).decode()
filename, filesize = received.split('_')

filename = os.path.basename(filename)
filepath = "destination/"+filename

filesize = int(filesize)

progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filepath, "wb") as f:
    while True:

        bytes_read = conn.recv(BUFFER_SIZE)
        if not bytes_read:    
            break

        f.write(bytes_read)
        
        progress.update(len(bytes_read))


conn.close()

s.close()