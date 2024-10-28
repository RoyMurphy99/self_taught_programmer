def squ(x):
    """
    return x squared
    """
    return float(x)**2

def prtStr(x):
    """
    print the string x passed to the function
    """
    print(x)

def required(x,y,z,a=1,b=2):
    """
    required parameters: x,y,z
    optional parameters: a,b
    print the values of all parametsrs
    """
    print(x)
    print(y)
    print(z)
    print(a)
    print(b)

def f1(x):
    """
    required parameters: x a number
    f1 returns x/2
    """
    return x/2

def f2(x):
    """
    required parameters: x a number
    f2 returns x*4
    """
    return x*4

def str_to_float(x):
    """
    required parameters: x a string that can be converted to a float
    str_to_float converts x to a float
    """
    try:
        s = float(x)
        print(s)
    except ValueError:
        print("string cannot be converted to a float")

# challenge 1
x = input("pick a number: ")
print(squ(x))

# challenge 2
print("")
x = input("type in a string: ")
prtStr(x)

# challenge 3
print("")
required(100,200,300,a=1000)

# challenge 4
print("")
y = f1(2)
print(y)
z = f2(y)
print(z)

# challenge 5
print("")
x = input("enter a string that can be converted to a float: ")
str_to_float(x)
