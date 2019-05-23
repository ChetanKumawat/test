# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

a = int(input("Input an integer : ")) # takes integer as input and stores it as integer in variable a # consider input as 7
n1 = int( "%s" % a ) # when "%s" will give you result "7" and it is stored in n1 as integer 7 because int() is used as int("7")
n2 = int( "%s%s" % (a,a) ) # similarly when %s is written twice it requires two numbers in this case it is same hence you will get "77" to converted to integer and stored in n2
n3 = int( "%s%s%s" % (a,a,a) ) # just like n2 number is used three times instead of two so you will get n3=777 in this case
print (n1+n2+n3) # as all values of n1,n2 and n3 are integer it can be added 7+77+777 and you will get result 861



# a = input("Input an integer : ")  # python 2 would need raw_input or the result would be incorrect
# print (sum(int(a*i) for i in range(1,4)))

