# -*- coding: utf-8 -*-
import os
import socket
import colorama
import progressbar
from colorama import *
from termcolor import colored
def posrtscan():
	print(colored("#"*10, "blue"))
	target = input(colored("Host:", "blue"))
	port = input(colored("Port:", "blue"))
	print(colored("#"*10, "blue"))
	scan = socket.socket()
	try:
    	scan.connect((host, port))
	except scan.error:
    	print(colored( "Port --> ", port, "|closed|", "blue"))
	else:
    	print(colored("Port --> ", port, "|open|", "blue"))
def scanner2():
	target = input(colored("Host:", "blue"))
	port = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23, 
			24, 25, 26, 27, 29, 53, 67, 68, 79, 80, 88, 106, 110, 111, 113, 119, 
			123, 137, 138, 139, 143, 161, 192, 311, 312, 389, 427, 443, 445, 464, 
			465, 500, 514, 414, 532, 548, 554, 587, 600, 623, 625, 626, 660, 687, 
			749, 985, 993,995, 1085, 1099, 1220, 1640, 1649, 1701, 1723, 1900, 2049, 
			2195, 2196, 2336, 3004,3031, 3283, 3284, 3306, 3659, 3689, 3690, 4111, 
			4488, 4500, 5003, 5100, 5222, 5223, 5228, 5297, 5350, 5351, 5353, 6970, 
			7070, 8000, 8005, 8008, 8043, 8080, 8089, 8096, 8170, 8171, 8175, 8443, 
			8800, 8843, 9418, 11211, 50003]
	for p in port:
		try:
			scan = socket.socket()
			scan.settimeout(0.5)
			scan.connect((host, p))
		except scan.error:
            print(colored("Port --> ", p, " -- |closed|", "blue"))
        else:
            print(colored("Port --> ", p, " -- |open|", "blue"))
