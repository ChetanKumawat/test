# capitalize() method retruns a string where the first character is upper case.
txt = "hello, and welcome to my world"
x = txt.capitalize()
print("\n1. capitalize() method return upper case the first letter in this sentence : ",x)


# casefold() function returns a string where all the characters are lower case.
# casefold() and lower() both methods are similar, but casefold() method more stronger, more aggressive, meaning that it will convert more
# characters into lower case and find more matches while comparing two strings and both are converted using casefold() method.
txt = "Hello, And Welcome To My World"
x = txt.casefold()
print("\n2. casefold() method return lower case the string : ",x)


# center() method will center align the string, using the specified character(space is default) as the fill character.
txt = "banana"
x = txt.center(20)
print("\n3. center() method, print the 'banana', taking up the space of 20 character, with 'banana' in the middle ; ",x)

y = txt.center(20,"O")
print("   Using the letter 'O' as the padding the character : ",y)



# count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apples are my favorite fruits"
x = txt.count("apple")
print("\n4. count() method returns the number of times the value 'apple' appear in the string : ",x)

y = txt.count("apple",10,24)
print("   Search from position 10 to 24 : ",y)



# encode() method encodes the string, using specified encoding. If no encoding is specified UTF-8 will be used.
txt = "My name is Ståle"
x = txt.encode()
print("\n5. UTF-8 encode the string : ",x)


print("\t",txt.encode(encoding="ascii",errors="backslashreplace"))
print("\t",txt.encode(encoding="ascii",errors="ignore"))
print("\t",txt.encode(encoding="ascii",errors="namereplace"))
#print("\t",txt.encode(encoding="ascii",errors="strict"))
#print("\t",txt.encode(encoding="ascii",errors="replace"))
#print("\t",txt.encode(encoding="ascii",errors="xmlcharrefreplace"))



# endswith() method returns True if the string ends with specified value, otherwise False.
txt = "Hello, and welcome to my world."
x = txt.endswith(".")
print("\n6. endswith() method, check if the string ends with punctulation sign (.) : ",x)

y = txt.endswith("my word.",5,11)
print("   Check if position 5 to 11 ends with the phrase 'my word.' : ",y)



# expandtabsize() method sets the tab size to the specified number of whitespace.
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print("\n7. expandtabs() method set the tab size to 2 whitespace : ", x)



# find() method find the first occurance of the specified value.
# find() method return -1 if the value is not found.
# find() method is almost same as index() method, only difference is that the index() method raise an exception if the value is not found.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print("\n8. find() method return the numeric position of the 'welcome' : ",x)

y = txt.find('e')
print("   Where in the text is the first occurrence of the letter 'e' : ",y)

z = txt.find("e",5,10)
print("   Where in the text is the first occurrence of the letter 'e' when you only search between position 5 and 10 ; ",z)

print("   Check  if the value is not found, find() method return -1, but the index() method will raise an exception : ")
print("\t\t\t\t\t\t",txt.find("q"))
#print("\t\t\t\t\t\t",txt.index("q"))



# index() method finds the first occurrence of specified value.
# index() method raise an exception if the value is not found.
# index() method same as find() method, but difference is that find() method return -1 if the value is not found.
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print("\n9. index() method return that where in the text is the word 'welcome' : ",x)


y = txt.index("e")
print("   Where in the text is the first occurrence of the letter 'e' : ",y)

z = txt.index("e",5,11)
print("   Where in the text is the first occurrence of letter 'e' when you only search between position 5 and 10 : ",z)



# islanum() method returns True, if all characters are alphanumeric, meaning alphabet letter(a-z) and numbers(0-9), otherwise False.
txt = "Sector8"
x = txt.isalnum()
print("\n10. isalnum() method return True if all the characters in the "+txt+" text are alphanumeruic : ",x)



# isalpha() method retruns True if all the characters are alphabet letters (a-z).
txt = "NescafeCe"
x = txt.isalpha()
print("\n11. isalpha() method returns True if all characters in the "+txt+" text are alphabet letters : ",x)



