print("While Loop :")
i = 1
while i <= 10:
 print(i)
 i += 1

print("\nWe can stop the loop even if the while condition is True with 'Break Statement' :")
a = 1
while a <= 10:
 print(a)
 if a == 3:
  break 
 a += 1

print("\nWe can stop the current iteration, and continue with the next with 'Continue Statement' :") 
b = 0
while b < 10:
 b += 1
 if b == 3:
  continue
 print(b)
