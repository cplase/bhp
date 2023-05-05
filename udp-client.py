import socket

target_host = "127.0.0.1"
target_port = 9997

# Create a socket object. The SOCK_DGRAM parameter is used to
# open a UDP socket. The AF_INET parameter is to use a standard
# hostname or IPv4 address.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the target host.
client.sendto(b"AAABBBCCC", (target_host, target_port))

# Receive data from the target host.
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()