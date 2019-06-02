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
		print("Port scaner")
menu()
