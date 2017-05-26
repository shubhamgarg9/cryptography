#CLIENT
import socket                   # Import socket module
import random
import base64
import hashlib
import sys
 
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 7778                    # Reserve a port for your service.
 
s.connect((host, port))
 
g = input('Enter the value of g : ')
p = input('Enter the value of p : ')
s.send(str(g))
Ack = s.recv(1024)
print Ack
s.send(str(p))
Ack = s.recv(1024)
print Ack
 
print '\nClient Side Calculations:'
a = random.randint(5, 10)
print "a (Client's randomly generated secret): ",a
A = (g**a) % p
print "Server's calculated value (A): ",A,' (g^a) mod p'
 
s.send(str(A))
print("Receiving Value 'B' from server...")
B = int(s.recv(1024))
print("Value 'B' from Server= " + repr(B))
 
print '\nGenerating Key on Client Side:'
keyA=(B**a) % p
print 'KeyA: ',keyA,' (B^a) mod p'
print 'Key Calculated on Client side : \n',hashlib.sha256(str(keyA)).hexdigest()
 
print('\nReceiving Key from Server...')
Key_server = s.recv(1024)
print("Key Recieved from Server = \n" + Key_server)
 
 
msg = s.recv(1024)
print msg
s.close()
print('Connection closed')