# Return the absolute value of a number.
a = -7.25
b = abs(a)
print('Absolute value of '+str(a)+' : ' + str(b))


# Return the absolute value of a complex number.
c = 3+5j
d = abs(c)
print("Absolute value of complex number"+str(c)+" : "+str(d))


# all() function returns True if all items in an iterable(list,tuple,set,dictionary) are true, otherwise it returns false.
mylist = [True,True,True]
e = all(mylist)
print("Retrun true if all items in list are true : "+str(e))


mylists =[0,1,1]
f = all(mylists)
print("Retrun true if all items in list are true : "+str(f))


mytuple = (0,True,False)
g = all(mytuple)
print("Return true if all items in tuple are true : "+str(g))


myset = {0,1,0}
h = all(myset)
print("Return true if all items in set are true : "+str(h))


mydict = {0 : "Richard", 0 : "Vely"}
i = all(mydict)
print("Return true if all items in dictionary are true : "+str(i))



# any() function return True if any items in an iterable(list,tuple,set,deictionary) are true, otherwise it return False.
mylistany = [False,True,False]
j = any(mylistany)
print("Retrun true if any items in list is true : "+str(j))


mytupleany = (0,1,False)
k = any(mytupleany)
print("Return true if any items in tuple is true : "+str(k))


mysetany = {0,1,0}
l = any(mysetany)
print("Return true if any items in set is true : "+str(l))


mydictany = {0:"Apple",1:"Banana"}
m = any(mydict)
print("Retrun true if any items in dictionary is true : "+str(m))


# The ascii() function returns a readable version of any objects(String,Tuple,List,etc.).
# ascii() function will replace any non ascii character with escape characters
n = ascii("My name is Ståle")
print("ascii() function will replace any non ascii character with escape characters : "+str(n))


# The bin() function return the binary version of specified integer.
o = bin(36)
print("bin() function return the binary verion of 45 number : "+str(o))


# The bool() function return the boolean value of a specified object.
p = bool(2)
print("bool() funtion return the boolean  2 value : "+str(p))


# The bytearray() function returns a bytearray object.
# It can convert objects into bytearray objects, or create empty bytearray object of the specified size.
q = bytearray(4)
print("Return an array of 4 bytes : "+str(q))


# The byte() function return a bytes object.
# It can convert objects into bytes objects, or create empty bytes object of the specified size.
# Difference : byte() retrun an object that cannot modified but bytearray() return an object that can be modified.
r = bytes(4)
print("Return an array of 4 bytes : "+str(r))


# Returns True if the specified object is callable, otherwise False.
# Check function is callable.
def x():
    a = 5
print(callable(x))


# chr() function return the character that represents the specified unicode.
# get the character that represent the unicode 97
s = chr(97)
print("chr() funtion return the character that represent the unicode 97 : "+s)


# compile() function returns the specified source as a code object, ready to be executed.
t = compile('print(55)','text','eval')
exec(t)
print("\n")

u = compile('print(55)\nprint(88)','text','exec')
exec(u)


# complex() function returns a complex number by specifying a real number and imaginary number.
v = complex(3,5)
print("\nConvert the real number 3 and imaginary number 5 into a complex number : "+str(v))


# delsttr() function will delete the specified attribute from the specified object.
class person:
    name = "Jone"
    age = 36
    country = "Canada"

delattr(person,'age')
print("\nAttribute deleted successfully from object\nThe person object will no longer contain an 'age' property\n")


# dict() function create dictionary
w = dict(name = "john",age = 36, country = "Norway")
print("Create dictionary : ",w)


# dir() function returns all properties and method of the specified of object(even built-in properties which are default for all object), without the values.
class pers:
    name = "John"
    age = 36
    country = "Norway"

print(dir(pers))

# divmod() function return the quotient and remainder.
x = divmod(13,2)
print("\ndivmod() function return the quotient and remainder of 13 divided by 2 : ",x)


# enumerate() function takes a collection(eg. tuple) and return it as an enumerate object.
x = ('Apple','Banana','Cherry')
y = enumerate(x)

print(list(y))


# eval() function evaluates the specified expression, if the expression is a legal python statement, it will be executed.
# It accept a single expression.
x = 'print(55)'
print("\neval() function execute legal code : ")
eval(x)


# exec() funtion executes the specified Python code.
# It accept large block of code.
x = 'name = "John"\nprint(name)'
print("\nexec() function execute large block of Python code ; ")
exec(x)


# filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
age = [5,12,17,18,24,32]

def myfunc(x):
    if x < 18 :
        return False
    else:
        return True

adults = filter(myfunc,age)
count = 0
for x in adults:
    if count==0:
        print("\nfilter() function : ",x)
    else:
        print(" "*21+str(x))
    count=count+1


# float() function return a floating point number(number or string that can be converting in floating number).
x = float(3)
print("\nfloat() function : ",x)



# format() function formats a specified value into a specified format.
x = format(5,'%')
print("\nformat() function formats a specified value into a specified format : "+x)


# frozenset() function returns an unchanable frozenset object
frozlist = ['apple','banana','cherry']
x = frozenset(frozlist)
print("\nFreez the list and make it unchangable : "+str(x))