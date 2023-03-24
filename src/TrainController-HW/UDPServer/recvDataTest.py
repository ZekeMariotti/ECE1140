import socket
import json
import os
import sys
import time

ip = "127.0.0.1"
port = 27000
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind((ip, port))
print(f'Start listening to {ip}:{port}')





while True:
    data, addr = sock.recvfrom(1024) # buffer
    # print(f"received message: {data}")
    # print(type(data))
    # trainControllerToTrainModel = json.loads(data)
    print(data)

    time.sleep(0.5)

