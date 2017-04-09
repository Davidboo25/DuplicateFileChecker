import socket

# Local Host
TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 1024

inputFolder = input("Please enter in a folder to be searched: ")

MESSAGE = inputFolder

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# Encode the data so that it is able to be passed over the server.
s.send(MESSAGE.encode())
print("Successfully sent data to the server:", MESSAGE)
print()

data = s.recv(BUFFER_SIZE)
s.close()

# Print the data that was returned from the server.
print(data.decode())