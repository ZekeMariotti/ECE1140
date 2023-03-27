#!/usr/bin/env python

import socket
import selectors
import types
import time

#Create a selector for handling multiple clients
sel = selectors.DefaultSelector()


#Change to local IP of server -Future version get this automatically
localIP     = "192.168.0.150"
#Car UDP Port
carPort   = 20001
#Client UDP Port
clientPort = 20002
#Create a UDP Port to listen for new client requests
listenPort = 20003
#UDP Buffer size maybe? Need to check CHK
bufferSize  = 1024

 
#Message to send to deivce, maybe a pairing message to recieve car number? FUT
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

#Create a list of client addresses to send to
clientList = []


# Create 3 datagram sockets, one for car, one for sending to clients, and one for adding new clients
UDPCarSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
listenSocket = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)

# Bind all sockets to address and ip
UDPCarSocket.bind((localIP, carPort))
UDPClientSocket.bind((localIP, clientPort))
listenSocket.bind((localIP,listenPort))

#Add listening socket to selector so it creates an interrupt when it recieves data
sel.register(listenSocket, selectors.EVENT_READ, data=None)

#Add the car socket to the selector
carData = types.SimpleNamespace(type="car", inb=b"")
sel.register(UDPCarSocket, selectors.EVENT_READ, data=carData)

print("UDP server up and listening")

#Function to get new clients
def accept_wrapper(sock):
    #Get message and address from listenSocket
    newClient = sock.recvfrom(bufferSize)
    #If client request is valid, add client to clientList, else produce error
    if newClient[0] == "Add Me":
        clientList.append(newClient[1])
        print(f"Accepted connection from {newClient[1]}")
    else:
        print("Invalid Client Request")

#Function to
def data_handler(key):
    # Get incoming data from the car
    carDataPackage = UDPCarSocket.recvfrom(bufferSize)

    # Extract Message from the car
    carMsg = carDataPackage[0]
    print("Car Data:{}".format(carMsg))

    #Add notes for the socket
    data = key.data
    data.inb += carMsg

    # Add newline to end of car data
    carMsgString = carMsg.decode("utf-8")
    carMsgString += "\n"

    # Encode the car data
    bytesToSend = str.encode(carMsgString)

    for clientAddress in clientList:
        # Sending data to client
        UDPClientSocket.sendto(bytesToSend, clientAddress)


#Main program
try:
    # Listen for incoming datagrams
    while(True):

        #Wait for an event (receiving input from or ready to send output to a socket)
        events = sel.select(timeout=None)
        #Extract key, which holds the socket object and mask which is an event mask of the operations that are ready
        for key, mask in events:
            #If key.data is none, then the key is the listenPort and we'll call a function to add it to the client list
            if key.data is None:
                print("client request received")
                accept_wrapper(key.fileobj)
            #If key.data is not none, then the event is from the car so run a function to recieve and send out that data
            else:
                data_handler(key)

except KeyboardInterrupt:
    print("Caught Keyboard interrupt, exiting")
finally:
    sel.close()