# 'a' - will be append to the end of the file, create the file if file doesn't exist:
f = open("demofile.txt","a")
f.write("\nNow the file has more content")
f.close()

# Open and read the file after appending:
f = open("demofile.txt","r")
print(f.read())
