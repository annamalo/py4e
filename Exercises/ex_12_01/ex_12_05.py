# Import socket library
import socket

# Initiate socket after library import
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server and port
mysock.connect(('data.pr4e.org', 80))

# Request (GET) website from server with protocol HTTP/1.0 as byte string (b' / encode)
# Byte string / object is neccesary to send over network
mysock.sendall(b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n')

# Define empty byte string
all_text = b''

while True:
    # Receive data (amount per recieve defined) from socket and add to data variable
    data = mysock.recv(5120)
    if len(data) < 1: break
    # Append received data to byte string variable all_text
    all_text = all_text + data

# Socket connection should be closed to define closure
mysock.close()

# In byte string variable all_text, look for the end of the header (standard HTTP/1.0)
# Search for 2 new lines (\r\n\r\n) as standard HTTP/1.0 between head and text
endhead = all_text.find(b"\r\n\r\n")
# Print tex after header as decoded byte string, i.e. string
print(all_text[endhead:].decode())

# Alternative: Decode before find() and search for \n in string
