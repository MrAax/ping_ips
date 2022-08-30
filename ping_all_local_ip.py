import subprocess
import platform
import os
import time

def ping(host):
	global parem
	parem = '-n' if platform.system().lower() == 'windows' else '-c'
	command = ['ping', parem, '2', host]
	return subprocess.call(command)
'''
for x in range(0, 256, 1):
  for j in range(0, 256, 1):
  	#print(f'ping : 192.168.{x}.{j}')
  	host = f'192.168.{x}.{j}'
  	print(ping(host))
'''

'''
while True:
	#host = 'gmail.com'
	host = str(input('Enter website name : '))
	print(ping(host))
'''



#	give ip list in ip-source.txt file
with open('ip-source.txt') as file:
	dump = file.read()
	dump = dump.splitlines()
	for ip in dump:
		os.system('clear')
		print('ping new', ip)
		print('_'*60)
		os.system('ping -c 4 {}'.format(ip))
		print('_'*60)
		time.sleep(5)
		