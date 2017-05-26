import socket
import sys

s = socket.socket()
host = socket.gethostname()
port = 7778
s.connect((host,port))

text = str(raw_input('give the string to cipher it: '))
s.send(text)

#####################################

key = 'zebras'

dic = {}
t = 0
for i in key:
	dic[i] = chr(t+97)
	t = t+1

for i in range(97,123):
	if chr(i) not in key:
		dic[chr(i)] = chr(t+97)
		t = t+1

######################################


rec = s.recv(1024)
print rec

ans = ''
for i in rec:
	if ord(i)>96 and ord(i)<123:
		a = dic[i]
		ans = ans + a
	else:
		ans = ans + i
print ans

s.close()