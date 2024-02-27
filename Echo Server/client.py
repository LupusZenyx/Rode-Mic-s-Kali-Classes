import socket

def echo_client(host, port, message):
    with socket.socket() as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode())

        received_data = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            received_data += data
        
        print("Received:", received_data.decode())

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000
    message = "Bing Bong, der Server ist tot!"
    
    echo_client(host, port, message)
