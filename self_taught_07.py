"""
chapter 7 exercises.
All in this file.
"""

# exercise 1
shows = ["the walking dead", "Entourage","The sopranos", "The vampire Diaries"]
for show in shows:
    print(show)
print()

# exercise 2
for i in range(25,51):
    print(i)
print()

# exercise 3
for index,show in enumerate(shows):
    print(index, show)
print()

# exercise 4
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
while True:
    num = input("Enter a number: ")
    if num == "q" or num == "Q":
        break
    num = int(num)
    if num in num_list:
        print("you guessed correctly")
    else:
        print("you guessed incorrectly")
print()

# exercise 5
list1 = [8,19,148,4]
list2 = [9,1,33,83]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i*j)
print(list3)
print()
                     


    
