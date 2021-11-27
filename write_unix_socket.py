import socket
s = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)
s.connect("test.soc")
s.sendall(b'testing\n')
s.sendall(b'1 2 3')
s.shutdown(socket.SHUT_RDWR)
s.close()
