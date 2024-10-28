"""
end of chapter exercises for chapter 6 self_taught programmer.
All exercise coded here.
"""

# exercise 1
s = "Camus"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print()

# exercise 2
s1 = input("give me a word: ")
s2 = input("give me a word: ")
s = "Yesterday I wrote a {}. I sent it to {}."
s = s.format(s1,s2)
print(s)
print()

# exercise 3
s = "aldous huxley was born in 1894"
s = s.capitalize()
print(s)
print()

# exercise 4
s = "Where now?Who now?When Now"
l = s.split("?")
print(l)
print()

# exercise 5
l = ["The", "fox", "jumped", "over", "the", "fence", "."]
s = " ".join(l)
s=s.replace(" .",".")
print(s)
print()

# exercise 6
s = "A screaming comes across the sky"
s=s.replace("s","$")
print(s)
print()

# exercise 7
s = "hemingway"
n = s.index("m")
print(n)
print()

# exercise 8
s = "How do I get out of this \"chickenshit\" outfit"
print(s)
print()

# exercise 9
t = "three"
s = " "
threes = t+s+t+s+t
print(threes)

threes=(t+s)*3
threes = threes.strip()
print(threes)
print()

# exercise 10
s = "It was a bright cold day in April, and the clocks were striking thirteen"
new_s = s[:33]
print(new_s)
print()

