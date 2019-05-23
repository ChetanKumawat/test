# 'r+' is used for reading and writing :
try:
  f = open("demofile.txt",'r+')
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
