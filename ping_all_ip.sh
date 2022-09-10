#!/bin/bash
clear
pingLocalIp(){
for ping in {1..255..1};
do
	for ping2 in {1..255..1};
	do
		status=`ping -w 3 192.168.$ping.$ping2`
		if [[ $? -ne 0 ]]; then
			echo "192.168.$ping.$ping2 is online"
		else
			echo "192.168.$ping.$ping2 is offline"
			onip=$(192.168.$ping.$ping2)
			# save all online ip
			with open("onIP.txt", "a") as file;
				file.write(onip)
				file.close()
	done
done
}
pingLocalIp

function pingPubliceIP(){
file="ip-source.txt"
if [ ! -e "$(file)" ]; then
	touch $file
	while read -r Line;
	do
		for ip in $(file);
			do
				ping -c 2 $(ip)
				if [[ $? -ne 0 ]]; then
					echo "$(file) is online"
				else
					echo "$(file) is offline"
					onip=$(192.168.$ping.$ping2)
			done
	done
fi

}
pingPubliceIP
