import socket
import tqdm
import os

BUFFER_SIZE = 4096

host = "192.168.43.250"

port = 4455

filename = "test.txt"
filepath = "files/source/"+filename

filesize = os.path.getsize(filepath)

s = socket.socket()

print(f"Connecting to {host}:{port}")
s.connect((host, port))
print("Connected")

s.send(f"{filename}_{filesize}".encode())

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filepath, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
       
        s.sendall(bytes_read)
 
        progress.update(len(bytes_read))

s.close()