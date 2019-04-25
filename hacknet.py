# -*- coding: utf-8 -*-
#modules
import os 
import subprocess 
import sys 
import time
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM
from prettytable import PrettyTable
from colorama import *
import progressbar

def banner():
	print(' ██╗  ██╗ █████╗  ██████╗██╗  ██╗     ███╗   ██╗███████╗████████╗' )
	print(' ██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝╚══██╔══╝')
	print(' ███████║███████║██║     █████╔╝█████╗██╔██╗ ██║█████╗     ██║'   )
	print(' ██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██╔══╝     ██║'   )
	print(' ██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║███████╗   ██║'	 )
	print(' ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝'	)
	print("""
	 ______________________________________________ 
	 |Author:Reffy|My VK:https://vk.com/mrgurutopyt |
	 |My GitHub:https://github.com/reffyMelon       |
	 |The creation date of the script:22.04.2019    |
	  ______________________________________________
	  ########################
	  # Developed for Termux #
	  ########################
	""")

#main-menu
def main():
		#Device information	
		banner()
		print('Name of your OS...')
		os.system('uname -o') 
		print('Other system info...')
		os.system("neofetch")
		print('Menu:')
		print('$##########################$')
		print('1)Gratitudes')
		print('2)Nmap')
		print('3)Metasploit')
		print('4)Port scan')
		print('5)Whois')
		print('6)IP Lookup')
		print('7)Quit')
		print('----------------------------')
		join()
def menu():
	os.system("clear")
	main()
def join():
	while True:
		hpt = input("[$hpt]>")


		if hpt == "1":
				print("""
			       #######################################
			       #Helpers/second developers:           #
			       # 1)https:github.com/Nironic/hacknetv1#
			       # 2)https://github.com/inkviz96       #
			       #######################################
				""")


		if hpt == "2":
			print('install Nmap') 
			os.system("apt update && apt upgrade") 
			os.system("pkg install nmap") 
			print("The installation is finished")


		if hpt == "3":
			print('install Metasploit')
			os.system("apt update && apt upgrade") 
			os.system("pkg install unstable-repo") 
			os.system("pkg install metasploit") 

		
		if hpt == "7":
			print("Bye!")
			exit()



#Start old process for programm
menu()
