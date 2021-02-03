import socket
import json			 

def api_call():
    """
    Creating a socket object,
    Make connection to host httpbin.org --> it will return new uuid for every get request,
    Receive btyes from socket.recv().
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        host = 'httpbin.org'
        port = 80
        message  = b'GET /uuid HTTP/1.1\r\nHost: httpbin.org\r\n Content-Type:application/json\r\n\r\n\r\n'
        conn.connect((host , port))
        conn.sendall(message)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode()
            print(data)
	
        conn.close()

api_call()