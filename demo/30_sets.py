x = {"Jerry","Tom","Richard"}

print(x)

for y in x:
 print(y)

print("Tom" in x)

x.add("Jeck")
print("Add single items :",x) # add items

x.update({"Amazon","Facebook","Google"})
print("Add multiple items using update() function :",x) # Add multiple items using update function

print("Total items in set :", len(x)) # Determine how many items a set has

x.remove("Facebook")
print("Remove an item from set using remove() function :",x)

x.discard("Jerry")
print("Remove an item from set using discard() function :",x)

y = x.pop()
print("This item will be remove from set using pop() function:",y)
print("Remove an item from set using pop() function :",x)

c = set(("IronMan","Thor","Jeck"))
print("Using set() constructor to make a set ",c)

d = c.copy()
print("copy() method use for copy the set :",d)

e = x.difference(c)
print("The difference() method returns a set contains items that exist only in the first set, and not in both sets :",e)

f = {"apple", "banana", "cherry"}
g = {"google", "microsoft", "apple"} 
f.difference_update(g) 
print("difference_update() method removes the items that exist in both sets and return first set :",f)

f = {"apple", "banana", "cherry"}
g = {"google", "microsoft", "apple"} 
h = f.intersection(g)
print("intersection() method return a set that contain items that exist in both set :",h)

f.intersection_update(g)
print("intersection_update() method removes the items that not present in both sets :",f)

i = {"apple","banana","cherry"}
j = {"oracle","graps","papaya"}
k = i.isdisjoint(j)
print("isdisjoint() method return True if none of the item are present in both sets, otherwise return False :",k)

l = {"a", "b", "c"}
m = {"f", "e", "d", "c", "b", "a"}
n = l.issubset(m)
print("issubset() method return True if all items in the set exist in the set specified set, otherwise it return False :",n) 

o = {"f", "e", "d", "c", "b", "a"}
p = {"a", "b", "c"}
q = o.issuperset(p)
print("issuperset() method return True if all items set l are present in set p :",q)

r = {"apple", "banana", "cherry"}
s = {"google", "microsoft", "apple"} 
t = r.symmetric_difference(s)
print("symmetric_difference() method retrun a set that contains all items from both sets, except that items that present in both sets :",t)

r.symmetric_difference_update(s)
print("symmetric_difference_update() method remove items that are present in both sets, And insert the items that is not present in both sets :",r)

u = r.union(s)
print("union() method retrun a set that contain all items from both sets, duplicate are excluded :",u)

x.clear()
print("Clear() method empties the set :",x)

a = {"apple", "banana", "cherry"}
del a
print("del keyword delete the set completely :",a) #this will raise an error because the set no longer exists

