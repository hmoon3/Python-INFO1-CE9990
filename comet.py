"""
comet.py
assignment #4
use nested loops and a list of strings to output an increasing song
Prologue from Natasha, Pierre, & the Great Comet of 1812
lyrics by David Malloy
Now playing at the Imperial Theatre
source: https://genius.com/Dave-malloy-prologue-annotated
"""

import sys

def intro():
    #prints the intro verse
    for i in range(2):
        print("There’s a war going on")
        print("Out there somewhere")
        print("And Andrey isn’t here")
    print()

def da():
    #prints the da da da verse
    for i in range(3):
        print("Da", "da " * 2)
    print()

def chorus():
    #prints the chorus
    print("And this is all in your program")
    print("You are at the opera")
    print("You're gonna have to study up a little bit")
    print("If you wanna keep with the plot")
    print("'Cause it’s a complicated Russian novel")
    print("Everyone’s got nine different names")
    print("So look it up in your program")
    print("We’d appreciate it, thanks a lot")
    da()

def pierre():
    #just prints the Pierre line
    print("What about Pierre?")

def singer(n):
    #prints who is singing, denoted by brackets and all caps
    print("[", person[n].upper(), "]")

def verse(n):
    #prints the repeating verses
    print(desc[n])
    print()
    singer(1)
    print(desc[n])
    print()
    

def stanza(n):
    #prints the increasing stanzas
    for i in range(n,0,-1):
        if person[-i] == "Andrey":
            print("and", person[-i] + role[-i])
        else:
            print(person[-i] + role[-i])
    print()

person = [
    "Pierre",
    "All",
    "Balaga",
    "Bolkonsky",
    "Mary",
    "Dolokhov",
    "Hélène",
    "Anatole",
    "Marya",
    "Sonya",
    "Natasha",
    "Andrey"
    ]


role = [
    " is fun",
    " is crazy",
    " is plain",
    " is fierce",
    " is a slut",
    " is hot",
    "'s oldschool",
    "'s good",
    "'s young",
    " isn't here"
    ]

desc = [
    "She loves Andrey with all her heart",
    "Natasha's cousin and closest friend",
    "Natasha's godmother, strict yet kind",
    "He spends his money on women and wine",
    "Anatole's sister, married to Pierre",
    "Anatole's friend, a crazy good shot"
    ]

for i in range(2):
    print("[", person[i].upper(), "]")
    intro()

chorus()

j = 2 
for i in range(len(role), 1, -1):
    if person[i] == "Natasha":
        print(person[i] + "!")
        print()
        singer(i)
        print(person[i], "is young")
        verse(j-2)
        stanza(j) #can't put stanza at end of loop because not all verses follow the same structure
    if person[i] == "Sonya":
        singer(i)
        print(person[i], "is good")
        verse(j-2)
        stanza(j)
    if person[i] == "Marya":
        singer(i)
        print(person[i], "is oldschool")
        print("A grande dame of Moscow")
        verse(j-2)
        stanza(j)
        chorus()
    if person[i] == "Anatole":
        print(person[i] + "!")
        print()
        singer(i)
        print(person[i], "is hot")
        verse(j-2)
        stanza(j)
    if person[i] == "Hélène":
        singer(i)
        print(person[i], "is a slut")
        verse(j-2)
        stanza(j)
    if person[i] == "Dolokhov":
        singer(i)
        print(person[i], "is fierce, but not too important")
        verse(j-2)
        stanza(j)
        print("Chandeliers and caviar, the war can’t touch us here")
        print()
        print("Minor characters!")
        print()  
        singer(i-2)  #need to place here because Bolksonsky and Mary switch places in the verses
        print("Old Prince Bolkonsky is crazy")
        print()
    if person[i] == "Mary":
        singer(i)
        print("And Mary is plain")
        print()
        print("[ ", person[i].upper(), "&", person[i-1].upper(), " ]")
        print("Andrey’s family")
        print("Totally messed up")
        print()
    if person[i] == "Balaga":
        singer(i)
        print("And Balaga’s just for fun!")
        print()
        singer(1)
        print("Balaga’s just for fun!")
        print()
        stanza(j)
    j += 1

pierre()
print("Dear, bewildered and awkward Pierre?")
pierre()
print("Rich, unhappily-married Pierre?")

for i in range(3):
    pierre()
    
sys.exit(0)
