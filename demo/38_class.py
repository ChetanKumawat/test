class myClass:
 x = 7
print("Create class : "+str(myClass))

p1 = myClass()
print("\nUsing class name create object : "+str(p1.x)+"\n")

class person:
 def __init__(self,name,age):
	self.name = name
	self.age = age 
p1 = person("Jhon", 36)
print(p1.name)
print(str(p1.age)+"\n")

class pers:
 def __init__(self,name,age):
	self.name = name
	self.age = age
 def myfunc(self,a,b):
	print("Hello my name is "+ self.name+" a"+a+"b"+b)
p1 = pers("Hobs",30)
p1.myfunc("a","b")


class prsn:
  def __init__(mysillyobject, name, age):
	mysillyobject.name = name
	mysillyobject.age = age
  def myfunc(abc):
	print("\nHello my name is " + abc.name)
p1 = prsn("Jeck", 45)
p1.myfunc()

class prn:
  def __init__(a,name, age):
	a.name = name
	a.age = age
  def myfunc(b):
	print("\nPredictive " + b.name)
p1 = prn("Analytics..!",50)
p1.age = 30
p1.myfunc()
print(p1.age)


class prn:
  def __init__(a,name, age):
	a.name = name
	a.age = age
  def myfunc(b):
	print("\nPredictive " + b.name)
p1 = prn("Analytics..!",50)
del p1.age
print(p1.age)


class prsn:
  def __init__(a,name,age):
	a.name = name
	a.age = age
  def myfunc(b):
	print("Hello my name is " +b.name)
p1 = prsn("Jerry",50)
del p1
print(p1)
