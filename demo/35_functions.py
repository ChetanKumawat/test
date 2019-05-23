def my_function():
 print("Analytics..!\n")

my_function()

#---------------------------------------------------------------------------------------------------

def func(fname,count):
 
 if count==0:
 	print("Parameter are specified after the function name, inside the parentheses : " +str(fname)+ " Smith")
 else:
	print(" "*74+fname + " Smith")
 count=count+1
	
func("Jeck",0)
func("Jeson",1)
func("Jerry",1)

#-----------------------------------------------------------------------------------------------------

print("\nDefault parameter value : ")
def func1(country = "Norway"):
	print(" "*25+str("I am from ")+ country)
 
func1("Sweden")
func1("Bazil")
func1()
func1("India")

#----------------------------------------------------------------------------------------------------

def func2(x):
 return 5 * x

print("\nReturn statement : "+str(func2(3)))
print(" "*19+str(func2(5)))
print(" "*19+str(func2(4)))

#------------------------------------------------------------------------------------------------

def tri_recursion(k):
	if (k>0):
		result = k+tri_recursion(k-1)	
		print(result)
	else:
		result = 0
	return result
print("\nRecursion result")
tri_recursion(6)


