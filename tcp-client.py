import re
import socket
import sys

# Regex pattern to verify domain.

domain_regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" \
                + "+[A-Za-z]{2,6}"
compile_regex = re.compile(domain_regex)

# Invalid input counter.

x = 0

# Ask user for domain input and verify input. Three wrong attempts
# causes the program to quit.

while x < 3:
    target_host = input("Enter victim host (ex: www.google.com): ")
    if(re.search(compile_regex, target_host)):
        break
    x += 1
    print("Invalid victim host!")

if x >= 3:
    sys.exit("Too many invalid attempts! Quitting!")

# Reset invalid input counter.

x = 0

# Ask user for port number and verify input. Three wrong attempts
# causes the program to quit.

while x < 3:
    target_port = input("Enter victim port (ex: 80): ")
    target_port = int(target_port)
    if (target_port >= 1 and target_port <= 65535):
        break
    x += 1
    print("Invalid victim port!")

if x >= 3:
    sys.exit("Too many invalid attempts! Quitting!")

# Create a socket object.
# The AF_INET parameter indicates the use of an IPv4 address or
# host name. The SOCK_STREAM parameter indicates the use of TCP.

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(3)
        # Connect the client.
        try:
            client.connect((target_host, target_port))
            # Send HTTP GET request.
            client.send(b"GET / HTTP/1.1\r\nHost: " + \
                        bytes(target_host, 'utf-8') + b"\r\n\r\n")
            # Receive HTTP response.
            try:
                response = client.recv(4096)
            except:
                sys.exit("Connection timed out! Quitting!")
        except:
            sys.exit("Unable to connect to the client! Quitting!")
except:
    sys.exit("Unable to open socket! Quitting!")

print(response.decode())