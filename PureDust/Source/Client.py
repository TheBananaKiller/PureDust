import socket
import threading
import sys

SERVER_IP = sys.argv[1]  # still passed from LunarCMD
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

name = input("Enter your name: ")

print("Connected to chat.\n")

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            print("Disconnected.")
            client.close()
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    msg = input()
    client.send(f"{name}: {msg}".encode())