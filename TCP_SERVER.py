import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

print("[*] Listening on %s:%d" % (bind_ip, bind_port))

# this is our client-handling thread
def handle_client(client_socket: socket.socket):
    # print out what the client sends
    request = client_socket.recv(1024)
    print("[*] Received: %s" % request)
    # send back a packet
    client_socket.send(b"ACK!")
    client_socket.close()

server.listen(5)

while True:
    client_socket, addr = server.accept()
    print("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))
    # spin up a thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()