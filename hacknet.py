# -*- coding: utf-8 -*-
#modules
import os # Use
import subprocess # Use
import sys # Use
import time # Use
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

os.system("clear")

def banner():
	print(colored(' ██╗  ██╗ █████╗  ██████╗██╗  ██╗     ███╗   ██╗███████╗████████╗', "red"))
	print(colored(' ██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝╚══██╔══╝', "blue"))
	print(colored(' ███████║███████║██║     █████╔╝█████╗██╔██╗ ██║█████╗     ██║', "red"))
	print(colored(' ██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██╔══╝     ██║', "blue"))
	print(colored(' ██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║███████╗   ██║', "red"))
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
		os.system("neofetch")
		print(colored('Menu:', "blue"))
		print('$##########################$')
		print(colored('1)Gratitudes', "yellow"))
		print(colored('2)Nmap', "red"))
		print(colored('3)Metasploit', "red"))
		print(colored('4)Port scan', "yellow"))
		print(colored('5)Whois', "green"))
		print(colored('6)IP Lookup', "red"))
		print(colored('7)Quit', "blue"))
		print('----------------------------')
		join()


def menu():
	os.system("clear")
	main()
def join():
	while True:
		#temp = colored("$", "blue") + colored(str(os.environ.get("USERNAME")), "red") + "||" + colored(str(os.getcwd()), "green") + colored(":-->", "yellow")
		#hpt = input(temp)
		hpt = input("[$HPT]>")

		if hpt == "1":
				print("""
													
				############################################## =========
				#Second developer:https://github.com/inkviz96# Writes port-scanner         
				############################################## =========
				""")


		if hpt == "2":
			print('install Nmap') #print
			os.system("apt update && apt upgrade") #Update apt and System termux
			os.system("pkg install nmap") #Install nmap
			print("The installation is finished")


		if hpt == "3":
			print('install Metasploit')
			os.system("apt update && apt upgrade") #Update apt and System termux
			os.system("pkg install unstable-repo") #Install repositories
			os.system("pkg install metasploit") #Install metasploit


		if hpt == "7":
			print("Goodbay")
			exit()



#Start old process for programm
menu()
