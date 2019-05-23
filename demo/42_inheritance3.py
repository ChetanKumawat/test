class person:
  def __init__(self,fname,lname):
	self.firstname = fname
	self.lastname = lname

  def printname(self):
	print(self.firstname,self.lastname)

class student(person):
  def __init__(self,fname,lname,year):
	person.__init__(self,fname,lname)
	self.graduationyear = year

x = student("Tom","Jerry",2019)
x.printname()
print(x.graduationyear)
