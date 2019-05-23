import re

str = "The rain in Spain"

# Check if the sting start with 'The'
x = re.findall("\AThe", str)
print(x)
if (x):
    print("Yes, there is a match\n")
else:
    print("No match\n")


# Check if 'ain' is present at the begining of the word.
y = re.findall(r"\bain",str)
print(y)
if(y):
    print("Yes, there is at least one match\n")
else:
    print("No match\n")

# Check if 'ain' is present at the end of the word.
z = re.findall(r"ain\b",str)
print(z)
if(z):
    print("Yes, there is at least one match\n")
else:
    print("No match\n")


# Check if 'ain' is present, but NOT at the beginning of the word.
a = re.findall(r"\Bain",str)
print(a)
if(a):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")


# Check if 'ain' is present, but NOT at the end of the word.
b = re.findall(r"ain\B",str)
if(b):
    print("Yes, there is at least one match!\n")
else:
    print("No match!\n")


# Check if string contain any digits (number from 0-9).
c = re.findall("\d",str)
print(c)
if(c):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")


# Return a match at every no-digit character.
d = re.findall("\D",str)
print(d)
if(d):
    print("Yes, there is at least one match!\n")
else:
    print("No match\n")

# Return a match at every white space character:
e = re.findall("\s",str)
print(e)
if(e):
    print("Yes, there is at least one match!\n")
else:
    print("No match\n")


# Return a match at every NON white space character:
f = re.findall("\S",str)
print(f)
if(f):
    print("Yes, there is at least one match!\n")
else:
    print("No match\n")


# Retrun a match at every word character (character from a-z, digits from 0-9, and underscore _ character:
g = re.findall("\w",str)
print(g)
if(g):
    print("Yes, there is at least one match!\n")
else:
    print("No match.")


# Return a match at every non word character (charactwer NOT between a and z, Like "!","?" white-space etc.
h = re.findall("\W",str)
print(h)
if(h):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")


#Check if the string ends with "Spain":
i = re.findall("Spain\Z",str)
print(i)
if(i):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")


# Check if the string has any a, r or n characters
j = re.findall("[arn]",str)
print(j)
if(j):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")


# Check if the string has any character between a and n:
k = re.findall("[a-n]",str)
print(k)
if(k):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")


# Check if the string has other character than a, r or n :
l = re.findall("[^arn]",str)
print(l)
if(l):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")


# Check if the string has any 0, 1, 2 or 3 digits:
m = re.findall("[0123]",str)
print(m)
if(m):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")


# Check if the string has any digits:
digi = "8 times before 11:45 AM"
n = re.findall("[0-9]",digi)
print(n)
if(n):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")



# Check if the string has any two digit numbers, from 00 to 59:
o = re.findall("[0-5][0-9]",digi)
print(o)
if(o):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")



# Check if the string has any characters from a to z lower case and A to Z upper case:
p =re.findall("[a-zA-Z]",digi)
print(p)
if(p):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")


# Check if the string has any + characters:
q = re.findall("[+]",digi)
print(q)
if(q):
    print("Yes, there is at least one match!\n")
else:
    print("No match.\n")