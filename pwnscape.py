import os
from os import system, name
import os.path
import sys
from pyfiglet import Figlet
from termcolor import cprint
from datetime import datetime
from datetime import date
import time
import colorama
import platform
import scapy.all as scapy
from tcping import Ping
import socket




#Function for clearing the screen throughout the program
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#custom_fig = Figlet()
#print(custom_fig.renderText('pwnyboi'))
def banner():
    print(" ______        ___   _      ____")
    print("|  _ \ \      / / \ | |    / ___|  ___ __ _ _ __   ___")
    print("| |_) \ \ /\ / /|  \| |____\___ \ / __/ _` | '_ \ / _ \ ")
    print("|  __/ \ V  V / | |\  |_____|__) | (_| (_| | |_) |  __/")
    print("|_|     \_/\_/  |_| \_|    |____/ \___\__,_| .__/ \___|")
    print("                                           |_|")
    print("Created by: PwnyBoi :)")

def wifi_scan():
    clear()
    cprint("Remember wifi adapter must be set to promiscuous mode...", "blue")
    time.sleep(.25)
    clear()
    cprint("Remember wifi adapter must be set to promiscuous mode...", "red")
    time.sleep(.25)
    clear()
    cprint("Remember wifi adapter must be set to promiscuous mode...", "blue")
    time.sleep(.25)
    clear()
    cprint("Remember wifi adapter must be set to promiscuous mode...", "red")
    time.sleep(.25)
    clear()
    cprint("Remember wifi adapter must be set to promiscuous mode...", "")
    time.sleep(.25)
    clear()
    cprint("Remember wifi adapter must be set to promiscuous mode...", "red")
    time.sleep(.25)
    clear()
    cprint("Remember wifi adapter must be set to promiscuous mode...", "white")
    time.sleep(.25)
    clear()
    cprint("Remember wifi adapter must be set to promiscuous mode...", "red")
    time.sleep(.25)
    clear()
    # Regular Expression Pattern to recognise IPv4 addresses.
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    # Get the address range to ARP
    while True:
        ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
        if ip_add_range_pattern.search(ip_add_range_entered):
            print(f"{ip_add_range_entered} is a valid ip address range")
            time.sleep(19)
            break
    # Try ARPing the ip address range supplied by the user. 
    # The arping() method in scapy creates a pakcet with an ARP message 
    # and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff.
    # If a valid ip address range was supplied the program will return 
    # the list of all results.
    arp_result = scapy.arping(ip_add_range_entered)

def ping():
    clear()
    cprint("input a valid web address: ", "green")
    cprint("or (back) to return to menu", "green")
    ping_www = input("Address: ")
    print("Output:")
    print(socket.gethostbyname(ping_www))
    input("press ENTER to continue")
   



while True:
    clear()
    banner()
    cprint("Main Menu", "green")
    cprint("(scan_wifi) -this tool scans wifi in a specified range", "green")
    cprint("(pwnmap) -port scanner [similar to nmap]", "blue")
    cprint("(tool 3) -to be developed", "green")
    cprint("(ping) - use -n for windows and -c for unix", "blue")
    cprint("(exit) -Exits the program", "red")
    menu_input = input("\nYour Selection: ")
    if menu_input == "exit":
        exit()
    elif menu_input == "scan_wifi":
        wifi_scan()
    elif menu_input == "ping":
        ping()