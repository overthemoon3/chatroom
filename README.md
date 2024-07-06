# chatroom

Notes: 

- use Python, on Linux
    - Specifically because Python has a socket library that allows us to have each host listen and send without ending the connection.
- GitHub repo:
- select() function for the server and client because they need to both continuously listen and send

## Client Functions
- initialize a listener socket that listens on port 6666
- accept a new connection from the initialized socket
- 

## Server Functions
- initialize a listener socket that listens on port 6666
- accept a new connection from the initialized socket
- 

# Milestones:

## Let it work on just 1 client.

### Goal 1: the client sends a message to the server

- [ ]  Let the server accept and listen to connections from the client
- [ ]  Let the client send a connection request to the server
    - [ ]  huh how do we do that? do we need IP related stuff if it’s just on my laptop
- [ ]  Once the connection is established, let the client send a message to the server
- [ ]  Display the message on the server side

### Goal 2: the client is able to display a message from the server

- [ ]  send connection requests to new ports on the client side??????
- [ ]  let the server send the received message as a broadcast (through all connected ports *including* the port from which the message was sent)
- [ ]  let the client accept that message and display it on their terminal

## let it work on multiple clients

- [ ]  let the server accept connections from multiple hosts
- [ ]  and be able to send information to multiple hosts (should already be taken care of)
- [ ]  [OPTIONAL]: MAKE IT MULTITHREADED?

## Sources:

https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python

https://docs.python.org/3/howto/sockets.html#socket-programming-howto
