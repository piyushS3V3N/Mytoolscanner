#!/usr/bin/env python3
import sys
import os
from pyfiglet import Figlet
def get_platform():
    platform = {
            'linux1' : 'Linux',
            'linux2' : 'Linux',
            'darwin' : 'OS X',
            'win32' : 'Windows'
            }
    if sys.platform not in platform:
        return sys.platform
    return platform[sys.platform]
def networkscanner():
    os.system("python3 ./tool/pingsweeper.py")
def portscanner():
    os.system("python3 ./tool/scanner.py")
def commandline():
    while True :
        opt = (input("\033[1;31m[s3v3n_k17 ;)]~# \033[1;00m"))
        if (opt == "discover"):
            networkscanner()
        elif (opt == "portscan"):
            portscanner()
        elif (opt == "exit" or opt == "Exit" or opt == "quit"):
            print("[;)]Exiting Now.....")
            break
        elif(opt ==  "clear"):
            os.system('clear')
            banner()
        elif(opt ==  "ls"):
            os.system("ls")
        else:
            print("Invalid Input")
def banner():
    t2 = "  ================================== "
    b2 = "  ||          \033[1;92mS3V3N_K17\033[1;00m           ||"
    cust_fig = Figlet(font = 'slant')
    print(cust_fig.renderText("S3V3N_K17"))
    print(t2)
    print(b2)
    print(t2)
    print(""*100)
    print("To use this tool simply type in the command and to exit type exit")
    print(t2)
    print("  Basic Tools")
    print("  Network Discovery (command: discover)")
    print("  Port Scanner (command: portscan)")
    print("  Exit ")
    print("  Shell")
    print(t2)
def nmapscanner():
    os.system('python3 nmapscanner.py')
if __name__ == "__main__":
    rows, columns = os.popen('stty size', 'r').read().split()
    rows = int(rows)
    os.system('clear')
    print(get_platform())
    banner()
    commandline()
