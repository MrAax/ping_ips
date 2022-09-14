#!/usr/bin/python3
import os, ipaddress

while True:
	ip=input('IP validity check: ')
	try:
		print('_' * 60)
		print(ipaddress.ip_address(ip))
		print('This ip is valid')
		print('_' * 60)
	except:
		print('_' * 60)
		print('This ip is not valid')
		print('_' * 60)
	finally:
		if ip == 'q':
			print('script finished')
		break