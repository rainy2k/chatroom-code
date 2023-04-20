#server.py
import socket
import pyttsx3

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
host = '' # ipv6 address
port = 8890
server.bind((host,port)) #bind server
server.listen(5)

print("[Server] server start")

client, addr = server.accept()
print("[Server] Got Connection from",addr)
client.send("[Server]: This is Server, Hello World :)".encode('UTF-8')) #send data to client

try:
    while True:
        msg = client.recv(1024).decode('UTF-8')
        print("[Client]: ", msg)
        engine = pyttsx3.init()
        engine.say(msg)
        engine.runAndWait()
except KeyboardInterrupt:
    print('[Server] closing...')
    server.close()
    
# python3.10 server.py
# sudo lsof -i:8889 