#!/ban/python3

import sys
import socket #for node to node connexion
from datetime import datetime #for date and time

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of argument.")
	print("Syntax: pyhton3 scanner.py <ip>")
	
#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-"*50)
try:
	for port in range(" ", " "): #can try 50 and 85 only first, max port 65535
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))  #return an error indicator
		
		print("Cheking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except keyboardInterrupt: #keyboard interrupt like ctrl c
	print("\nExisting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Could not connect to server.")
	sys.exist()
