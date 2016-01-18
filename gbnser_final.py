import socket
import time
import pickle

HOST="192.168.0.9"
PORT=3501

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
s.settimeout(16)
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

#conn,addr=s.recvfrom(1024)
#print 'connected by:', addr

while (B==True):
	if(seq_no<window):
		seq_no=i
		se_no=s.sendto(str(seq_no),addr)
		print 'seq_no:',seq_no
		packet=(data[i])
		#pack_new=pickle.dumps(packet)
		#print packet
		#data_send=s.sendto(pack_new,addr)
		data_send=s.sendto(packet,addr)
		print 'packet sent:'
		timer()
		try:
			if seq_no > base:
				print 'waiting for ack to be received, cannot transmit unless ack received'
				#sendto('please')
				#print 'sent'
				rec=s.recv(1024)
				print 'received seq num',rec
				if rec:
					print ' ack received, sending next data '
					base=base+int(rec)
					window=window+int(rec)
					print 'new base is:',base
					print 'new window is:',window
			
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
				
	
