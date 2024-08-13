#!/bin/python3
import socket
from datetime import datetime
import sys

# define enums
VR = "0.2.1"
AUTHOR = "UnderATK"

# text coloring enums
WHITE_TXT = "\033[0m"
GREY_TXT = "\033[30m"
GRN_TXT = "\033[0;32m"
ERR_TXT = "\033[31m"

# define variables
###

def scanner(target):
    try:
        targetIP = socket.gethostbyname(target)

        print("-" * 75)
        print(f"Scanning the target: {target} | {targetIP}")
        print(f"Scan starting time: {datetime.now()}")
        print("-" * 75)

        for port in range(1,1025): 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((targetIP, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                    print(f"\033[32m[+] \033[30mPort {port}/tcp is open\tService {service}")
                except:
                    print(f"\033[32m[+] \033[30mPort {port}/tcp is open\tService Unknown\t")
            sock.close()

    except socket.gaierror:
        print(f"{ERR_TXT}[Error] Hostname could not be resolved.")
        sys.exit()

    except socket.error:
        print(f"{ERR_TXT}[Error] could not connet to the server.")
        sys.exit()

    except KeyboardInterrupt:
        print("\nExiting sps.py")
        sys.exit()

# Welcome banner
print("-" * 50)
print(f"-----\tSimple Port Scanner v{VR}")
print(f"-----\tBy {AUTHOR}")
print("-" * 50)

# Checking correct amount of arguments
if len(sys.argv) == 2:
    target = sys.argv[1]
    scanner(target)
else: 
    print(f"{ERR_TXT}[Error] Invalid amount of arguments.")
    print(f"{GREY_TXT}Syntax: python3 sps.py <ip/domain>")
    sys.exit()


