# getattr() function return the value of specified attribute from the specified object.
class person:
    name = "Pole"
    age = "25"
    country = "India"

a = getattr(person,'age')
b = getattr(person,'name')
c = getattr(person,'company','BDB')
print(str(b)+" age is "+str(a))
print(str(b)+" company name is "+str(c))


# globals() function returns the global symbol table as a dictionary.
d = globals()
print("\nPrint the global symbol table : ")
print(d)


# hasattr() function return True if specified object has specified attribute otherwiise False.
# Check the pers object has the age property
class pers:
    name = "Doy"
    age = 36
    country = "Canada"

e = hasattr(pers,'age')

print("\nReturn True if if specified object has specified attribute : "+str(e))



# hash() function return the hash value of the object.
print("\nhash() function return the hash value of the object :  ")
print(hash(125))
print(hash(36.25))
print(hash("Analytics"))


# hex() function convert the specified number into a hexadecimal value.
f = hex(365)
print("\nConvert 365 into hexadecimal value : "+f)


# id() function return the unique id for specified object.
g = ('apple','banana','cherry')
h = id(g)
print("\nReturn the unique id of a tuple object : ",h)


# input() function allowing user input
print('\nEnter your name:')
i = input()
print('Hello, '+i)


# int() function convert specified value into an integer number.
j = int(3.6)
print("\nConvert the number 3.6 into an integer : "+str(j))


# isinstance() function return True if specified object is an instance of specified object, otherwise False
k = isinstance(5, int)
print("\nCheck if 5 number is true : ",k)


l = isinstance("Hello",(float,int,str,list,dict,tuple))
print("Check if 'Hello' is one of the type decribed in the type parameter : "+str(l))


class myObj:
    name : "John"

m = myObj()

n = isinstance(m,myObj)
print("Check if m is instance of myObj : "+str(n))



# issubclass() function returns True if the specified objects is a subclass of the specified object, otherwise False.
class myAge:
    age = 36

class myObje(myAge):
    name = "Richard"
    age = myAge

o = issubclass(myObje,myAge)

print("\nCheck if the 'myobje' is a subclass of 'myAge' : "+str(o))



# iter() function returns an iterator object
q = iter(["apple","banana","cherry"])
print("\nCreate an iterator object and print the items : ",next(q))
print(" "*49+next(q))
print(" "*49+next(q))


# len() function return the number of item in an object.
mylist = ["apple","banana","cherry"]
r = len(mylist)
print("\nRetrun the number of items in a list : ",r)


# list() function create a list object.
print("\n Create a fruit list")
s = list(("apple","banana","cherry"))
print(s)


# locals() function return the local symbol table.
t = locals()
print("\n Print the local symbol table : ",t)


# map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
def myfunc(a):
    return len(a)

n = map(myfunc,('apple','banana','cherry'))

print("\nCalculate the length of the each word in the tuple : ")
print(n)
    # convert the map into a list for readabilty
print(list(n))



def myfunc1(a,b):
    return a + b
x = map(myfunc1,('apple','banana','cherry'),('orange','lemon','pineapple'))
print("\nMake new fruits by sending two iterable objects into the function : ")
print(x)
print(list(x))



# max() function return the items with highest value.
x = max(5,2)
print("\nReturn the largest number : ",x)

y = max("Tom","Jerry","Dom")
print("Return the name with higest value, ordered alphabetically : ",y)

tuple = (1,2,3,4,5)
z = max(tuple)
print("Return item in a tuple with the highest value : ",z)



# memoryview() function return a memory view object from a specified object.
x = memoryview(b"hello")
print("\nCreate and print memoryview object : ")
print(x)
print(x[0])
print(x[1])



# min() function return the item with lowest value.
x = min(5,2)
print("\nReturn the lowest number : ",x)

y = min("Tom","Jerry","Dom")
print("Retrun the name with lowest value, ordered alphabetically : ",y)

tuples = (1,5,2,7)
z =  min(tuples)
print("Return item in a tuple with the lowest value : ",z)



# next() function return the next item in an iterator.
mylist1 = iter(["apple","banana","cherry"])
x = next(mylist1)
print("Create the iterator and print the item one by one : ",x)
x = next(mylist1)
print(" "*52,x)
x = next(mylist1)
print(" "*52,x)


mylist2 = iter(["apple","banana","cherry"])
x = next(mylist2,"orange")
print("Return a default value when the iterator has reached to its end : ",x)
x = next(mylist2,"orange")
print(" "*66,x)
x = next(mylist2,"orange")
print(" "*66,x)
x = next(mylist2,"orange")
print(" "*66,x)


