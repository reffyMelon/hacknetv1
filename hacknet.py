# -*- coding: utf-8 -*-
#modules
import os 
import subprocess 
import sys 
import time 
import colorama
from termcolor import colored
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
#main-menu
def main():
		#Device information	
		print('Name of your OS...')
		print(sys.platform)
		os.system('uname -o')
		print(colored('Other system info...', "blue"))
		if os.system("neofetch") == 1:
			os.system('pkg install neofetch')
		print(colored('Menu:', "blue"))
		print('$##########################$')
		print(colored('Menu:', "blue"))
		print(colored('$#############################$', "blue"))
		print(colored('1)Ports-Scanner:', "blue"))
		print(colored('3)Whois', "blue"))
		print(colored('4)Information gathering', "blue"))
		print(colored('5)Exploitation', "blue"))
		print(colored('6)Exit', "blue"))
		print(colored('$#############################$', "blue"))
		join()
		hpt = input("[$HPT]>", "blue")
		#if hpt == "1":

		#if hpt == "2":
			
		#if hpt == "3":
		
		if hpt == "7":
			print("Bye!")
			exit()
menu()
