# chatroom

Notes: 

- use Python
    - Specifically because Python has a socket library (select) that allows us to have each host listen and send without ending the connection.
- GitHub repo:
- select() function for the server and client because they need to both continuously listen and send

## Client Functions
- elaborated in client.py

## Server Functions
- elaborated in server.py

# Milestones:

## Let it work on just 1 client.

### Goal 1: the client sends a message to the server

- [DONE]  Let the server accept and listen to connections from the client
- [DONE]  Let the client send a connection request to the server
    - [NO, NOT NEEDED]  huh how do we do that? do we need IP related stuff if it’s just on my laptop
- [DONE]  Once the connection is established, let the client send a message to the server
- [DONE]  Display the message on the server side

### Goal 2: the client is able to display a message from the server

- [DONE]  send connection requests to new ports on the client side??????
- [DONE]  let the server send the received message as a broadcast (through all connected ports *including* the port from which the message was sent)
- [DONE]  let the client accept that message and display it on their terminal

## let it work on multiple clients

- [DONE]  let the server accept connections from multiple hosts
- [DONE]  and be able to send information to multiple hosts (should already be taken care of)
- [DONE]  [OPTIONAL]: MAKE IT MULTITHREADED?

## beyond: create some kind of logout functionality 

## Sources:

https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python

https://docs.python.org/3/howto/sockets.html#socket-programming-howto

https://docs.python.org/3/library/socket.html#socket.socket

https://docs.python.org/3/library/selectors.html#module-selectors

https://docs.python.org/3/library/io.html#io.IOBase.fileno

https://docs.python.org/3/library/threading.html

https://www.geeksforgeeks.org/socket-programming-multi-threading-python/

