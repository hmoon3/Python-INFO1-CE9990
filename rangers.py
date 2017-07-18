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
roster = []

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
    
def name(n):
    # the name field in the csv file has a weird abbreviation at the end that needs to be removed
    name = roster[n][1].split("\\")
    return name[0]
 
def formatOutput(n):
    #format the output to print only a few select fields
    print("Name: ", name(n))
    print("Number: ", roster[n][0])
    print("Position: ", roster[n][3])
    print("Shoots/catches: ", roster[n][7])
    print("Country: ", country[roster[n][2]]) #added a dictionary because country abbreviation was not easily readable 
    print("Summary: ", roster[n][-1])
    print()
    
lines = csv.reader(csvfile, delimiter = ",")
          
for line in lines:
    #build our list of lists from the csv file
    roster.append(line)
          
csvfile.close()

print("The 2016-17 New York Rangers were:")

for i in range(len(roster) - 1):  #first line in the csv is actually the field descriptions so need to offset by one
          formatOutput(i+1)

sys.exit(0)
