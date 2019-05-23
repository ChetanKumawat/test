mob = ["Apple","BlackBerry","Motorola"]

count=0
for x in mob:
    if count==0:
       print("1) For loop : "+x)
    else:
       print(" "*11+x)
    count=count+1


count=0
for x in "Apple":
    if count==0:
       print("\n2) Looping through a String : "+x)
    else:
      print(" "*30+x)
    count=count+1

count=0        
for x in mob:
	if count==0:
		print("\n3) With 'Break Statement', we can stop the loop before it has looped through all the items : "+x)
	elif x=="BlackBerry":
		print(" "*93+x)
		break
	count=count+1

 
count=0
for x in mob:
	if count==0:
		print("\n4) 'Break Statement' come before the print : "+x)
  	elif x == "banana":
    		break
  		print(x)
	count=count+1


count=0
for x in mob:
  	if count==0:
		print("\n5) With 'Continue Statment' we can stop the current iteration of the loop and continue with the next : "+x)
  	elif x == "BlackBerry":
    		continue
    	print(" "*103+x)
	count=count+1

count=0
for x in range(6):
	if count==0:
		print("\n6) range() funtion return the sequence of number, starting from 0 by default : "+str(x))
	else:
		print(" "*79+str(x))
	count=count+1

count=0
for x in range(2,6):
	if count==0:
		print("\n7) range() function, possible to specify the starting value by adding a parameter : "+str(x))
	else:
		print(" "*84+str(x))
	count=count+1

count=0
for x in range(2,30,3):
	if count==0:
		print("\n8) range() function, possible to specify the increment value by adding 3rd parameter : "+str(x)) 
	else:
		print(" "*87+str(x))
	count=count+1

adj = ["Red","Tasty","Big"]
count=0
for x in adj:
	for y in mob:
		if count==0:
			print("\n9) Nested Loop..! : "+str(x)+" "+str(y))
		else:
			print(" "*20+str(x)+" "+str(y))
		count=count+1
