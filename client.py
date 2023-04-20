#client.py
import socket

client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
host = '' # ipv6 address
port = 8890
client.connect((host,port))

msg = client.recv(1024)
print(msg.decode('UTF-8'))
client.sendall('Client Online ...'.encode('UTF-8'))

try:
    while True:
        word = input("[Client] send your message to server: ")
        client.send(word.encode('UTF-8'))
except KeyboardInterrupt:
    print('[Client] closing...')
    client.close()

# python3.10 client.py