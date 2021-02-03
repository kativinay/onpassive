import socket			 



def client():
    """
    Creating a socket object,
    Make connection to ip(127.0.0.1) and port(12345),
    Receive btyes from socket.recv().
    return message type: bytes
    """
    s = socket.socket()	 
    port = 12345	
    s.connect(('127.0.0.1', port)) 
    print (s.recv(1024) ) 
    s.close()	 
	
client()
