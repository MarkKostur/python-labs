import socket
import threading

clients = []  

def set_callback(callback):
    global callback_function
    callback_function = callback

def broadcast(message, address):
    for client_socket, addr_client in clients:
        try:
            if addr_client[1] != address[1]:
                client_socket.send(message.encode())
        except socket.error:
            pass

def client_thread(conn, addr):
    global clients
    
    print(f"Connected by {addr}")
    clients.append((conn, addr))
    print('clients', clients)
    while True:
        message = conn.recv(1024).decode()
        if not message:
            break

        broadcast(f"Client {addr} says: {message}", addr)

    
    clients.remove((conn, addr))
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_thread, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
