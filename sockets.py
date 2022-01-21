import socket

ip = socket.gethostbyname('247ctf.com')
print(ip)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the transport mechanism ; use ipv4 | SOCK_STREAM - tcp

s.connect(("247ctf.com", 80))
s.sendall(b"HEAD / HTTP/1.1\r\nHost: 247ctf.com\r\n\r\n")
print(s.recv(1024).decode()) #1024 max data receive at once
s.close()

client = False
server = False
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if server:
	s.bind(("127.0.0.1", port))
	s.listen()
	
	while True:
		connect, addr = s.accept()
		connect.send(b"You made it to the socket!")
		connect.close()

if client:
	s.connect(("127.0.0.1", port))
	print(s.recv(1024))
	s.close()

for port in [22, 80, 139, 443, 445, 8080]:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	result = s.connect_ex(("127.0.0.1", port)) # return error rather than raising an exception; error 0 if success
	if result == 0:
		print("{} is open!".format(port))
	else:
		print("{} is closed!".format(port))
	s.close()



























