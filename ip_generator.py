from time import sleep
import random
import string 

def localIP_generator():
	for i in range(0, 256, 1):
	  for j in range(0, 256, 1):
	  	#for k in range(0, 256, 1):
	  		#for l in range(0, 256, 1):
	  			#print(f'ping : 192.168.{i}.{j}')
	  			#host = (f'{i}.{j}.{k}.{l}')
	  			host = (f'192.168.{i}.{j}')
	  			print(host)
	  			with open('ip-source.txt', 'a') as f:
	  				print(host)
	  				f.write(host + '\n')
	  				sleep(0.1)
	  				f.close()
'''
while True:
	localIP_generator()
'''

def ipv4_generator():
	number = random.randint(0, 255)
	return number

while True:
	for x in range(1, 101):
		ip=(f'{ipv4_generator()}.{ipv4_generator()}.{ipv4_generator()}.{ipv4_generator()}')
		with open('ip-source.txt', 'a') as f:
			print(x, ') ' + ip)
			f.write(ip + '\n')
			f.close()
			sleep(1)
	

def ipv6_generator():
	#letters = string.ascii_letters
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	num = '1234567890'
	symbols = letters + num
	length = 4
	ipv6 = "".join(random.sample(symbols, length))
	return ipv6

'''	
while True:
	ip=(f'{ipv6_generator()}:{ipv6_generator()}:{ipv6_generator()}:{ipv6_generator()}:{ipv6_generator()}:{ipv6_generator()}:{ipv6_generator()}:{ipv6_generator()}')
	with open('ip-source.txt', 'a') as f:
		print(ip)
		f.write(ip + '\n')
		sleep(0.1)
		f.close()
'''