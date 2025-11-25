import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("localhost",7774))
print("she is ready")

while True:

	data,addr= s.recvfrom(1024)
	print("Joshua: ",data.decode())
	
	