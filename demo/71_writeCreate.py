# 'w' will overwrite any existing content in the file

f = open("demofile1.txt", "w")
f.write("Hello! Welcome to demofile.txt \nThis file is for testing purposes. \nGood Luck!")
f.close()

# 'a' will append to the end of the file, create the file if doesn't exist:

f = open("demofile1.txt", "a")
f.write("\nNow the file has more content")
f.close()

# 'w' will overwrite the file content
f = open("demofile1.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after appending:

f = open('demofile1.txt', "r")
print(f.read())

# 'x' will create a file, return error if specified file exist

f = open("myfile.txt", "x")




