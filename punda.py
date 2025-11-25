import socket
import struct 

def main():

	sniffer=socket.socket(socket.AF_NET,socket.SOCK_RAW,socket.IPPROTO_IP)
        	host=socket.gethostbyname(socket.gethostname())
        print("ur ip",host)
        sniffer.bind((host,0))
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        	sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

	print("\n---packet sniffer---")

while True:
	packet,addr= sniffer.recvform(65535)
        ip_header = packet[:20]
	iph = struct.unpack("!BBHHHBBH4s4s",ip_header)

	scr=socket.inet_ntoa(iph[8])
	des=socket.inet_ntoa(iph[9])
	pro=iph[6]

	print("scr ip: ",scr)
	print("des ip: ",des)
	print("protocol: "pro)

if__name__=="_main_":
	main()
	

