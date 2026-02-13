import socket
import threading

HOST = '192.168.1.223'
PORT = 9999

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Server disconnected")
                break
            print(f"Server: {data.decode()}")
        except:
            print("Connection lost")
            break

def send_messages(sock):
    while True:
        try:
            message = input()
            if message.lower() == 'quit':
                sock.close()
                break
            sock.sendall(message.encode())
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT}")
print("You can now chat! Type messages and press enter\n")

receive_thread = threading.Thread(target=receive_messages, args=(client,))
send_thread = threading.Thread(target=send_messages, args=(client,))

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

print("Disconnected")