# -*- coding: utf-8 -*-
#modules
import os
import sys
from core import *
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

def banner():
	print(colored(' ██╗  ██╗ █████╗  ██████╗██╗  ██╗     ███╗   ██╗███████╗████████╗', "red"))
	print(colored(' ██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝╚══██╔══╝', "red"))
	print(colored(' ███████║███████║██║     █████╔╝█████╗██╔██╗ ██║█████╗     ██║', "red"))
	print(colored(' ██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██╔══╝     ██║', "red"))
	print(colored(' ██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║███████╗   ██║', "red"))
	print(colored(' ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝', "red"))
	print(colored(' __________________________________________________________________', "red"))
	print(colored('|		Author:Reffy|My VK:https://vk.com/mrgurutopyt			  |', "red"))
	print(colored('|		My GitHub:https://github.com/reffyMelon					  |', "red"))
	print(colored('|		The creation date of the script:22.04.2019				  |', "red"))
	print(colored(' ------------------------------------------------------------------', "red"))
	#print("User:", str(os.environ.get("USERNAME"), "loading conf.")
#main-menu
def join():
	while True:
		temp = colored("$", "blue") + colored(str(os.environ.get("USERNAME")), "red") + "||" + colored(str(os.getcwd()), "green") + colored(":-->", "yellow")
		hpt = input(temp)
		#hpt = input("[$HPT]>", "blue")

		if hpt == "1":
			portscanner()
		# if hpt == "2":

		# if hpt == "3":

		if hpt == "7":
			print("Goodbye!")
			exit()
def main():
		#Device information	
		banner()
		print(colored('Menu:', "blue"))
		print(colored('$#############################$', "blue"))
		print(colored('1)Ports-Scanner', "blue"))
		print(colored('3)Whois', "blue"))
		print(colored('4)Tools installation', "blue"))
		print(colored('5)Exit', "blue"))
		print(colored('$#############################$', "blue"))
		join()
def menu():
	main()
menu()