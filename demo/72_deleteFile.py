# Remove file you must import the 'OS' module and run it's os.remove function
import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("The file deleted successfully deleted.")
else:
    print("The file does not exist")