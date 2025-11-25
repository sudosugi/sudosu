import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=input("antolina ")
c.sendto(msg.encode(),("localhost",7774))
