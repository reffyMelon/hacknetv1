# -*- coding: utf-8 -*-
#modules
import os 
import sys
import time
import colorama
from colorama import *
from termcolor import colored
#banner
os.system("clear")
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
def main():
		#Device information	
		banner()
		print(colored('Name of your OS...', "blue"))
		#можно сделать так:os.system('uname -o')
		print(sys.platform)
		print(colored('Other system info...', "blue"))
		if os.system("neofetch") == 1:
			os.system('pkg install neofetch')
		print(colored('Menu:', "blue"))
		print(colored('$#############################$', "blue"))
		print(colored('1)Ports-Scanner:', "blue"))
		print(colored('3)Whois', "blue"))
		print(colored('4)Information gathering', "blue"))
		print(colored('5)Exploitation', "blue"))
		print(colored('6)', "blue"))
		print(colored('$#############################$', "blue"))
		join()
def menu():
	os.system("clear")
	main()
def join():
	while True:
		hpt = input("[$HPT]>", "red")
		#так же можно сделать так:
		#temp = colored("$", "blue") + colored(str(os.environ.get("USERNAME")), "red") + "||" + colored(str(os.getcwd()), "green") + colored(":-->", "yellow")
		#hpt = input(temp)
		#functionality:
	if hpt == "1":
		print(colored('Ports-Scanner', "blue"))

menu()
