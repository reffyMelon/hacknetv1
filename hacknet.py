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
	print("Thank", end = "")
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
	os.system('uname -o')
	print('Other system info...')
	if os.system("neofetch") == 1:
		os.system('pkg install neofetch')
main()
