cars = ["Mustang","Ford","Volvo"]
print(cars)

x = cars[0]
print("Access the element of the aaray by refering the index number : "+str(x))

cars[1] = "Toyoto"
print("Modify the values of the array : "+str(cars))

x = len(cars)
print("len() method return the length of array : "+str(x))

count = 0
for x in cars:
 if count==0:
 	print("Looping array element : "+str(x))
 else:
 	print(" "*24+str(x))
 count=count+1


cars.append("Honda")
print("append() method add an element to array : "+str(cars))


cars.pop(1)
print("Remove the array element : "+str(cars))

cars.remove("Volvo")
print("Delete the array element that remove first occurrence of the specified value : "+str(cars))

#x = cars.copy()
#print(x)

x = cars.count("Mustang")
print("count() method return the number of element with specified value : "+str(x))

name = ['Tom','Dom','Jerry']
cars.extend(name)
print("extend() method add specified list element to the end of the current of the list : "+str(cars))

x = cars.index("Tom")
print("index() method return the position of specified value : "+str(x))

cars.insert(2,"Chetan")
print("insert() method insert the specified value at the specified position : "+str(cars))

cars.reverse()
print("reverse() method reverse the sorting order of element : "+str(cars))

cars.sort()
print("sort() method sorts the list ascending : "+str(cars))

cars.sort(reverse=True)
print("sort() method with reverse parameter will sort the list descending : "+str(cars))

def myfunc(e):
 return len(e)
car = ['Ford','Mitsubishi','BMW','VW']
car.sort(key=myfunc)
print("Sort the list by the length of value : "+str(car))

def myfunc1(e):
 return e['year']
car = [
	{'car': 'Ford', 'year': 2005},
	{'car': 'Mitsubishi','year': 2000},
	{'car': 'BMW', 'year': 2019},
  	{'car': 'VW', 'year': 2011}
      ]
car.sort(key=myfunc1)	
print("Sort a list of dictionaries based on the 'year' value of the dictionaries : "+str(car)) 


def myfunc2(e):
 return len(e)
car = ['Ford','Mitsubishi','BMW','VW']
car.sort(reverse=True, key=myfunc2)
print("Sort the list by the length values and reserved : "+str(car))



