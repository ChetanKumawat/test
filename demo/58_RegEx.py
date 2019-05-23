import re

# Return a list containing every occurrence of 'ai'

str = "The rain in spain"

x = re.findall("ai",str)
print(x)
if(x):
  print("Yes, there is at least one match!\n")
else:
  print("No match\n")



#Check if "Portugal" is in the string:
y = re.findall("Portugal",str)
print(y)
if(y):
    print("Yes, there is at least one match!\n")
else:
  print("No match\n")



# Check the first white space in the string :
z = re.search("\s",str)
print("The first white spcae character is located in position:",z.start())



# Check split the string at every white space character :
a = re.split("\s",str)
print(a)



# Check split the string at every white space character and you can control the number of occurrence by specifing maxsplit parameter:
b = re.split("\s",str,1)
print(b)


# Replace all white space character with the digit "9":
c = re.sub("\s","9",str)
print(c)


# Contrl the number of replacement by specifing the count parameter
# Replace the first two occurrence of white space character with the digit 9:
d = re.sub("\s","9",str,2)
print(d)



# Search() function return a match object;
e = re.search("ai",str)
print(e)



# Search for an upper case "S" character in the beginning of a word and print its position :
str = "The rain in Spain"
f = re.search(r"\bS\w+", str)
print(f.span())


# Retrun the string passed into the function
g = re.search(r"\bS\w+",str)
print(g.string)


# Print part of the string where there was a match.
# Search for the upper case "S" character in the beginning of the word, print the word !
h = re.search(r"\bS\w+",str)
print(h.group())
