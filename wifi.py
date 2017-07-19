"""
wifi.py
assignment #5
takes input from the user, and returns the closest wi-fi hotspot using the
NYC Wi-Fi Hotspot Locations database from the NYC Open Data database
"""

import sys
import csv
import urllib.request

url = "https://data.cityofnewyork.us/api/views/yjub-udmw/rows.csv" 
     
try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

def hotSpot(line):
    #prints wifi information in easily readable format
    print("Provider:", line[3])
    print("Street:", line[5])
    print("Location:", line[10])
    print("SSID:", line[13])
    print()


borough = {
    "a": "MN",
    "b": "BX",
    "c": "QU",
    "d": "BK",
    "e": "SI"
        }

prompt = """\
What is your borough?
a) Manhattan
b) Bronx
c) Queens
d) Brooklyn
e) Staten Island    
"""

boroname = input(prompt)
street = input("What is your street? ")

wifi = []
for line in lines:
    try:
        s = line.decode("utf-8")    #s is a string
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)
    r = csv.reader([s])         #[s] is a list containing one string
    fields = next(r)
    if fields[1] == borough[boroname] and street in fields[5]:  #the borough code is absolute, but street names can be a little vague
        wifi.append(fields)

lines.close() 

if len(wifi) > 0:
    print("These are the wi-fi hotspots near your location: ")
    for i in range(len(wifi)):
        hotSpot(wifi[i])
else:
    print("Sorry, could not find any wi-fi hotspots near your location")

sys.exit(0)
