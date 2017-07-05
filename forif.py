"""
forif.py
assignment #3
illustrate for and if statements
given a sentence, count the number of words
"""

import sys

sentence = input("Please provide a sentence: ")

if sentence == "":
    print("You must input something!")
    sys.exit(1)

n = sentence.count(" ")
vowels = 0
for character in sentence:
    if character in "aeiouy":
        vowels += 1

print("There are", n + 1, "words in your sentence.")
print("There are", vowels, "vowels in your sentence.")

sys.exit(0)

