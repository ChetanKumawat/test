x = ["Tom","Jerry","Shaw","Hobs"]

print(x)

print(x[1]) # Access the list item by refering to the index number.

x[1] = "Smith"
print(x) # Change the value of specific item, refer to the index number.

for y in x:
  print(y) # Loop through a list

if "Smith" in x:
    print("Yes, 'Smith' is exist in the list.") # Check if item exist. 

print(len(x)) # Check how many items in list.

x.append("Viru")
print(x) # Add an item to the end of the list.

x.insert(1,"Jay")
print(x) # Add an item to the specified index.

x.remove("Jay")
print(x) # Remove items from the list.

x.pop()
print(x) # Remove the specified index (or last item if index is not specified.

del x[0]
print(x) # Remove the specified index.

del x # Delete the list completely.

x = ["Tom","Jerry","Shaw","Hobs"]
x.clear()
print(x) # Empty the list.

y = list(("Apple","Banana","Mango"))
print(y) # list constructor to make a list.

a = ["Jaipur","Hyderabad","Delhi"]
z = a.copy()
print(z) # Return a copy of the specified list.

b = ["Google","Apple","MS","OnePlus","MS"]
c = b.count("MS")
print(c) # Return the number of the element with the specified value.

e = ["Noida","Goa","Pune"]
a.extend(e)
print(a) # Add the specified list element to the end of the current list.

f = a.index("Goa")
print(f) # Return the position of at the first occurrence of the specified value.

a.reverse()
print(a) # Reverse the sorting order of the element.

a.sort()
print(a) # Sort the list.
