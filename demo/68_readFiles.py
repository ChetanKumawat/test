# By default read() method return the whole content of the file, but you can also specify how many characters you want to return:

f = open("demofile.txt","r")

print(f.read(5))