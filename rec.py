import socket
import random
import time
HOST='localhost'
PORT=3800
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
recfinal=[]
B=True
retry=0

def timer():
	timeout=time.time()+1
	print timeout
	while (time.time()<timeout):
		if time.time() > timeout:
			print time.time()
			break	
	
while B==True:
	rec_sequence=s.recv(1024)
	print 'rec_seq:',rec_sequence
	ack=s.sendall(str(rec_sequence))
	rec_data=s.recv(1024)
	print 'rec_data:',rec_data
	rand=random.randrange(-1,1,1)
	if (rand>0):
		rec_seq=1
		
	elif (rand<0):
		rec_seq=0
	else: 
		print 'timer started'
		timer() ## dont send ack, wait for the sender to resend data again
		print 'timer ended'
		s.send('FALSE')
		rec_data=s.recv(1024)
		
		rand1=random.uniform(-1,1)
		if rand1>0.5:
			rec_seq=1
		else:
			rec_seq=0

	if str(rec_seq)==str(rec_sequence):
		recfinal.append(rec_data)
		print recfinal,'retries:',retry
	else:
		retry=retry+1
	data_ack=s.sendall(str(rec_seq))
	print data_ack
	print not rec_sequence
	
	if not (rec_sequence): 
		print(not rec_sequence)
		B=False
	
	
print recfinal,'retries:',retry
mess=s.recv(1024)
s.close()
	

