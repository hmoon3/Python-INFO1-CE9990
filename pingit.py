"""
pingit.py
assignment #7
calls the os.popen function to launch another program
pings a domain or ip address and prints output to screen
"""

import sys
import os

pingit = "ping -c3 " + input("What is the domain/ip address you need to test? ")

infile = os.popen(pingit)   #Create a child process and a pipe.
lines = infile.readlines()           #lines is a list of lines.
status = infile.close()

lines = [line.rstrip() for line in lines]       #Remove trailing newline.

for i, line in enumerate(lines):
    print("{}".format(line))
    
sys.exit(0)
