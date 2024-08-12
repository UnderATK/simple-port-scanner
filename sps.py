import socket
from datetime import datetime

# define enums
VR = "0.1.0"
AUTHOR = "UnderATK"
ERR = "\033[31m[Error]"

def scanner(target):
    try:
        targetIP = socket.gethostbyname(target)

        print("----------------------------------")
        print(f"Scanning the target: {target} | {targetIP}")
        print(f"Scan starting time: {datetime.now()}")
        print("----------------------------------")
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
        print(f"{ERR} Hostname could not be resolved.")

    except socket.error:
        print(f"{ERR} could not connet to the server.")

print(f"----- Simple Port Scanner v{VR} -----")
print(f"----- By {AUTHOR}                -----")
target = input("Enter the target IP address or domain: ")
scanner(target)

