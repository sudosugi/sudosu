import socket
s = socket.socket()
s.bind(("localhost",7474))
s.listen(3)
print("Sherlin is waiting")
while True:
    c, addr = s.accept()
    print("Connected to ", addr)

    c.send(bytes("Welcome joshua, enter your love","utf-8"))

    msg = c.recv(1024).decode()
    print("Client says:", msg)

    c.close()
