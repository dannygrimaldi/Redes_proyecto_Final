import socket
import threading

# Lista para mantener un registro de todos los sockets de clientes conectados
clients = []

def handle_client(client_socket):
    while True:
        try:
            # Recibir mensaje del cliente
            msg = client_socket.recv(1024)
            print(f"Received: {msg}")

            # Reenviar el mensaje a todos los otros clientes
            for client in clients:
                if client is not client_socket:
                    client.send(msg)
        except Exception as e:
            print(f"Error: {e}")
            clients.remove(client_socket)
            client_socket.close()
            break

def server_start():
    server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    server.bind(("14:7d:da:9b:18:e0", 4))
    server.listen(1)
    print("Listening on port 4")

    while True:
        client, addr = server.accept()
        print(f"Accepted connection from: {addr[0]}:{addr[1]}")
        clients.append(client)
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

server_start()