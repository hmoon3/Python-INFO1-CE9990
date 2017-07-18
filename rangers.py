"""
rangers.py
assignment #5
create a list that holds information in rows and columns
loads the roster for the 2016-2017 NY Rangers from a csv file
source: https://www.hockey-reference.com/teams/NYR/2017.html#roster
expanding the Share & more submenu gives you the csv option
"""

import sys
import csv
import re

file = "/Users/Username/Desktop/roster.csv"

try:
    csvfile = open(file, 'r', encoding='utf-8')
except FileNotFoundError:
    print("ERROR! File not found.")
    sys.exit(1)
except PermissionError:
    print("ERROR! You do not have permission to access this file.")
    sys.exit(1)

country = {
    "ca": "Canada",
    "ru": "Russia",
    "us": "USA",
    "at": "Austria",
    "se": "Sweden",
    "cs": "Slovakia", #made small change because source website incorrectly listed country as Czechoslovakia
    "dk": "Denmark",
    "fi": "Finland",
    "no": "Norway"
    }
    
def formatOutput(line):
    #format the output to print only a few select fields
    print("Name: ", line[1].split("\\")[0])
    print("Number: ", line[0])
    print("Position: ", line[3])
    print("Shoots/catches: ", line[7])
    print("Country: ", country[line[2]]) #added a dictionary because country abbreviation was not easily readable
    print("Summary: ", line[-1])
    print()
   
lines = csv.reader(csvfile, delimiter = ",")

roster = [line for line in lines]          
csvfile.close()
roster = roster[1:]
print("The 2016-17 New York Rangers were:")

for line in roster:
    formatOutput(line)

sys.exit(0)
