x = ("Joy","Smith","Roy")
print(x)

print(x[1]) # You can access tuple item by referring to the index number, inside square brackets.

for y in x:
 print(y) # Loop through a Tuples.

if "Roy" in x:
    print("Yes,'Roy' is in the list.") # Check if item is exists.

print(len(x)) # Print number of items in the tuple.

#del x
# print(x) # This will be raise an error because the tuple no longer exists.

a = tuple(("Ape","Ban","Ches","Ape"))
print(a) # tuple() method to make a tuple

e = (1,2,3,4,5,6,1,5,3,4,2,1)
b = e.count(1)
print(b) # Return the number of time a specified value appears in tuple.

