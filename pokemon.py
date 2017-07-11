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
except PermissionError:
    print("ERROR! You do not have permission to access this file.")
    sys.exit(1)

pokedex = []

for line in kanto:
    #populate list from text file
    pokedex.append(line.strip())
    
kanto.close()

def sorter(alpha, reverse):
    #twoColumns is a list of tuples (i.e., a list of pairs).
    twoColumns = [(i, pokemon) for (i, pokemon) in enumerate(pokedex, start = 1)]
    if alpha:
        twoColumns.sort(key = lambda t: t[1])
    if reverse:
        twoColumns.reverse()
    for (i, pokemon) in twoColumns:
        print("#{:03} {}".format(i, pokemon))
#Each key is a string containing one character.
#Each value is a tuple containing two bools.

dictionary = {
    'a': (False, False), #ascending numeric
    'b': (False, True),  #descending numeric
    'c': (True, False),  #ascending alphabetical
    'd': (True, True)    #descending alphabetical
}

def sortPokedex(initial):
    prompt = """\
    How do you want to sort your pokédex?
    a) numerical order(low to high)
    b) numerical(high to low)
    c) alphabetical(a-z)
    d) alphabetical(z-a): """
    query = input(prompt)
    try:
        sorter(*dictionary[query])
    except KeyError:
        print("Bad entry", query)
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
