import subprocess
import platform
import os
import time
#import urllib2
from urllib.request import urlopen
import json

def ping(host):
	global parem
	parem = '-n' if platform.system().lower() == 'windows' else '-c'
	command = ['ping', parem, '2', host]
	return subprocess.call(command)
'''
for i in range(0, 256, 1):
  for j in range(0, 256, 1):
  	#print(f'ping : 192.168.{i}.{j}')
  	host = f'192.168.{i}.{j}'
  	print(ping(host))
'''

'''
while True:
	#host = 'google.com'
	host = str(input('Enter website name : '))
	print(ping(host))
'''


#	give ip list in ip-source.txt file
with open('ip-source.txt') as file:
	dump = file.read()
	dump = dump.splitlines()
	for ip in dump:
		if (platform.system().lower() == 'windows'):
			os.system('cls')
			print('Ping new ip - ', ip)
			print('_' * 60)
			os.system('ping -n 2 {}'.format(ip))
			print('_' * 60)
			time.sleep(5)
		else:
			os.system('clear')
			print('Ping new ip - ', ip)
			print('_' * 60)
			#os.system('ping -c 4 {}'.format(ip))
			online=os.system(f'ping -c 2 {ip}')
			print('_' * 60)
			time.sleep(5)
			
		