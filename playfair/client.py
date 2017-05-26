#author - Huzaifa
# https://e...content-available-to-author-only...a.org/wiki/Playfair_cipher
 
import string
 
def gen_table(key):
 
	key = key.lower().replace(' ','').replace('q','')
 
	key_ = []
 
	# https://stackoverflow.com/questions/16060899/alphabet-range-python
	for i in list(key)+list(string.ascii_lowercase):  #removing duplicates while keeping the order
		if i not in key_ and i is not 'q':
			key_.append(i)
 
	# key_ = ['p', 'l', 'a', 'y', 'f', 'i', 'r', 'e', 'x', 'm', 'b', 'c', 'd', 'g', 'h', 'j', 'k', 'n', 'o', 's', 't', 'u', 'v', 'w', 'z']
 
	table = [] #has to be 5x5
 
	for i in xrange(0, 26, 5):
		table.append(key_[i:i+5])		
 
	# table = [['p', 'l', 'a', 'y', 'f'], ['i', 'r', 'e', 'x', 'm'], ['b', 'c', 'd', 'g', 'h'], ['j', 'k', 'n', 'o', 's'], ['t', 'u', 'v', 'w', 'z'], []]
 
	loc = {}  #dictionary loc will store location for each character.
	for x, item in enumerate(table):
		for y, char in enumerate(item):
			loc[char] = [x,y]
 
	# example - {'a': [0, 2], 'c': [2, 1], 'b': [2, 0], 'e': [1, 2], 'd': [2, 2], ... 
 
	return (table, loc)
 
 
def encrypt(msg, key='playfair example', mode='encrypt'):
 
	table,loc = gen_table(key)
 
	msg = msg.lower().replace(' ','').replace('q','') #remove spaces and q
 
	'''
	cant do this shit msg_ = [msg[i:i+2 for i in xrange(0,l en(msg), 2)]
	because a pair cant have same element
	'''
 
	msg_ = ''
 
	j = 0
	for i in msg:
		if j%2==1 and msg_[-1]==i:   #if the last element is same as current 
			msg_+='x' #add extra x; pray that i is not equal to x :(
		j+=1
		msg_+=i
 
	if len(msg_)%2!=0:  #make length equal
		msg_+='x'
 
	# msg = 'Hide the gold in the tree stump'
 
	pairs = [msg_[i:i+2] for i in xrange(0, len(msg_), 2)]
 
	# pairs = ['hi', 'de', 'th', 'eg', 'ol', 'di', 'nt', 'he', 'tr', 'ex', 'es', 'tu', 'mp']
 
	#print pairs
 
	encrypt_msg = []
 
	for pair in pairs:
		l1 = loc[pair[0]]
		l2 = loc[pair[1]]
 
		if l1[0]!=l2[0] and l1[1]!=l2[1]:  #form a rectangle
			y1 = l2[1]
			y2 = l1[1]  #exchange columns
 
			p1 = table[l1[0]][y1]
			p2 = table[l2[0]][y2]
 
		elif l1[1]==l2[1]: #same column
			if mode=='encrypt':
				x1 = (l1[0] + 1)%5 #increment and wrap(if neeeded)
				x2 = (l2[0] + 1)%5
			else:
				x1 = (l1[0] - 1) #decrement and wrap(if neeeded)
				x2 = (l2[0] - 1)
				if x1<0:
					x1+=5
				if x2<0:
					x2+=5
 
			p1 = table[x1][l1[1]]
			p2 = table[x2][l2[1]]
 
		else: #same row
			if mode=='encrypt':
				y1 = (l1[1] + 1)%5 #increment y and wrap(if neeeded)
				y2 = (l2[1] + 1)%5
 
			else:
				y1 = (l1[1] - 1) #decrement and wrap(if neeeded)
				y2 = (l2[1] - 1)
				if y1<0:
					y1+=5
				if y2<0:
					y2+=5
 
			p1 = table[l1[0]][y1]
			p2 = table[l2[0]][y2]
 
		encrypt_msg.append(str(p1+p2))
 
	return ' '.join(encrypt_msg)
	#bm nd zb xd ky be jv dm ui xm mn uv if
	# NOTE- different from wiki because i removed Q
 
 
 
msg = 'Hide the gold in the tree stump'
#msg = raw_input()
enc =  encrypt(msg)
print enc
print encrypt(enc, mode='decrypt')