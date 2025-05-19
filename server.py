
import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}
groups = {}

def broadcast(message, sender=None, group=None):
    if group:
        for member in groups.get(group, []):
            if member != sender and member in clients:
                clients[member].send(message.encode())
    else:
        for client in clients.values():
            if client != sender:
                client.send(message.encode())

def handle(client, username):
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg.startswith("/w "):
                target, message = msg[3:].split(" ", 1)
                if target in clients:
                    clients[target].send(f"[Private] {username}: {message}".encode())
            elif msg.startswith("/g "):
                group_name, message = msg[3:].split(" ", 1)
                broadcast(f"[{group_name}] {username}: {message}", sender=username, group=group_name)
            elif msg.startswith("/join "):
                group_name = msg[6:]
                groups.setdefault(group_name, set()).add(username)
                client.send(f"Joined group {group_name}".encode())
            else:
                broadcast(f"{username}: {msg}", sender=username)
        except:
            client.close()
            del clients[username]
            break

def receive():
    print("Server running...")
    while True:
        client, address = server.accept()
        username = client.recv(1024).decode()
        clients[username] = client
        print(f"{username} connected.")
        threading.Thread(target=handle, args=(client, username)).start()

receive()
