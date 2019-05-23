# You can use else keyword to define a block of code to be executed if no error were raised.
#The try block does not raise any error, so else block is executed.

try:
    print("Hello")
except:
    print("Someting went wrong")
else:
    print("Nothing went wrong")