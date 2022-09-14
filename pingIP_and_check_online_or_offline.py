import subprocess
import platform
import os
import time

def ip_on_off_check():
	
	with open('ip-source.txt') as file:
		dump = file.read()
		dump = dump.splitlines()
		print(dump)
		for ip in dump:
			res = os.popen(f'ping {ip}').read()
			if (('unrechable') or ('request time out') or ('0 received') or ('100% packet loss')) in res:
				print(res)
				f = open('downIP.txt', 'a')
				f.write(str(ip) + ' is down' + '\n')
				f.close()
			else:
				print(res)
				f = open('upIP.txt', 'a')
				f.write(str(ip) + ' is up' + '\n')
				f.close()
	
	with open('upIP.txt') as file:
		output = file.read()
		print(output)
	
	with open('upIP.txt') as file:
		pass
	
# =========================

def check_online_or_offline():
	with open('ip-source.txt') as file:
		dump = file.read()
		dump = dump.splitlines()
		for ip in dump:
			res = os.popen(f'ping {ip}').read()
			if (('unreachable') or ('Request time out' or ('0 received') or ('100% packet loss'))) in res:
				print(res)
				f=open('downIP.txt', 'w')
				print(ip + ' is down' + '\n')
				f.write(str(ip) + ' is down' + '\n')
				f.close()
			else:
				print(res)
				f=open('upIP.txt', 'w')
				f.write(str(ip) + ' is up' + '\n')
				f.close()
			
# ===============================

with open('ip-source.txt') as file:
	dump = file.read()
	dump = dump.splitlines()
	for ip in dump:
		if (platform.system().lower() == 'windows'):
			os.system('cls')
			print('Ping new ip - ', ip)
			print('_' * 60)
			os.system('ping -n 2 {}'.format(ip))
			check_online_or_offline()
			print('_' * 60)
			time.sleep(5)
			
		else:
			os.system('clear')
			print('Ping new ip - ', ip)
			print('_' * 60)
			#os.system('ping -c 4 {}'.format(ip))
			online=os.system(f'ping -c 2 {ip}')
			check_online_or_offline()
			print('_' * 60)
			time.sleep(5)
			
			
