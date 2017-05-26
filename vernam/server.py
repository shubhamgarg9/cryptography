import socket
import sys

port = 7778
s = socket.socket()
host = socket.gethostname()
s.bind((host,port))
s.listen(5)

print 'server is listening'
conn,addr = s.accept()

#####################################

key = 'zebras'

mapList = []
for i in key:
	mapList.append(i)

for i in range(97,123):
	if chr(i) not in key:
		mapList.append(chr(i))

######################################

message = conn.recv(1024)
ans = ""

for i in message:
	print i
for i in message:
	if ord(i)>96 and ord(i)<123:
		ans = ans + mapList[ord(i)-97]
	else:
		ans = ans + i

print ans
conn.send(ans)

conn.close()
