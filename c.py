import socket
c = socket.socket()
c.connect(("localhost",7474))
print(c.recv(1024).decode())  
message = input("antolina to  ")
c.send(bytes(message, "utf-8"))
c.close()
