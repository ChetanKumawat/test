a = 32
b = 253
if b > a:
 print("a = "+str(a)+"\nb = "+str(b)+"\na > b :\n""b is greater than a\n")

c = 32
print("a = "+str(a)+"\nc = "+str(c)+"\na == c :")
if c > a:
 print("c is greater than a")
elif a == c:
 print("a and c are equal") 

d = 365
e = 254
print("\nd = "+str(d)+"\ne = "+str(e)+"\ne > d :")
if e > d:
 print("e is greater than d")
elif e == d:
 print("d and e are equal")
else:
 print("d is greater than e")

print("\nShort Hand If")
if d > e: print("d is greater than e")

print("\nAND keyword for combine conditional statement")
print("b = "+str(b)+"\nd = "+str(d)+"\ne = "+str(e)+"\ne > b and d > e :")
if e > b and d > e:
 print("Both conditions are True")

print("\nOR keyword for at least one statement is true")
print("a = "+str(a)+"\nb = "+str(b)+"\nd = "+str(d)+"\na > b or a < d :")
if a > b or a < d:
 print("At least one of the condition is true") 
