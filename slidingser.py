import socket
import time
import pickle

HOST="192.168.0.9"
PORT=3501

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
s.settimeout(20)
new=s.recv(1024)
print new
def timer():
	time_out=time.time()+2
	print time_out
	while (time.time()<time_out):
		if time.time() > time_out:
			print time.time()
			break
	
data=raw_input('enter data to be txd')
length=len(data)
addr=(HOST,3500)
s.sendto(str(length),addr)
window=8## max window size through which frames can be sent without an acknowledgement
print 'initial window:',window
B=True
seq_no=1
base=4
print 'initial base:',base
i=0
recfinal=[]


## calculating cumulative sum to check if data sent == data received , else calculate and request to resend only tat particular data
def cumsum():
	global csum
	csum=0
	for num in recfinal:
		csum=csum+int(num)
		#print csum

#conn,addr=s.recvfrom(1024)
#print 'connected by:', addr

while (B==True):
	if(seq_no<window):
		seq_no=i
		se_no=s.sendto(str(seq_no),addr)
		print 'seq_no:',seq_no
		packet=(data[i])
		recfinal.append(int(seq_no))
		cumsum()
		
		#pack_new=pickle.dumps(packet)
		#print packet
		#data_send=s.sendto(pack_new,addr)
		data_send=s.sendto(packet,addr)
		print 'packet sent:'
		print 'cumulative sum of seq sent:',csum
		#s.sendto(csum,addr)
		timer()
		try:
			if seq_no > base:
				#timer()
				#s.sendto(str(csum),addr)
				print 'waiting for ack to be received, cannot transmit unless ack received'
				#rec=s.recv(1024)
				#print 'received seq num',rec
				datachk=s.recv(1024)
				if datachk=='data_check':
					s.sendto(str(csum),addr)
				reco=s.recv(1024)
				if reco=='continue':
					rec=s.recv(1024)
					print ' ack received, sending next data '
					base=base+int(rec)
					window=window+int(rec)
					print 'new base is:',base
					print 'new window is:',window
				else:
					resend=s.recv(1024)
					print 'resend data bearing sequence no:',resend
					se_no=s.sendto(str(seq_no),addr)
					print 'seq_no:',seq_no
					packet=(data[i])
					#pack_new=pickle.dumps(packet)
					print 'packet:',packet
					#data_send=s.sendto(pack_new,addr)
					data_send=s.sendto(packet,addr)
			
		except socket.timeout:
			
			print 'timeout, resending data'
			se_no=s.sendto(str(seq_no),addr)
			print 'seq_no:',seq_no
			packet=(data[i])
			#pack_new=pickle.dumps(packet)
			print 'packet:',packet
			#data_send=s.sendto(pack_new,addr)
			data_send=s.sendto(packet,addr)
			#print 'packet sent:',data_send
			timer()
	seq_no=seq_no+1
	i=i+1
	if seq_no==int(length):
		B=False
print 'connection closed'	
				
	
