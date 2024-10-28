"""
this contains all code for chapter 9 challenges.
Roy P. Murphy september 2024
"""

import csv

# exercise 1
with open("self_taught_08.py","r") as f:
    print(f.read())

print()

# exercise 2
answer = input("what is your name?: ")
with open("challenge_2.txt","w") as f:
    f.write(answer)

with open("challenge_2.txt","r") as f:
    print(f.read())
    
print()

# exercise 3
list_of_lists =[["TG","RB","MR"],
                ["T","TR","I"],
                ["TD","MOF","F"]]

with open("lists.csv","w",newline='') as f:
    w=csv.writer(f,delimiter=",")
    for li in list_of_lists:
        w.writerow(li)

with open("lists.csv","r") as f:
    print(f.read())

print()


