"""
self taught chapter 17.
Regular expressions.
Roy P Murphy 26/10/2024
"""

import re

# exercise 1
with open("zen.txt", "r") as f:
    text = f.read()
    matches = re.findall("Dutch",text)
    print(matches)

# exercise 2
s = "Arizona 479, 501, 870. California 209, 213, 650."
pattern = r"\d+"
matches = re.findall(pattern,s)
print(matches)

# exercise 3
s = "The ghost that says boo haunts the loo"
pattern = r".oo.*?"
matches = re.findall(pattern,s)
print(matches)


