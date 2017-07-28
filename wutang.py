"""
wutang.py
assignment #7
read a json file from the web into a dictionary
returns information about the Wu-Tang Clan
"""

import sys
import json
import urllib.request

url = "https://raw.githubusercontent.com/duckduckgo/zeroclickinfo-goodies/" \
      "master/share/goodie/cheat_sheets/json/wu-tang.json"

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
    wutang = json.loads(s)          #dictionary is a dictionary.
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)

print(wutang["description"])
for dictionary in wutang["sections"]["Members"]:
    print(dictionary["key"], ": ", dictionary["val"], sep = "")

sys.exit(0)
