# The readline() method return the one line of the file:

f = open("demofile.txt","r")

print(f.readline())

# if you calling the readline() method two times, you can read the two first lines
print(f.readline(),"\n\n\n")


# By looping through the lines of the file, you can read the whole file, line by line:
file = open("demofile.txt","r")
for x in file:
    print(x)
# Close the file when you done with it:
    f.close()


