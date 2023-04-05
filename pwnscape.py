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
import validators
import hashlib




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

def pwnscan():
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

def pingr():
    clear()
    cprint("input a valid web address: ", "green")
    cprint("or (back) to return to menu", "green")
    pingr_secure_chk = input("Is website using HTTPS?\n (y) HTTPS\n (n) HTTP\n(m) Return to Menu")
    pingr_protocol_addr = ""
    pingr_www = input("Address: ")
    if pingr_secure_chk == "y" or pingr_secure_chk == "Y":
        pingr_protocol_addr = "https://"
    elif pingr_secure_chk == "n" or pingr_secure_chk == "N":
        pingr_protocol_addr = "http://"

    if validators.url(f"{pingr_protocol_addr}{pingr_www}") is True:
        cprint(f"{pingr_www} is a VALID URL :)", "green")
        time.sleep(.5)
        print("\nOutput:")
        print(socket.gethostbyname(pingr_www))
    else:
        clear()
        cprint(f"{pingr_www} is NOT VALID :)", "red")
        cprint("Please Try Again!\n")
    input("press ENTER to continue")

def pwnhash():
    clear()
    print(" ____                   _   _           _     ")
    print("|  _ \__      ___ __   | | | | __ _ ___| |__  ")
    print("| |_) \ \ /\ / / '_ \  | |_| |/ _` / __| '_ \ ")
    print("|  __/ \ V  V /| | | | |  _  | (_| \__ \ | | |")
    print("|_|     \_/\_/ |_| |_| |_| |_|\__,_|___/_| |_|")
    while True:
        cprint("Main Menu", "green")
        cprint("(input) -sets the hash value", "green")
        cprint("(hashr) -provides all the hash values for hash.txt", "blue")
        cprint("(back) -back to main menu", "red")
        menu_input = input("\nYour Selection: ")
        if menu_input == "input":
            print("selected [input]")
        elif menu_input == "hashr":
           filename = input("Enter the input file name: ")
           sha256_hash = hashlib.sha256()
           with open(filename, "rb") as f:
               for byte_block in iter(lambda: f.read(4096),b""):
                   sha256_hash.update(byte_block)
                   print(byte_block)
                   print(sha256_hash.hexdigest())
        elif menu_input == "pingr":
            continue
        elif menu_input == "pwnhash":
            continue
        elif menu_input == "back" or menu_input == "exit":
            break           
        else:
            cprint("invalid option! Try again", "red")
            input("press ENTER to continue...")
            break

while True:
    clear()
    banner()
    cprint("Main Menu", "green")
    cprint("(pwnscan) -this tool scans wifi in a specified range", "green")
    cprint("(pwnmap) -port scanner [similar to nmap]", "blue")
    cprint("(pwnhash) -to be developed", "green")
    cprint("(pingr) -Checks a Valid URL and displays IP Addr (IPv4)", "blue")
    cprint("(exit) -Exits the program", "red")
    menu_input = input("\nYour Selection: ")
    if menu_input == "exit":
        exit()
    elif menu_input == "pwnscan":
        pwnscan
    elif menu_input == "pingr":
        pingr()
    elif menu_input == "pwnhash":
        pwnhash()


#modules = os.getcwd()
#for module in modules:
#    print(module)