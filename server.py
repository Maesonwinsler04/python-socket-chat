import socket
import threading

HOST = '192.168.1.223'
PORT = 9999

def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("Client disconnected")
                break
            print(f"Client: {data.decode()}")
        except:
            print("Connection lost")
            break

def send_messages(conn):
    while True:
        try:
            message = input()
            if message.lower() == 'quit':
                conn.close()
                break
            conn.sendall(message.encode())
        except:
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")
print("Waiting for a connection...\n")

conn, addr = server.accept()
print(f"Connected by {addr}")
print("You can now chat! Type messages and press enter\n")

receive_thread = threading.Thread(target=receive_messages, args=(conn,))
send_thread = threading.Thread(target=send_messages, args=(conn,))

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

print("Chat ended")