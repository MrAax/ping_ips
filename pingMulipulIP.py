import os
ip = "192.168.0."
for x in range(10, 110):
	result = os.popen("ping -c 1 " + ip + str(x))
	for line in result.readlines():
		if (("TTL") or ("0% packet loss")) in line:
			print("ONLINE DETECTED: ", line)
		else:
			print("OFFLINE: ", ip + str(x))