# from Computer Networking Principles Bonaventure
import socket
import sys
hostip = sys.argv[1]
port = int (sys.argv[2])
msg = "Hello World!"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(msg, (hostip, port))