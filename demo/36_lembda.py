x = lambda a : a + 10
print("Add number to argument using lambda function : "+str(x(5)))

z = lambda a, b : a * b
print("Multiplies arguments using lambda function : "+str(z(5, 6)))

y = lambda a, b, c : a + b + c
print("Sum the arguments using lambda function : "+str(y(5, 6, 7)))

def myfunc(n):
 return lambda a : a * n
mydoubler = myfunc(2)
print("Make function that double the number that you send in : "+str(mydoubler(11)))

def myfunc1(n):
 return lambda a : a * n
mytripler = myfunc(3)
print("Make function that tripler the number that you send in : "+str(mytripler(11)))


count = 0
def myfunc2(n):
 return lambda a : a * n
mydoublers = myfunc2(2)
mytriplers = myfunc2(3)

if count==0:
	print("Use the same function definition to make both functions, in the same program : "+str(mydoublers(11)))
else:
	print(" "*50+str(mytriplers(11)))
count=count+1

