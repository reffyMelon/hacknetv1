# -*- coding: utf-8 -*-
#modules
import os # Use
import subprocess # Use
import sys # Use
import time # Use
import socket
import threading
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM #use
import colorama
from termcolor import colored
os.system("clear")
def banner():
	print(colored(' ██╗  ██╗ █████╗  ██████╗██╗  ██╗     ███╗   ██╗███████╗████████╗', "blue"))
	print(colored(' ██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝╚══██╔══╝', "blue"))
	print(colored(' ███████║███████║██║     █████╔╝█████╗██╔██╗ ██║█████╗     ██║', "blue"))
	print(colored(' ██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██╔══╝     ██║', "blue"))
	print(colored(' ██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║███████╗   ██║', "blue"))
	print(colored(' ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝', "blue"))
	#print("User:", str(os.environ.get("USERNAME"), "loading conf.")
	print(colored("""
	 ______________________________________________ 
	 |Author:Reffy|My VK:https://vk.com/mrgurutopyt |
	 |My GitHub:https://github.com/reffyMelon       |
	 |The creation date of the script:22.04.2019    |
	  ______________________________________________
	""", "green"))

#main-menu
def main():
		#Device information	
		banner()
		print('Name of your OS...')
		os.system('uname -o') # Os command line
		print(colored('Other system info...', "red"))
		if os.system("neofetch") == 1:
			os.system('pkg install neofetch')
		print(colored('Menu:', "green"))
		print('$##########################$')
		print(colored('1)Port scaner:', "green"))
		#print(colored('3)Metasploit', "green"))
		#print(colored('4)Port scan', "green"))
		#print(colored('5)Whois', "green"))
		#print(colored('6)IP Lookup', "green"))
		print(colored('7)Quit', "green"))
		print('----------------------------')
		join()
def menu():
	os.system("clear")
	main()
def join():
	while True:
		hpt = input("[$HPT]>", "green")
		#так же можно сделать так:
		#temp = colored("$", "blue") + colored(str(os.environ.get("USERNAME")), "red") + "||" + colored(str(os.getcwd()), "green") + colored(":-->", "yellow")
		#hpt = input(temp)
		#functionality:
	if hpt == "1":
		portsList = input("Enter targets IP:")
		print(portsList)
		if portsList = []:
			portsList = [21, 22, 23, 25, 38, 43, 80, 109, 110, 115, 118, 119, 143,
			194, 220, 443, 445, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
			3306, 4000, 4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200]
		def scan(port):
			host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			time.sleep(0.6)
		try:
			 connection = portsList.connect((host, port)) 
			print("Port:", port, "OPEN")
		except:
			pass
		for elements in portsList:
			 t = threading.Thread(portsList=scan, kwargs={'port': element})

			 t.start() 
		input()
menu()