# isdecimal() method returns True if all the characters are decimals (0-9).
txt = "\u0033"  #incode for 3
x = txt.isdecimal()
print("\n12. isdecimal() method returns True if all characters in the "+txt+" unicode object are decimals : ",x)
print(" "*94+str(txt.isdecimal()))



# isdigit() method returns True if all the characters are digits, otherwise False.
txt = "32652"
x = txt.isdigit()
print("\n13. isdigit() method return True If all in the "+txt+" are digits : ",x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print("    Check if all the characters in the text  is alphabetics : ",a.isdigit())
print(" "*62,b.isdigit())



# isidentifier() method return True if the string is a valid identifier, otherwise False.
# A string considered a valid identifier if it only contains alphanumerics letters (a-z) and (0-9) or underscore (_).
# A valid identifier cannot start with a number or contain any space.
txt = "Demo"
x = txt.isidentifier()
print("\n14. isidentifier() method check if the string "+txt+"   is a valid identifier : ",x)

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(" "*77,a.isidentifier())
print(" "*77,b.isidentifier())
print(" "*77,c.isidentifier())
print(" "*77,d.isidentifier())



# islower() method returns if all the characters are in lower case, otherwise False.
txt = "hello world"
x = txt.islower()
print("\n15. islower() method return True if all the characters in the "+txt+" text are in lower case : ",x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(" "*3,"Text is "+a+" : ",a.islower())
print(" "*3,"Text is "+b+" : ",b.islower())
print(" "*3,"Text is "+c+" : ",c.islower())




# isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
txt = "526532"
x = txt.isnumeric()
print("\n16. isnumeric() method returns True if all the characters are "+txt+" numeric : ",x)


a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2
c = "\10km2"

print(" "*3,"This is '\u0030' character is numeric : ",a.isnumeric())
print(" "*3,"This is  '\u00B2' character is numeric : ",b.isnumeric())
print(" "*3,"This is '\10km2' character is numeric : ",c.isnumeric())



# isprintable() method returns True if all characters are printable, otherwise False.
txt = "Hello! Are you #1?"
x = txt.isprintable()
print("\n17. isprintable() method returns True if all the characters in the '"+txt+"' text are printable : ",x)


txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(" "*3,"isprintable() method returns True if all the characters in the '"+txt+"' text are printable : ",x)



# isspace() method returns True if all the characters in a string are whitespace, otherwise False.
txt = "   "
x = txt.isspace()
print("\n18. isspace) method return True if all the characters in the text are whitespace : ",x)


txt = "   s   "
x = txt.isspace()
print(" "*3,"Check if all the characters in the '  s  ' text are whitespace : ",x)



# istitle() method returns True if all words in a text start with upper case letter, and rest of the word are lower case letters, otherwise False.
# symbols and numbers are ignored.
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print("\n19. istitle() method, check if each word start with an upper case letter : ",x)


a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(" "*42+a+" : ",a.istitle())
print(" "*67+b+" : ",b.istitle())
print(" "*64+c+" : ",c.istitle())
print(" "*60+d+" : ",d.istitle())



# isupper() method return True if all the characters are in upper case, otherwise False.
# Number, Symbols and Spaces are not checked, only alphabets characters.
txt = "THIS IS NOW!"
x = txt.isupper()
print("\n20. isupper() method, check if all the characters are in upper case : ",x)



a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(" "*55+a+" : ",a.isupper())
print(" "*58+b+" : ",b.isupper())
print(" "*52+c+" : ",c.isupper())



# join() method takes all items in an iterable and joins them into into one string.
# A string must be specified as the separator.
myTuple = ("John","Peter","Vicky")
x = "#".join(myTuple)
print("\n21. join() method join all items in a tuple into a string, using a hash(#) character as separator : ",x)


myDict = {"name":"Jhon","country":"Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print("    Join all items in dictionary into a string, using the word 'TEST' as separator : ",x)

# Note : When using the dictionary as an iterable, the returned values are the keys, not the values.


# ljust() method will left align the string, using specified character (space is default) as the fill character.
txt = "banana"
x = txt.ljust(20)
print("\n22. ljust() method, return a 20 character long, left justify version of the word 'banana' : ")
print(x,"is my favorite fruit.")

y = txt.ljust(20,"O")
print("Using the letter 'O' as the padding the character : ")
print(y)



# lower() method returns a string where all the characters are lower case. Symbols and numbers are ignored.
txt = "Hello my FRIENDS"
x = txt.lower()
print("\n23. lower() method returns a string where all the characters are lower case : ",x)



# lstrip() method removes any leading characters (space is the default leading character to remove)
txt = "    banana     "
x = txt.lstrip()
print("\n24. lstrip() method removes spaces to the left of the string : ")
print("all of fruits",x,"is my favorite")


txt = ",,,,,,ssaaw......banana"
x = txt.lstrip(",.saw")
print("Removes the leading the characters : ")
print(x)



# partition() method searches for a specified string and split the string into a tuple containing three elements.
# First element contains the part before the specified string.
# Second element contains the specified string.
# Third element contains the part after the string.
# Note : This method search for the first occurrence of the specified string.
txt = "I could eat banana all day"
x = txt.partition("banana")
print("\n25. partition() method search for the 'banana' and return a tuple with three elements : \n\t1. Everything before the 'match'\n\t2. The 'match' \n\t3. Everything after the 'match'\n\tResult is : ",x)



y = txt.partition("apples")
print("\n    If the specified value is not found, the partition method retrun a tuple containing :\n\t1. The whole string.\n\t2. An empty string.\n\t3. An empty string.\n\tResult is :",y)




# replace() method replaces a specified phrase with another specified space.
# Note : All occurrences of the specified phrase will be replaced, if nothing else is specified.
txt = "I like mango"
x = txt.replace("mango","apple")
print("\n26. replace() method replace the word 'mango' with 'apple' : ",x)


txt = "one one was a race horse, two two was one too."
y = txt.replace("one","three")
print("    Replace all occurrence of the word 'one' : ",y)


z = txt.replace("one","three",2)
print("    Replace the two first occurrence of the word 'one' : ",z)



# rfind() method finds the last occurrence of the specified value.
# rfind() method returns the -1 if the value is not found.
# rfind() method is almost the same as the rindex() method.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print("\n27. rfind() method find last occurrence of the string 'casa' : ",x)


txt = "Hello, welcome to my world."
y = txt.rfind("e")
print("    Find the last occurrence of the letter 'e' : ",y)


z = txt.rfind("e",5,10)
print("    Find the last occurrence of letter 'e' when you only search between position 5 and 10 : ",z)


print("    If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception :")
print(" "*11,txt.rfind("q"))
try:
    print(txt.rindex("q"))
except:
    print("\t\t\tAn exception occurred.")




# rindex() method find the last occurrence of the specified value.
# rindex() method raises an exception if the value is not found.
# rindex() method is almost same as rfind() method.
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print("\n28. rindex() method fincd last occurrence of the specified value : ",x)


txt = "Hello, welcome to my world."
y = txt.rindex("e")
print("    Find last occurrence of the letter 'e' : ",y)


z = txt.rindex("e",5,10)
print("    Find last occurrence of the letter 'e' when you only search between position 5 and 10 : ",z)


print("    If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception :")
print(" "*11,txt.rfind("q"))
try:
    print(txt.rindex("q"))
except:
    print("\t\t\tAn exception occurred")



# rjust() method will right align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.rjust(20)
print("\n29. rjust() method return a 20 characters long, right justified version of the word 'banana : ")
print(x, "is my favorite fruit")


y = txt.rjust(20,"O")
print("    Using the letter 'O' as the padding character : ")
print(y)



# rpartition() method searches for the last occurrence of a specified string and split the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
txt = "I could eat bananas all day, bananas are my favorite fruite."
x = txt.rpartition("bananas")
print("\n30. rpartition() method search for the last occurrence of the word 'bananas' and return a tuple with three elements : \n\t1. Everything before the match.\n\t2. The match.\n\t3. Everything after the match.\n\tResult is : ",x)


y = txt.rpartition("apples")
print("\n    If the specified value is not found, the rpartition() method returns a tuple containing : \n\t1. The whole string.\n\t2. An empty string.\n\t3. An empty string.\n\tResult is :",y)



# rsplit() method splits a string into a list, starting from the right.
# if no max is specified, this method will return the same as the split() method.
# When max is specified, the list will contain the specified number of elements plus one.
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print("\n31. rsplit() method, split string into a list, using comma, followed by a space(,) as the separator : ",x)


y = txt.rsplit(",",1)
print("    Split the string into a list with maximum 2 items : ",y)



# rstrip() method removes any trailing characters(characters at the end a string) space is default trailing character to remove.
txt = "    banana     "
x = txt.rstrip()
print("\n32. rstrip() method removes spaces to the right of the string : ")
print("\tof all fruits",x,"is my favorite")

txt = "banana,,,,,ssqqqwww...."
y = txt.rstrip(",.sqw")
print("\tRemoves all trailing characters : ")
print("\t",y)



# split() method splits a string into a list.
# You can specify the separtor, default separtor is any whitespace.
# Note : When max is specified, the list will contain the specified number of element plus one.
txt = "Welcome to the jungle"
x = txt.split()
print("\n33. split() method splits a string into a list where each word is a list item : ",x)


txt = "hello, my name is Piter, I am 26 year old"
y = txt.split(", ")
print("\tSplit the string, using comma, followed by a space, as a separator : ",y)


txt = "apple#banana#cherry#orange"
z = txt.split("#")
print("\tUse a hash character as separator : ",z)


a = txt.split("#",1)
print("\tSplit the string into a list with max 2 items : ",a)



# splitlines() method splits a string into a list. The spliting is done at line breaks.
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print("\n34. splitlines() method split a string into a list where each lines is a list item : ",x)


y = txt.splitlines(True)
print("\tSplit the string, but keep the lines breaks : ",y)



# startswith() method ireturn True if the string end with the specified value, otherwise False.
txt =  "Hello, welcome to my world"
x = txt.startswith("Hello")
print("\n35. startswith() method return True if string start with 'Hello' : ",x)

y = txt.startswith("wel",7,20)
print("\tCheck if position 7 to 20  starts with the characters 'wel' : ",y)



# strip() method removes any leading space(spaces at the beignning) and trailing(spaces at the end) characters(space is default leading character to remove)
txt = "   banana   "
x = txt.strip()
print("\n36. strip() method removes space at the beginning and end of the string : ",x)


txt = ",,,,,rrttggg......banana..rrrrr"
y = txt.strip(",.rtg")
print("\tRemoves the trailing and leading characters : ",y)



# swapcase() method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print("\n37. swapcase() method, make the lower case letter upper case and the upper case letter lower case : ",x)



# title() method returns a string where the first character in every word is upper case. Like a header or title.
# If the word contains a number or a symbol, the first letter after that will converted to upper case.
txt = "Welcome to my world"
x = txt.title()
print("\n38. title() method, make the first letter in each word upper case : ",x)


txt = "Welcome to my 2nd world"
y = txt.title()
print("\tMake the first letter in each word upper case : ",y)


txt = "hello b2b2b2 and 3g3g3g"
z = txt.title()
print("\tThe first letter after a non alphabet letter is converted into a upper case letter : ",z)



# upper() method returns a string where all characters are in upper case. Symbols and numbers are ignored.
txt = "Hello my friend"
x = txt.upper()
print("\n39. upper() method convert all characters of string in upper case : ",x)



# zfill() method adds zero(0) at the beginning of the string, until it reaches the specified length.
# if the value of the len parameter is less than the length of the string, no filling is done.
txt = "50"
x = txt.zfill(10)
print("\n40. zfill() method fill the string with zero until it is 10 character long : ",x)