import socket
import sys

port = 7778
s = socket.socket()
host = socket.gethostname()
s.bind((host,port))
s.listen(5)

print 'server is listening'
conn,addr = s.accept()


def get_order(key):
	out = [i+1 for j in key for i,v in enumerate(sorted(list(key))) if j==v]
	return out

def decrypt(msg, key='HACK'):

	n = len(key)
	clen = len(msg)/n
	chars = list(msg) 
	
	key_ = get_order(key)
	matrix = [[None]*n for i in xrange(clen)]
	
	for i in xrange(n):
		cno = key_[i] - 1  
		col = chars[cno*clen:(cno+1)*clen]  
		
		for rno, item in enumerate(col):
			matrix[rno][i] = item   

	original_msg = ''.join([''.join(item) for item in matrix])
	
	return original_msg.replace('_', ' ')


message = conn.recv(1024)
key = raw_input('enter the key: ')
ans = decrypt(message,key)
print ans

conn.close()