x = { "brand":"Ford",
      "model":"Mustang",
      "year":"1964"
    }

print(x) 

y = x["model"]
print("\nCar model : "+y+"\n") #You can access the items of a dictionary by reffering to it's key name, inside square brackets.

z = x.get("model")
w = x.get("price",1500000) 
print("Car model : "+str(z)) #Get the value of key also using get() method.
print("Car price : "+str(w)+"\n") #Get the values that doesn't exist.

print("Change the 'year' key value :")
x["year"] = 2018
print(str(x)+"\n") #You can change the value of a specific item by reffering to it's key name.

print("Print all key names in the dictionary, one by one :")
for z in x:
 print(z)

print("\nPrint all values in the dictionary one by one :")
for z in x:
 print(x[z])

print("\nUsing values() function also return all values in the dictionary one by one :")
for z in x.values():
 print(z)

print("\nUsing items() function return all keys and values in the dictionary :")
for y, z in x.items():
 print(y,z)

print("\ncopy() method return a copy of specified dictionary :")
b = x.copy()
print(b)

print("\nfromkeys() method returns a dictionary with the specified keys and values :")
c = ('Jeck','Jerry','Herry')
d = 1
e = dict.fromkeys(c,d)
print(e)

print("\nfromkeys() method returns a dictionary with specified keys and without values :")
f = dict.fromkeys(c)
print(f)

print("\nitems() method return a view object that contain keys-values pair of the dictionary as tuple in a list :")
g = x.items()
print(g)

print("\nUsing items() method, when an item in the dictionary change value, the view object also updated :")
h = x.items()
x["year"] = 2019
print(h)

print("\nkeys() method return a view object that contain keys of the dictionary as a list :")
i = x.keys()
print(i)

print("\nsetdefault() method return the value of the item with the specified key :")
l = x.setdefault("model","Bronco")
print(l)

print("\nGet the value of item if item doesn't exist using setdefault() method :")
m = x.setdefault("color","White")
print(m)

print("\nupdate() method insert the specified item to the dictionary :")
x.update({"CCeng": 1250})
print(x)

if "model" in x:
 print("\nYes, 'model' is one of the keys in the x dictionary.\n")

print("Using len() function determine how many items a dictionary has :")
print(len(x))

print("\nAdding an item to the dictionary is done by using a new index key and assigning a value to it :") 
x["color"] = "Blue"
print(x)

print("\npop() method remove the item with specified key name :")
x.pop("model")
print(x)

print("\nThe value of removed item is the return value of the pop() method :")
j = x.pop("year")
print(j)

print("\npopitem() mathod remove the last inserted item :")
x.popitem()
print(x)

print("\nThe value of removed item is the return value of popitem() method :")
k = x.popitem()
print(k) 

print("\ndel() mathod also remove the item with specified key name :")
del x["brand"]
print(x)

a = dict(brand="Audi",model="Q3",year=2015)
print("\n"+str(a)+"\n")

print("clear() keyword empties the dictionary :")
a.clear()
print(a)

print("\ndel() mathod can also delete the dictionary completely, this will cause an error because x is no longer exist.")
del x
print(x)
