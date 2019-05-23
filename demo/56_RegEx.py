import re

str = "Match will fixing with 450k"

x = re.findall("[a-m]",str)
print("A set of characters : ",x)

y = re.findall("\d",str)
print("Signals special sequence : ",y)

z = re.findall("Ma..h",str)
print("Search any character, except newline character : ",z)


a = re.findall("^Match",str)
if (a):
    print("Yes, the string start with 'Match'")
else:
    print("No match")


b = re.findall("450k$",str)
if (b):
    print("Yes, the string end with '450k'")
else:
    print("No match")


c = re.findall("wix*",str)
print("\n",c)
if (c):
    print("Yes, there is at least one match")
else:
    print("No match")


d = re.findall("wix+",str)
print("\n",d)
if (d):
    print("Yes, there is at least one match")
else:
    print("No match")


e = re.findall("at{2}",str)
print("\n",e)
if (e):
    print("Yes, there is at least one match")
else:
    print("No match")


f = re.findall("will|stays",str)
print("\n",f)
if(f):
    print("Yes, there is at least one match!")
else:
    print("No match")
