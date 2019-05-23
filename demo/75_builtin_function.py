# zip() function return iterator from two or more iterators.
# zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired
# together, and second item in each passed iterator are paired together etc.
# Note : if the passed iterators have different lengths, the iterator with least items decides the length of new iterator.
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:
print("Join two tuples together : ")
print(tuple(x))






a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica","Vicky")

x = zip(a, b)
print("\nIf one tuple contain more item, these items are ignored : ")
print(tuple(x))
