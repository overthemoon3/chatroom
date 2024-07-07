# hello
# this is server side code uwu 

import socket
import select
import selectors
import io


# create a socket object 
#(use sock.listen(100)), set setblocking to FALSE

server_ip = "127.0.0.1" # localhost, change when deployed 
server_open_port = 6969

# create a GLOBAL list which initially just contains the fileno for the socket object of the server 

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

