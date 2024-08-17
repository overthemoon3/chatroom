# hello 
# this is the client side code uwu

import socket
import threading 
import select
import selectors
import io

def send_messages(client):
    while True:
        # send message 
        msg = input("Message: ")
        if msg != "":
            client.send(msg.encode("utf-8")[:1024])

def receive_messages(client):
    while True:    
        # receive message from the server
        response = client.recv(1024)
        response = response.decode("utf-8")
        if response != "":
            print("recieved", response, "from server")

        # not really gonna program anything for when the
        # server needs to close.
        # if response.lower() == "closed":
        #   break 

    # closing client socket (I know the code will never reach here)
    # client.close()
    # print("Connection to the server closed")



def run_client():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #                           default         default      
    #                           address         socket
    #                           type            type 
              
    # will reach out to the server first 
    server_ip = "127.0.0.1" # localhost, change when deployed 
    server_open_port = 6969

    # establish connection
    client.connect((server_ip, server_open_port))
    
    # create threads for sending and recieving 
    send_thread = threading.Thread(target=send_messages, args=(client,))
    receive_thread = threading.Thread(target=receive_messages, args=(client,))

    # start threads
    send_thread.start()
    receive_thread.start()

    # wait for both to finish (won't happen)
    send_thread.join()
    receive_thread.join()

run_client()
