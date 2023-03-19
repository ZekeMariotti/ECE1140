import socket
import time
ip = "127.0.0.1"
port = 27000
msg = b"hello world"
counter = 0

def readjson:
    

while True:
    print(f'Sending {msg} to {ip}:{port}    Counter:{counter}')
    sock = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM)
    sock.sendto(msg, (ip, port))
    counter+=1
    time.sleep(1)
