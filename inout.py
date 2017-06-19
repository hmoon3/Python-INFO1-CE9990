"""
inout.py

first homework assignment

"""

import sys

total = 0
while True:
    lb = input("How many ladybugs are there? ")
    try:
        lb = int(float(lb)) 
        total += lb
    except ValueError:
        print("BAD VALUE! EXITING NOW!!!" )
        sys.exit(1)
    print("you have", total, "ladybugs so far")
