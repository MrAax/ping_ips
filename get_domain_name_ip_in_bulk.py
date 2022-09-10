import socket
import time
from time import sleep

start_time = time.time()
#print(dir(socket))
file= open('bulk-domains.txt', 'r')
domain_list=[]

for x in file.readlines():
	domain_list.append(x.rstrip())
	
for y in domain_list:
	soct = socket.gethostbyname(y)
	print(y + ' -> ' + soct)
	#print(y + ' -> ' + socket.gethostbyname(y))
	with open('ip-source.txt', 'a') as f:
		f.write(soct + '\n')
		sleep(1)
		f.close()
end_time=time.time()
finisingTime= end_time - start_time
print(f'Finsing this programe : {finisingTime}')