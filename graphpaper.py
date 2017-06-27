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

if rows == 0 or columns == 0 or rs == 0 or cs == 0:
    print("ERROR. You cannot have a blank value")
    sys.exit(1)
    
while rows > 0:
    tc = columns
    while tc > 0:
        print("+", rs * "-", sep = "", end = "")
        tc -= 1
    print("")
    ttc = columns
    while ttc > 0:
        print("!", rs * " ", sep = "", end = "")
        ttc -= 1
    print("")
    rows -= 1
