#!/usr/bin/python3
import requests
import time
import os
import platform
import pprint
import sys
import datetime

url = 'https://google.com'
'''dt = datetime.today()
mdate = dt.strftime("%d/%b/%Y")
mtime = dt.strftime("%H:%M:%S")
print(mdate, mtime)
'''
with open("mySYSinfo.txt", "w"):
	pass
	
while True:
	try:
		request = requests.get(url, timeout=5)
		print('internet Connected')
		ip = requests.get("https://api.ipify.org").text
		print("What is my ip :  ", ip)
		#time.sleep(3)
		if (platform.system().lower() == 'windows'):
			os.system('cls')
			print('_' * 60)
			print('Ping my ip - ', ip)
			print('_' * 60)
			os.system('ping -n 2 {}'.format(ip))
			url=f"https://ipapi.co/{ip}/json/"
			r=requests.get(url)
			pprint.pprint(r.json())
			print('_' * 60)
			#time.sleep(10)
		else:
			#os.system('clear')
			print('-' * 60)
			print('Ping my ip - ', ip)
			print('_' * 60)
			#os.system('ping -c 4 {}'.format(ip))
			online=os.system(f'ping -c 2 {ip}')
			url=f"https://ipapi.co/{ip}/json/"
			r=requests.get(url)
			pprint.pprint(r.json())
			print('_' * 60)
			#time.sleep(15)
			with open('mySYSinfo.txt', 'a') as f:
				f.write(ip + '\n')
				f.close()
		break
	except:
	   	print('internet not Connected')
	   	time.sleep(3)
	   	continue
	   	
	   	