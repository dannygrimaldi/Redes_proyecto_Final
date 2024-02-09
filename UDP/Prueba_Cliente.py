import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    client.connect(("14:7d:da:9b:18:e0", 4))
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
except OSError as e:
    print(f"Error: {e}")
finally:
    client.close()
