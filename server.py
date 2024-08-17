# hello
# this is server side code uwu 

import socket
import select
import selectors
import io

selector = selectors.DefaultSelector()

list_of_open_sockets = []


def accept(sock, mask):
    connection, address = sock.accept()
    print('accepted', connection, 'from', address)
    connection.setblocking(False)
    selector.register(connection, selectors.EVENT_READ, read)
    list_of_open_sockets.append(connection)

def read(connection, mask):
    request = connection.recv(1024)
    response = request.decode("utf-8")

        # if request.lower() == 'close' 
        # connection.send("closed".encode("utf-8"))

    print("Recieved", response)
    for i in list_of_open_sockets:
        if i != connection:
            i.send(response.encode("utf-8")[:1024])


    # while True:
    #     request = connection.recv(1024)
    #     request.decode("utf-8")

    #     # if request.lower() == 'close' 
    #     # connection.send("closed".encode("utf-8"))

    #     print("Recieved", request)
    #     response = request.encode("utf-8")
    #     connection.send(response)

    # data = connection.recv(1024)
    # if data:
    #     print('echoing', repr(data), 'to', connection)
    #     connection.send(data)
    # else:
    #     print('closing', connection)
    #     selector.unregister(connection)
    #     connection.close()

server_ip = "127.0.0.1" # localhost, change when deployed 
server_open_port = 6969


# create a GLOBAL list which initially just contains the fileno for the socket object of the server 

# create the server socket object 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_open_port)) # server_ip, port 
server.listen(100)  # tells you how many clients can be put into the queue
                    # before the accept method is called on them
print("Listening on", str(server_ip), "on port", str(server_open_port))
server.setblocking(False)
selector.register(server, selectors.EVENT_READ, accept)


# communication loop 
while True:

    events = selector.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)


# while loop to : 
#   run the select method until the returned list is non-empty 
#   
#   if the returned list is not empty: 
#       if it contains the fileno of the server's socket object,
#           call an 'accept' function because it means someone's tried to connect to it 
#           accept incomming connections 
#           extract that connection's own filedescriptor using client_fd = client_socket.fileno()
#           register that connection using register(fileobj, ...)
#       if there's a fileno that *isn't* the server's socket object, 
#           it means someone tried to send the server a message
#           accept the message and send a response (through all open sockets), just iterate through 
#           the global list 

