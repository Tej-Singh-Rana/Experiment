#!/bin/python3



import os

print("Enter the press 6 to reboot your system :")

press=int(input())
if press == 6:
    os.system("reboot")
else:
    print("press wrong key")
