# object() function return the empty object
# you cannot add new properties or methods to this objects.
# This object is the base for all classes, it hold the built-in the properties and methods which are default for all classes.
x = object()
print(dir(x))


# oct() function convert an integer into an octal string
x = oct(12)
print("\noct() function convert the 12 number into octal value : ",x)


# open() function opens a file and return it as a file object.
f = open("demofile1.txt","r")
print("\n")
print(f.read())


# ord() function return the number representing the unicode number of a specified character.
x = ord("h")
print("\nord() function the integer that represent the character 'h' : ",x)


# pow() function return the value of 'x' to the power of 'y'
x = pow(4,3)
print("\npow() function the value of 4 to the power of 3 : ",x)


# if third parameter is present in pow() function, it retruns x to power of y, modulus z.
x = pow(4, 3, 5)
print("\npow() function return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5) : ",x)


# range() function returns a sequence of a number, starting from 0 by default & increment by 1 (by default) & ends at a specified number.
x = range(6)
count=0
for n in x:
    if count==0:
        print("\nCreate a sequence of numbers from 0 to 5, & print each item in the sequence : ",n)
    else:
        print(" "*79+str(n))
    count=count+1


x = range(3,6)
count = 0
for n in x:
    if count==0:
        print("\nCreate a sequence of numbers from 3 to 5, & print each item in the sequence : ",n)
    else:
        print(" "*79+str(n))
    count=count+1


x = range(3,20,2)
count = 0
for n in x:
    if count==0:
        print("\nCreate a sequence of numbers from 3 to 20, but increment by 2 instead of 1 : ",n)
    else:
        print(" "*78+str(n))
    count=count+1


# reversed() function returns a reversed iterator object.
alph = ["a","b","c","d"]
ralph = reversed(alph)
count = 0
for x in ralph:
    if count==0:
        print("\nReverse the sequence of a list and each item : ",x)
    else:
        print(" "*48+x)
    count=count+1


# round() function return the floating point number that is rounded version of the specified number, with the specified number of decimals.
# The default number of decimal is 0, meaning that the function will return nearest integer.
x = round(53.4789854,2)
y = round(53.5654125)
print("\nRound a number to only two decimal : ",x)
print("Round to the nearest integer : ",y)


# set() function creates a set object. The item in a set are unordered, so it will be appear in random order.
x = (('apple','banana','cherry'))
print("\nCreate a set that containing fruit name : "+str(x))


# setattr() function sets the value of the specified attribute of specified object.
class person:
    name = "Jhon"
    age = 36
    country = "Norway"

setattr(person,'age',40)

# age property will now have the value : 40

x = getattr(person,'age')
print("\nsChange the value of 'age' property of the 'person' object x : ",x)



# slice() function return a slice object, you can specify where to start the slicing and where to end, and you can specify
# the step which allow you to slice only every other item.
a = ("a","b","c","d","e","f","g","h")
x = slice(2)
print("\nCreate a tuple and slice object, use the slice object to get only the two first items of the tuple : ",a[x])

y = slice(3,5)
print("\nCreate a tuple and slice object, start the slice object at position 3, and slice to position 5 and return the result : ",a[y])

z = slice(0,8,3)
print("\nCreate a tuple and slice object, use the step parameter to return every third item : ",a[z])



# sorted() function returns a sorted list of the specified iterable object.
# you can specifiy ascending and descending order, string are sorted in alphabetically and numbers are sorted in numerically.
b = ("b","g","a","d","f","c","h","e")
x = sorted(b)
print("\nSort a tuple : ",x)


c = (1,11,3)
x = sorted(c)
print("\nSort numeric : ",x)


# str() function converts the specified value into a string.
x = str(3.25)
print("\nConvert the 3.25 number into an string : ",x)


# int() function convert the specified value tnto an integer.
x = int("12")
print("\nConvert a string into an integer ; ",x)


# sum() function return the number the sum of all items in an iterable.
x = (1,2,3,4,5)
y = sum(x)
print("\nAdd all items in an tuple, and return the result : ",y)


a = (1,2,3,4,5)
x = sum(x,7)
print("Start with number 7, and add all the items in the a tuple to this number : ",x)


# type() function returns the type of the specified object.
a = ("apple","banana","cherry")
b = "Hello  World"
c = 12

x = type(a)
y = type(b)
z = type(c)

print("\nReturn the type of the object : ",x)
print("Return the type of the object : ",y)
print("Return the type of the object : ",z)



# vars() function returns the_dic_attribute of an object.
# The_dic_attribute is a dictionary containing the object's changeable attributes.
# Note : Calling the vars() function without parameters will return a dictionary containing the local symbol.

class persons:
    name : "Jhon"
    age : 36
    country : "Norway"

x = vars(persons)
print("\n")
print(x)



