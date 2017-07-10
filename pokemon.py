"""
pokemon.py
assignment #4
inputs all the lines of a text file and sorts them
lists all 151 first generation Pokémon
can be sorted either in alphabetical or numerical order
in ascending or descending order
or search for the pokédex number of a particular pokémon
kanto.txt used has been uploaded to this repository
"""

import sys

file = "/Users/Username/Desktop/kanto.txt"

try:
    kanto = open(file, 'r', encoding='utf-8')
except FileNotFoundError:
    print("ERROR! File not found.")
    sys.exit(1)

pokedex = []

for line in kanto:
    #populate list from text file
    pokedex.append(line.strip())
    
kanto.close()

def ascending():
    #prints pokémon in ascending numerical order
    print("Pokémon in ascending numerical order:")
    for i, pokemon in enumerate(pokedex, start = 1):
        print("#"+"{:03} {}".format(i, pokemon))
        
def descending():
    #prints pokémon in descending numerical order
    reversedPokedex = reversed(pokedex)
    print("Pokémon in descending numerical order:")
    for pokemon in reversedPokedex:
        print("#"+"{:03} {}".format(pokedex.index(pokemon) + 1, pokemon))

def alpha():
    #prints pokémon in alphabetical order
    sortedPokedex = sorted(pokedex)
    print("Pokémon sorted in alphabetical order:")    
    for pokemon in sortedPokedex:
        print("#"+"{:03} {}".format(pokedex.index(pokemon) + 1, pokemon))
     
def reverseAlpha():
    #prints pokémon in reverse alphabetical order
    reversedAlphadex = reversed(sorted(pokedex))
    print("Pokémon in reverse alphabetical order")
    for pokemon in reversedAlphadex:
        print("#"+"{:03} {}".format(pokedex.index(pokemon) + 1, pokemon))

def sortPokedex(initial):
    query = input("How do you want to sort your pokédex? a) numerical order(low to high) b) numerical(high to low) c) alphabetical(a-z) d) alphabetical(z-a): ")
    if query == "a":
        ascending()
    elif query == "b":
        descending()
    elif query == "c":
        alpha()
    elif query == "d":
        reverseAlpha()
    else:
        print("ERROR! Bad entry")
        sys.exit(1)

def searchPokedex():
    query = input("Which pokémon are you looking for?: ")
    if query not in pokedex:
        print("ERROR! Pokémon not found")
        sys.exit(1)
    print("The pokédex number for", query, "is", pokedex.index(query) + 1)


initial = input("Do you want to a) list all pokémon or b) search for a particular one? ")

if initial == "a":
    sortPokedex(initial)
elif initial == "b":
    searchPokedex()
else:
    print("ERROR! Bad entry")
    sys.exit(1)

sys.exit(0)
    
 
