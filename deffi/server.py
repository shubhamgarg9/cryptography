#SERVER
import socket                   # Import socket module
import random
import base64
import hashlib
import sys
 
port = 7778                     # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
#MY_KEY = "cvwopslweinedvq9fnasdlkfn2"
 
print 'Server listening...'
 
while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    g = int(conn.recv(1024))
    conn.send('g Sent to Server!')
    p = int(conn.recv(1024))
    conn.send('p Sent to Server!')
 
    print 'g: ',g,' (a shared value), n: ',p, ' (a prime number)'
 
    print '\nServer Side Calculations:'
    b = random.randint(10, 20)    
    print "b (Server's randomly generated secret): ",b
    B = (g**b) % p    
    print "Server's calculated value (B): ",B,' (g^b) mod p'    
 
    print("Receiving Value 'A' from client...")
    A = int(conn.recv(1024))
    print("Value 'A' from Client= " + repr(A))
    conn.send(str(B))
 
    print '\nGenerating Key on Server Side:'
    keyB=(A**b) % p
    print 'KeyB: ',keyB,' (A^b) mod p'
    print 'Key Calculated on Server side: \n',hashlib.sha256(str(keyB)).hexdigest()
 
    conn.send(str(hashlib.sha256(str(keyB)).hexdigest()))
    conn.send('\n\nClosing Server connection...')
    conn.close()