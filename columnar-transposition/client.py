import socket
import sys

s = socket.socket()
host = socket.gethostname()
port = 7778
s.connect((host,port))

def get_order(key):
	out = [i+1 for j in key for i,v in enumerate(sorted(list(key))) if j==v]
	return out

def encrypt(msg, key='HACK'):

	n = len(key)
	msg_ = msg.replace(' ', '_')

	while len(msg_)%n!=0:
		msg_ = msg_ + '_'
	chars = list(msg_)  
	matrix = []
	
	for i in xrange(0, len(chars), n):
		matrix.append(chars[i:i+n])     

 	
	key_ = get_order(key)

	encrypt_msg = [None]*n 

	for i in xrange(n):
		col = [row[i] for row in matrix] 
		encrypt_msg[key_[i] - 1] = col  
	
	final_msg = ''.join([''.join(item) for item in encrypt_msg])

	return final_msg



print 'Enter message'
msg = raw_input()

print 'Enter Key'
key = raw_input()

encrypt_msg = encrypt(msg, key)

print encrypt_msg

s.send(encrypt_msg)
s.close()
