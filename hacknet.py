#modules
import socket
import os
import subprocess
import sys
import requests
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
def ip(dn):
	try:
		ip = socket.gethostbyname(domainName)
		return ip
	except:
        return "[Error]: ip not found!"
ip()

def getServerName ( siteName ):
    try:
        content = requests.get( siteName )
        server = content.headers['Server']
        return server

    except:
        return "[Error]: Server not found!"
if moduleNum == "1":

        try:
            domain = input ( "[Enter domain]: " ) 
            ipSite = getIPaddr(domain) 

            print("-" * 60)
            print("[IP] == [{0}]".format(ipSite)) 
            print("-" * 60)

        except:
            print( "[Error]: Domain or ip not found!" )
  

    elif moduleNum == "2":

        try:
            site = input ( "[Enter domain]: " )
            url = "http://" + site
            server = getServer(url)
          
            print("-" * 60)
            print("[Server] == [{0}]".format(server))
            print("-" * 60)

        except:
            print( "[Error]: Domain or server not found!" )


    comand()
   getServerName()
def comand (): 

    comand = input("[$] --> ")

    if comand == "exit": exit( "Close program... " )
    elif comand == "back": print(comand())
    elif comand == "modules":
      
        print ( modulesList )
        print ( setModule () )

    else:

        print ( "[Error]: Comand not found!" )
        print ( comand () )


print(comand())
comand()
