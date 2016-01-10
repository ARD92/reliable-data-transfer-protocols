	
import socket
import time
HOST='localhost'
PORT=3800

##socket creation##
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)


def timer():
	timeout=time.time()+2
	print timeout
	while(time.time()<timeout):
		#print 'waiting for ack'
		if (time.time()>timeout):
			print time.time()	
			break	
			
send_seq='0'
rec_seq='0'

data=raw_input('enter the message to be transmitted')
#length=len(data)
#length=str(length)
##msg to send ###=

B=True
i=0
conn,addr=s.accept()
print 'connected by ', addr
#conn.send(length)
while (B==True):
		
		print 'sender seq:',send_seq
		a=conn.sendall(send_seq)
		print 'sending data'
		b=conn.recv(1024)
		send=str(data[i])
		print 'data_sent:',send
		data_sent=conn.send(send)
		rec_seq=conn.recv(1024)
		
		
		if (rec_seq=='FALSE'):
			print 'timer started, waiting for ack'
			timer()
			conn.send(send)
			rec_seq=conn.recv(1024)
			if str(rec_seq)==str(send_seq):
				i=i+1
				send_seq=str((3+int(send_seq))%2)## bit flipping
			else:
				#i-=1
				send_seq=str((2+int(send_seq))%2)##retaining same bit
				#continue
			if i==len(data):
				B=False
		else:
							
		
			print str(rec_seq)
		
			if str(rec_seq)==str(send_seq):
				i=i+1
				send_seq=str((3+int(send_seq))%2)## bit flipping
			else:
				#i-=1
				send_seq=str((2+int(send_seq))%2)##retaining same bit
				#continue
		 
			if i==len(data):
				B=False
#conn.send('closing connection')
	
		




	
