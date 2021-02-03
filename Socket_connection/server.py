# first of all import the socket library 
import socket			 


def socket_creation():
    """
    Creating a socket object,
    Binding defalut ip(127.0.0.1) and port(12345),
    listen() make socket into listening.
    accept() waits for incoming connection attempts and blocks until a client tries to connect
    send() will send the message to request server.	
    """
    s = socket.socket()	 
    # declearing a port
    port = 12345				
    s.bind(('', port))	 
    print ("Binded successfully to port: %s" %(port)) 
    s.listen() 
    print ("Iam listening......")
    while True:
        c, addr = s.accept()	 
        print ('Got connection from', addr ) 
        message = 'Thank you for connecting'
        c.send(message.encode()) 
        c.close() 


socket_creation()