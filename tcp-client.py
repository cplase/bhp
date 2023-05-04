import socket

target_host = input("Enter victim host (example: www.google.com): ")
target_port = input("Enter victim port (example: 80): ")

target_port = int(target_port)

# Create a sockt object
# The AF_INET parameter indicates the use of an IPv4 address or
# host name. The SOCK_STREAM parameter indicates the use of TCP.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send HTTP GET request
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive HTTP response
response = client.recv(4096)

print(response.decode())
client.close