# -*- coding: utf-8 -*-
import os
import socket
from termcolor import colored
def posrtscan():
	def scaner():
    color_a = colored("[+] ", 'green')
    print("#"*55)
    host = input(color_a + "Host --> ")
    port = int(input(color_a + "Port --> "))
    print("#"*55)

    scan = socket.socket()
    try:
        scan.connect((host, port))
    except socket.error:
        print(color_b + "Port -- ", port, " -- [CLOSED]")
    else:
        print(color_c + "Port -- ", port, " -- [OPEN]")

def scaner2():
    color_a = colored("[+] ", 'green')
    color_b = colored("[!] ", 'red')
    color_c = colored("[!] ", 'yellow')

    host = input(color_a + "Host --> ")
    print("\n")
    port = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23, 
	   24, 25, 26, 27, 29, 53, 67, 68, 79, 80, 88, 106, 110, 111, 113, 119, 
	   123, 137, 138, 139, 143, 161, 192, 311, 312, 389, 427, 443, 445, 464, 
	   465, 500, 514, 414, 532, 548, 554, 587, 600, 623, 625, 626, 660, 687, 
	   749, 985, 993,995, 1085, 1099, 1220, 1640, 1649, 1701, 1723, 1900, 2049, 
	   2195, 2196, 2336, 3004,3031, 3283, 3284, 3306, 3659, 3689, 3690, 4111, 
	   4488, 4500, 5003, 5100, 5222, 5223, 5228, 5297, 5350, 5351, 5353, 6970, 
	   7070, 8000, 8005, 8008, 8043, 8080, 8089, 8096, 8170, 8171, 8175, 8443, 
	   8800, 8843, 9418, 11211, 50003]

    for p in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.5)
            scan.connect((host, p))
        except socket.error:
            print(color_b + "Port -- ", p, " -- [CLOSED]")
        else:
            print(color_c + "Port -- ", p, " -- [OPEN]")

print("~"*50)

print(colored("[1] --- сканировать отделный порт", "blue"))
print(colored("[2] --- сканировать список", "blue"))

print("#"*55)
scann = input("[scan]--> ")

if scann == "1":
    scaner1()
elif text_a == "2":
    scaner2()
else:
    print(colored("Параметр введен не правильно!", 'red'))
