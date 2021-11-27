import socket
s = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)
s.bind("test.soc")
s.listen()
con, addr = s.accept() # addr is empty string with AF_UNIX
while True:
	data = con.recv(1024)
	if not data: break
	print(data.decode('utf-8'))
