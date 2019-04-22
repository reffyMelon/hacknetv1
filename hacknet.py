#modules
import socket
import os
import subprocess
import sys
import time
#banner
print('██╗  ██╗ █████╗  ██████╗██╗  ██╗     ███╗   ██╗███████╗████████╗' )
print(' ██║  ██║██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝╚══██╔══╝')
print(' ███████║███████║██║     █████╔╝█████╗██╔██╗ ██║█████╗     ██║'   )
print(' ██╔══██║██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██╔══╝     ██║'   )
print(' ██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║███████╗   ██║'	 )
print(' ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝'	 )
#main-menu
def main():
#a lot of print's :)
	print("H", end = "")
	time.sleep(0.1)
	print("e", end = "")
	time.sleep(0.4)
	print("l", end = "")
	time.sleep(0.7)
	print("l", end = "")
	time.sleep(0.10)
	print("o", end = "")
	time.sleep(0.11)
	print('Thank you for using my script')
	print(' ______________________________________________ ')
	print('|Author:Reffy|My VK:https://vk.com/mrgurutopyt |')
	print('|My GitHub:https://github.com/reffyMelon       |')
	print('|The creation date of the script:22.04.2019    |')
	print('|______________________________________________|')
	print("""
     ____________________
   +|Developed for Termux|+
  ==========================
    """)

#Device information	
	print('Name of your OS...')
	print('os.name')
	os.system('uname -o')
	print('Check your MAC-address:')
main()
