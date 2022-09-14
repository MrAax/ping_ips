#!/usr/bin/python3
from time import sleep
import random
import string 

def localIP_generator():
	for i in range(0, 256, 1):
	  for j in range(0, 256, 2):
	  	#for k in range(0, 256, 1):
	  		#for l in range(0, 256, 1):
	  			#print(f'ping : 192.168.{i}.{j}')
	  			#host = (f'{i}.{j}.{k}.{l}')
	  	host = (f'192.168.{i}.{j}')
	  	n=0
	  	while 1:
	  		n +=1
		  	with open('ip-source.txt', 'a') as f:
		  		print(n, ') ' + host)
		  		f.write(host + '\n')
		  		sleep(0.1)
		  		f.close()

def IPv4_generator():
	number = random.randint(0, 255)
	return number


def IPv6_generator():
	#letters = string.ascii_letters
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	num = '1234567890'
	symbols = letters + num
	length = 4
	ipv6 = "".join(random.sample(symbols, length))
	return ipv6


'''
with open("ip-source.txt", "w"):
	pass
	
while True:
	localIP_generator()
'''	
with open("ip-source.txt", "w"):
	pass
	
while True:
	x = 0
	while 1:
		x += 1
		ip = (f'{IPv4_generator()}.{IPv4_generator()}.{IPv4_generator()}.{IPv4_generator()}')
		with open('ip-source.txt', 'a') as f:
			print(x, '] ' + ip)
			f.write(ip + '\n')
			f.close()
			sleep(1)
'''	
with open("ip-source.txt", "w"):
	pass
		
while True:
	ip=(f'{IPv6_generator()}:{IPv6_generator()}:{IPv6_generator()}:{IPv6_generator()}:{IPv6_generator()}:{IPv6_generator()}:{IPv6_generator()}:{IPv6_generator()}')
	with open('ip-source.txt', 'a') as f:
		print(ip)
		f.write(ip + '\n')
		sleep(0.1)
		f.close()
'''