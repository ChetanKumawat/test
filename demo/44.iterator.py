mytuple = ("apple","mango","cherry")
myit = iter(mytuple)

print("Return an itrator from tuple and print each value : "+next(myit))
print(" "*52+next(myit))
print(" "*52+next(myit))

#-------------------------------------------------------------------------------------

mystr = "banana"
myit = iter(mystr)

print("String are iterable objects, containing a sequence of characters : "+next(myit))
print(" "*67+next(myit))
print(" "*67+next(myit))
print(" "*67+next(myit))
print(" "*67+next(myit))
print(" "*67+next(myit))

#-------------------------------------------------------------------------------------

mytuple = ("apple","banana","cherry")
count = 0
for x in mytuple:
    if count==0:
        print("Looping through an iterator")
        print("Iterate the value of tuple: "+x)
    else:
        print(" "*28+x)
    count=count+1

#--------------------------------------------------------------------------------------

mystr = "banana"
count = 0
for x in mystr:
    if count==0:
        print("Iterate the character of string : "+x)
    else:
        print(" "*34+x)
    count=count+1

#--------------------------------------------------------------------------------------

class myNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = myNumber()
myiter = iter(myclass)

print("Create an iterator that returns numbers, starting with 1 and each sequence will increase by one : "+str(next(myiter)))
print(" "*98+str(next(myiter)))
print(" "*98+str(next(myiter)))
print(" "*98+str(next(myiter)))
print(" "*98+str(next(myiter)))

#-----------------------------------------------------------------------------------------

class mynum:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclasses = mynum()
myiter = iter(myclasses)

count = 0

for x in myiter:
    if count==0:
        print("Retun number using StopIteration statement and condition : "+str(x))
    else:
        print(" "*59+str(x))
    count=count+1