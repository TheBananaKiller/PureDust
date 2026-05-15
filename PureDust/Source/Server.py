import socket
import threading

HOST = "0.0.0.0"
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()

clients = []

print("Server running on 55555")

def broadcast(msg, sender):
    for c in clients:
        if c != sender:
            try:
                c.send(msg)
            except:
                c.close()
                clients.remove(c)

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            print(msg.decode())
            broadcast(msg, client)
        except:
            break

    client.close()
    if client in clients:
        clients.remove(client)

while True:
    client, addr = server.accept()
    print("Connected:", addr)
    clients.append(client)
    threading.Thread(target=handle_client, args=(client,)).start()