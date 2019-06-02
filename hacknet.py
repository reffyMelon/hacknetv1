# -*- coding: utf-8 -*-
#modules
import os # Use
import subprocess # Use
import sys # Use
import time # Use
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM #use
try:
	from prettytable import PrettyTable
except:
	print("Install prettytable")
	os.system("pip install prettytable")
try:
	import colorama
except:
	print("Install colorama")
	os.system("pip install colorama")
try:
	from termcolor import colored
except:
		print("Install termcolor")
		os.system("pip install termcolor")
from colorama import *
try:
	import progressbar
except:
	print("Install progressbar")
	os.system("pip install progressba")



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
	  ########################
	  # Developed for Termux #
	  ########################
	""", "green"))

#main-menu
def main():
		#Device information	
		banner()
		print('Name of your OS...')
		os.system('uname -o') # Os command line
		print(colored('Other system info...', "red"))
		os.system("pkg install neofetch")
		os.system("neofetch")
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
		hpt = input("[$HPT]>")
		#так же можно сделать так:
		#temp = colored("$", "blue") + colored(str(os.environ.get("USERNAME")), "red") + "||" + colored(str(os.getcwd()), "green") + colored(":-->", "yellow")
		#hpt = input(temp)
		#functionality:
		if hpt == "1":
			#port scaner developer:https://github.com/inkviz96?
			print("Port scaner")
			init(autoreset=True)
			usersTarget = input("Input target's ip or url: ")
			portsList = [int(x) for x in input("Input ports \"like 80 443 8080\"(or empty for full scan): ").split()]
			print(portsList)
			if portsList == []:
				portList = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23,24, 25, 26, 27, 29, 53, 67, 68, 79, 80, 88, 106, 110, 111, 113, 119,123, 137, 138, 139, 143, 161, 192, 311, 312, 389, 427, 443, 445, 464,465, 500, 514, 414, 532, 548, 554, 587, 600, 623, 625, 626, 660, 687,749, 985, 993,995, 1085, 1099, 1220, 1640, 1649, 1701, 1723, 1900, 2049,2195, 2196, 2336, 3004,3031, 3283, 3284, 3306, 3659, 3689, 3690, 4111,4488, 4500, 5003, 5100, 5222, 5223, 5228, 5297, 5350, 5351, 5353, 6970,7070, 8000, 8005, 8008, 8043, 8080, 8089, 8096, 8170, 8171, 8175, 8443,8800, 8843, 9418, 11211, 50003]
def CheckPorts(portsListValue=portsList, target="192.168.100.1"):
	targetIP = gethostbyname(target)
	portIsOpen = []
	portIsClose = []
	statusPortScan = len(portsListValue)
	print(target)
	progressBarScan = progressbar.ProgressBar(maxval=statusPortScan)
	progressBarScan.start()
	contProgressBar = 0
	for portCount in portsListValue:
		testSocket = socket(AF_INET, SOCK_STREAM)
		testSocket.settimeout(1)
		try:
			result = testSocket.connect_ex((targetIP, int(portCount)))
			if(result == 0):
				portIsOpen.append(portCount)
				progressBarScan.update(contProgressBar)
				contProgressBar += 1
			else:
				portIsClose.append(portCount)
				progressBarScan.update(contProgressBar)
				contProgressBar += 1
				testSocket.close()
		except:
			print("ERROR SOCKET!")

		progressBarScan.finish()
		return portIsOpen, portIsClose
def portsTable(portIsOpenList, portIsCloseList):
	tablePortsList = PrettyTable([Back.WHITE + Fore.BLACK + "Port", "Availability"])
	for everyPorts in portIsOpenList:
		tablePortsList.add_row([Back.WHITE + Fore.GREEN + str(everyPorts), "Open"])
	for everyPorts in portIsCloseList:
		tablePortsList.add_row([Back.WHITE + Fore.RED + str(everyPorts), "Close"])
	tablePortsList.reversesort = False

	return tablePortsList

portIsOpenList, portIsCloseList = CheckPorts(target = usersTarget)
print(portsTable(portIsOpenList, portIsCloseList))
menu()
