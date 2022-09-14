#!/usr/bin/python3
import os
import platform
import time
import sys
import threading

if sys.version_info[0] !=3: 
	print('''--------------------------------------
	REQUIRED PYTHON 3.x
	use: python3 checkonline.py
--------------------------------------
			''')
	sys.exit()
'''
ip = "192.168.0."
for x in range(100, 110):
	result = os.popen('ping -c 1 ' + ip + str(x))
	try:
		for line in result.readlines():
			if "TTL" in line:
				print("DETECTED: ", line)
				print("ONLINE : ", ip + str(x))
			else:
				print("OFFLINE: ", ip + str(x))
	except:
		print("Sumthing is rong ")
'''
with open("output.txt", "w"):
	pass
	
with open('ip-list.txt') as file:
	dump = file.read()
	dump = dump.splitlines()
for i in dump:
	def check():
		print('Please stayed work is under process !!!')
		parem = '-n' if platform.system().lower() == 'windows' else '-c'
		host = i.split()[0]
		ip = i.split()[1]
		res = os.popen(f'ping {parem} 2 {ip}').read()
		if ("Request time out") in res:
			print(res)
			f=open("output.txt", "a")
			f.write(str(host) + "\t" + str(ip) + "\t" + "down" + "\n")
			f.close()
		elif ("Destination host unreachable") in res:
			print(res)
			f=open("output.txt", "a")
			f.write(str(host) + "\t" + str(ip) + "\t" + "down" + "\n")
			f.close()
		elif ("100% packet loss") in res:
			print(res)
			f=open("output.txt", "a")
			f.write(str(host) + "\t" + str(ip) + "\t" + "down" + "\n")
			f.close()
		else:
			f=open("output.txt", "a")
			f.write(str(host) + "\t" + str(ip) + "\t" + "up" + "\n")
			f.close()
	
	if (platform.system().lower() == 'windows'):
		os.system('cls')
		check()
	else:
		os.system('clear')
		
		thred= threading.Thread(target = check )
		thred.start()

print('_' * 60)
with open("output.txt", "r") as file:
	output = file.read()
print(output)
print('_' * 60)	


