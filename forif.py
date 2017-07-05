"""
forif.py
assignment #3
illustrate for and if statements
given a sentence, count the number of words
"""

import sys

sentence = input("Please provide a sentence: ")

if sentence == "":
    print("You must input something! ")
    sys.exit(1)

x = 1
for letters in sentence:
    if letters == " ":
        x += 1

print("There are", x, "words in your sentence.", end = "") 

sys.exit(0)

