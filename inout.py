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
    except ValueError:
        print("BAD VALUE ", lb, "! EXITING NOW!!!", sep = "" )
        sys.exit(1)
    total += lb
    print("You have", total, "ladybugs so far.")
