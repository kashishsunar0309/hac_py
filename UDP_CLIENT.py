import socket

target_host = "127.0.0.1"   # or any server IP
target_port = 9999          # example port

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data (must be bytes)
client.sendto(b"AAABBBCCC", (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print("Received from server:", data.decode())
