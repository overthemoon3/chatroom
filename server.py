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

    print(response)
    for i in list_of_open_sockets:
        if i != connection:
            i.send(response.encode("utf-8")[:1024])

server_ip = "127.0.0.1" # localhost, change when deployed 
server_open_port = 6969

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
