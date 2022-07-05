import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py")

#Add a pretty banner
print(" ")
print("~" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("~" * 50)
print(" ")
print(" ")
try:
	flag=0
	ctr=0
	print("/"* 75)
	print("TEST Results!!")
	print(" ")
	for port in range(1,65535):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result ==0:
			print("		Port {} is open".format(port))
			flag=1
		ctr+=1
		s.close()
	if(flag==0):
		print("	dang!! All ports are closed...")
	print("Total port scanned {}".format(ctr))
	print("\\" *75)
except KeyboardInterrupt:
	print("\nExiting program...")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()

