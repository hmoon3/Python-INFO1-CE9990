"""
control.py
assignment #2
utilizing if statements check if a user provided name signed the Declaration of Independence
"""

import sys
import urllib.request

url = "http://www.ushistory.org/declaration/document/index.html"
name = input("What is the name you are searching for? ")


try:
    site = urllib.request.urlopen(url)
except urllib.error.URLError:
    print("ERROR. unable to access site.")
    sys.exit(1)
    
for line in site:
    content = line.decode("utf-8")
    if name.title() in content:
        print(name, "was a signer of the Declaration of Independence.", end="")
        break
else:
    #Arrive here if the for loop never executed the break.
    print(name, "did not sign the Declaration of Independence.", end="")

site.close()
sys.exit(0)
