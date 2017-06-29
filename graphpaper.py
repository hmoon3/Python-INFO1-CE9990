"""
graphpaper.py
assignment #2
create a graph paper with user-defined dimensions
"""

import sys


try:
    rows = int(input("How many rows of boxes? "))
    columns = int(input("How many columns of boxes? "))
    rs = int(input("How many rows of spaces in each box (e.g., 1)? "))
    cs = int(input("How many columns of spaces in each box (e.g., 3)? "))
except ValueError:
    print("ERROR. That is not a valid number" )
    sys.exit(1)

if rows == 0 or columns == 0 or rs == 0 or cs == 0:
    print("ERROR. You cannot have a zero value")
    sys.exit(1)
    
while rows > 0:
    tc = 0
    while tc < columns:
        print("+", cs * "-", sep = "", end = "")
        tc += 1
    print()
    tcs = 0
    while tcs < rs:
        ttc = 0
        while ttc < columns:
            print("|", cs * " ", sep = "", end = "")
            ttc += 1
        print()
        tcs += 1
    rows -= 1

sys.exit(1)
