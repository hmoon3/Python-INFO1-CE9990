"""
solarsystem.py
assignment #6
creates a dictionary from a json file
provides information about the sun and planets in the solar system
"""

import sys
import json
import urllib.request

url = "https://raw.githubusercontent.com/duckduckgo/zeroclickinfo-goodies/" \
      "master/share/goodie/cheat_sheets/json/solar-system.json"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = lines.read()         #Read the entire input file.
lines.close()

try:
    s = sequenceOfBytes.decode("utf-8") #s is a string.
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

try:
    solarsystem = json.loads(s)          #dictionary is a dictionary.
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)

body = input("What is the celestial body you are looking for? ").title()

def printInfo(body):
    print("Here is some information about ", body, ":", sep = "")
    for i in range(len(solarsystem["sections"][body])):
        dict = solarsystem["sections"][body][i]
        print(dict["key"], ": ", dict["val"], sep = "")

if body == "Pluto":
    print("Sorry,", body, "is no longer classified as a planet")
elif body in solarsystem["sections"]:
    printInfo(body)
else:
    print("Sorry, could not find", body)
    sys.exit(1)

sys.exit(0)
