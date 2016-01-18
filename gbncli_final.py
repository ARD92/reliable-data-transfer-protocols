import socket
import time
import pickle
import random
HOST="192.168.0.9" ## connect to the server
PORT=3500
i=0

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.connect((HOST,PORT))
s.settimeout(15)

s.bind((HOST,PORT))
recfinal=[]
rec_seq_array=[]
B=True
addr=(HOST,3501)
s.sendto('connected!',addr)
print 'connected'
length=s.recv(1024)
length=int(length)
nextseq=0
print 'length of data to be received:',length
while (B==True):
	try:	
		#while C==True:
		rec_seq=s.recv(1024)
		#if recseq:
		#rec_seq=recseq
		print 'receiving seq:',rec_seq
		#order=range(length+1)
		## checking if received seq is in order, else reject the data
		if (int(rec_seq)==nextseq):
			print 'entering loop'
			if  int(rec_seq) not in rec_seq_array:
					rec_seq_array.append(int(rec_seq))
					print 'rec_seq_array:',rec_seq_array
					leng_rec=len(rec_seq_array)
					#print 'data already there'
					#break
					print 'entering loop'
					rec=s.recv(4096)
					print 'received data:',rec
					#rec_rec=pickle.loads(rec)
					#print rec_rec
					#seq_no=int(rec_rec[0])
					#print 'sequence number received:',seq_no
					#data=rec_rec[1]
					#print 'data received:',data
					recfinal.append(rec)
					i=i+1
					print 'length received:',i
					print recfinal	
					nextseq=int(rec_seq)+1
					if i==int(length):
						print 'data received completely'
						B=False
			else:
				data_already=s.recv(1024) ## data is already present and a duplicate is occuring
				#i=i+1
				#print 'lengh received:',i
				#print recfinal
		else:
			print 'data rejected , not in sequence'	
			data_already1=s.recv(1024)	
		
	except socket.timeout:
		print 'time out occured'
		se_seq=random.randrange(0,leng_rec) ## sending seq number randomly from rec end.
		print 'sending seq'
		s.sendto(str(se_seq),addr)
		print 'sent seq',se_seq

s.sendto('exit',addr)
s.close()				
	#except socket.error:
	#	print 'receiving complete'
	#	s.close()

	
	
