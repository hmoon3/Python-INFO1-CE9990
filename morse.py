"""
morse.py
assignment #7
read a json file from the web into a dictionary
converts text into morse code
"""

import sys
import json
import urllib.request

url = "https://raw.githubusercontent.com/duckduckgo/zeroclickinfo-goodies/" \
      "master/share/goodie/cheat_sheets/json/morse-code.json"

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
    morsecode = json.loads(s)          #dictionary is a dictionary.
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)

       
def convPunct(punctuation):
    #need to convert punctuation symbols separately because the json file has punctuation written out
    #left and right parentheses seem to be the same in morse code 

    punct = {
        ",": "Comma",
        ":": "Colon",
        "?": "Question Mark",
        "'": "Apostrophe",
        "-": "Hyphen",
        "/": "Forward slash",
        "(": "Parentheses",
        "\"": "Quotation Mark",
        "@": "At sign",
        "=": "Equals sign"
        }
    return punct[punctuation]


morsechart = morsecode["sections"]["Alphabet"] + morsecode["sections"]["Digit"] + morsecode["sections"]["Punctuation Mark"]

text = list(input("Input some text: ").upper())

translated = []
for i in text:
    for dictionary in morsechart:
        if i in ",:?'-/(\"(@-":
            i = convPunct(i)  # python is interpretive so it will go on to next if statement with updated i value
        if i == dictionary["key"]:
            translated.append(dictionary["val"] + " ")

print("Here is your text translated to Morse code: ")
print("".join(translated))

sys.exit(0)
