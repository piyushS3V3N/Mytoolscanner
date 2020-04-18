#!/usr/bin/env python3
import os
import sys
import time
def Main():
    platform = sys.platform

    if platform == 'Linux' or platform == 'linux':
        print('Linux System Detected !! \n Running Scripts Now......')
        time.sleep(2)
        os.system("clear")
        os.system("python3 sysfil/linux");
    elif platform == 'win64' or platform == 'win32':
        os.system("python3 sysfil/windows.py")
        print('Windows is not supported yet')
    else:
        print("Error Unsupported Platform")

if __name__ == "__main__":
    Main()
