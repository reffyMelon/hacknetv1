# -*- coding: utf-8 -*-
#modules
import socket
import os
import subprocess
import sys
import time
def banner():
print(' ██╗  ██╗ █████╗  ██████╗██╗  ██╗     ███╗   ██╗███████╗████████╗' )
print(' ██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝╚══██╔══╝')
print(' ███████║███████║██║     █████╔╝█████╗██╔██╗ ██║█████╗     ██║'   )
print(' ██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██╔══╝     ██║'   )
print(' ██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║███████╗   ██║'	 )
print(' ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝'	 )
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
#a lot of print's :)
banner()
print("|Thank", end = "")
time.sleep(0.1)
print("you", end = "")
time.sleep(0.4)
print("for", end = "")
time.sleep(0.7)
print("using", end = "")
time.sleep(0.10)
print("my", end = "")
time.sleep(0.11)
print('script')
#Device information	
print('Name of your OS...')
os.system('uname -o')
print('Other system info...')
if os.system("neofetch") == 1:
	os.system('pkg install neofetch')
print('Menu:')
print('$##########################$')
print('1)Gratitudes')
print('2)Nmap')
print('3)Metasploit')
print('4)Port scan')
print('5)Whois')
print('6)IP Lookup')
print('7)Quit')
hpt = raw_input("[$hpt]>")
def restart():
	#copied from https://github.com/Gameye98/Lazymux
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
def back():
	##copied from https://github.com/Gameye98/Lazymux
	print('Quit!')
	back = raw_input("[$hpt]>")
	if back == "7":
		restart()
	else:
		print('ERROR!')
		time.sleep(2)
		restart()
		
if hpt == "1":
	print("""
								       
		############################################## =========
		#Second developer:https://github.com/inkviz96# Writes port-scanner         
		############################################## =========
	""")
Nmap = raw_input("[$hpt]>")
if hpt == "2":
	print('install Nmap')
	subprocess.run("apt update && apt upgarde")
	subprocess.run("pkg install nmap")
	print("The installation is finished")
Metasploit = raw_input("[$hpt]>")
if hpt == "3":
	print('install Metasploit')
	subprocess.run("apt update && apt upgarde")
	subprocess.run("pkg install unstable-repo")
	subprocess.run("pkg install metasploit")	
Quit = raw_input("[$hpt]>")
if hpt == "7":
	print("Quit back to menu")
	back()
	else:
		print('ERROR!')
		time.sleep(2)
		restart()
main()
